#import needed modules
import os
import csv

#define filepath
csvpath=os.path.join("Resources","election_data.csv")

#declare initial variables
total = 0
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0
winner = ''

#open and read file as dictionary
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    #loop through each row and capture total and candidate counts
    for row in reader:
        if row["Candidate"] == "Khan":
            votes_khan += 1
        elif row["Candidate"] == "Correy":
            votes_correy += 1
        elif row["Candidate"] == "Li":
            votes_li += 1
        elif row["Candidate"] == "O'Tooley":
            votes_otooley += 1

        total += 1

    #conditional to determine which candidate has greatest number of votes
    if votes_khan > votes_correy and votes_khan > votes_li and votes_khan > votes_otooley:
        winner = "Khan"
    elif votes_correy > votes_li and votes_correy > votes_otooley:
        winner = "Correy"
    elif votes_li > votes_otooley:
        winner = "Li"
    else:
        winner = "O'Tooley"

#calculate percentages based on votes per candidate and total votes
pct_khan = votes_khan*100/total
pct_correy = votes_correy*100/total
pct_li = votes_li*100/total
pct_otooley = votes_otooley*100/total

#output results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
print(f"Khan: {pct_khan:.3f}% ({votes_khan})")
print(f"Correy: {pct_correy:.3f}% ({votes_correy})")
print(f"Li: {pct_li:.3f}% ({votes_li})")
print(f"O'Tooley: {pct_otooley:.3f}% ({votes_otooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#create text file and print outputs to text
text_file = open("Output.txt", "w")

print("Election Results",file=text_file)
print("-------------------------",file=text_file)
print(f"Total Votes: {total}",file=text_file)
print("-------------------------",file=text_file)
print(f"Khan: {pct_khan:.3f}% ({votes_khan})",file=text_file)
print(f"Correy: {pct_correy:.3f}% ({votes_correy})",file=text_file)
print(f"Li: {pct_li:.3f}% ({votes_li})",file=text_file)
print(f"O'Tooley: {pct_otooley:.3f}% ({votes_otooley})",file=text_file)
print("-------------------------",file=text_file)
print(f"Winner: {winner}",file=text_file)
print("-------------------------",file=text_file)

#close text file
text_file.close()
