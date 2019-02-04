import os
import csv

csvpath=os.path.join("Resources","budget_data.csv")

#Declare variables for min, max, total profit and set initial values
max_inc = 0
min_dec = 0
total_prof = 0
change_prof = 0
sum_change = 0
avg_change = 0
curr_mo_val = 0
last_mo_val = 0
min_mo = ""
max_mo = ""

#define lists & variables
months = []

#read file
with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

#set up header
    header = next(csv_reader)

    #iterate through rows in csv file
    for row in csv_reader:
        #build months with values in each row
        months.append(row[0])
        curr_mo_val = int(row[1])
        total_prof += curr_mo_val
        if last_mo_val != 0:
            change_prof = int(curr_mo_val - last_mo_val)
            sum_change += change_prof
                
        if change_prof > max_inc:
            max_inc = change_prof
            max_mo = row[0]
        elif change_prof < min_dec:
            min_dec = change_prof
            min_mo = row[0]
        last_mo_val = curr_mo_val
            #for average change in profit/loss, populate prof_change with month-to-month changes
            #average is equal to sum of values in prof_changes divided by len(prof_change)

total_mos = len(months)
avg_change = sum_change/(total_mos -1)

print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(total_mos))
print("Total: $",total_prof)
print("Average  Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + str(max_mo) + "(" + str(max_inc) + ")")
print("Greatest Decrease in Profits: " + str(min_mo) + "(" + str(min_dec) + ")")

#output to text