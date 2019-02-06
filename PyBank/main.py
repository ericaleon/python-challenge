#import needed modules
import os
import csv

#declare lists & variables
months = []
curr_mo_val = 0
last_mo_val = 0
total_prof = 0
change_prof = 0
sum_change = 0
avg_change = 0
max_inc = 0
min_dec = 0
min_mo = ""
max_mo = ""

#define filepath
csvpath=os.path.join("Resources","budget_data.csv")

#read file
with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

#set up header
    header = next(csv_reader)

    #iterate through each row in csv file
    for row in csv_reader:
        #build months list from date column using values in each row
        months.append(row[0])
        #set value for current month's profit/losses
        curr_mo_val = int(row[1])
        #add current month value to running total of profit/losses
        total_prof += curr_mo_val
        #conditional to skip row 1 and capture month-to-month change in profit/losses
        if last_mo_val != 0:
            change_prof = int(curr_mo_val - last_mo_val)
            sum_change += change_prof

        #grab max increase and min decrease values for change in profit
        #also capture date value for each       
        if change_prof > max_inc:
            max_inc = change_prof
            max_mo = row[0]
        elif change_prof < min_dec:
            min_dec = change_prof
            min_mo = row[0]

        #reset previous month value before going to next row in loop
        last_mo_val = curr_mo_val

#calculate total number of months and the average change in profit/loss
total_mos = len(months)
avg_change = sum_change/(total_mos -1)

#print outputs to terminal
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {total_mos}")
print(f"Total: ${total_prof}")
print(f"Average  Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {max_mo} (${max_inc})")
print(f"Greatest Decrease in Profits: {min_mo} (${min_dec})")

#create text file and print outputs to text
text_file = open("Output.txt", "w")

print("Financial Analysis",file=text_file)
print("----------------------------------",file=text_file)
print(f"Total Months: {total_mos}",file=text_file)
print(f"Total: ${total_prof}",file=text_file)
print(f"Average  Change: ${avg_change:.2f}",file=text_file)
print(f"Greatest Increase in Profits: {max_mo} (${max_inc})",file=text_file)
print(f"Greatest Decrease in Profits: {min_mo} (${min_dec})",file=text_file)

#close text file
text_file.close()