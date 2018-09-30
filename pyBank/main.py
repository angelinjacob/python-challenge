#main py in pyBank

"""
average change as integer 
total change as integer
greatest increase in profits (date , value)
greatest decrease in profits (date, value)
total months as integer
total profits/loses as integer
record 1 (date, value)
record 2 (date, value)

open the csv file in read mode
    read record 1 and record 2
    /* set values for 
    total months as integer = total months + 1
    total profits/loses as integer = total profits/losses + record1.profits/losses + record2.profits/losses
    total change = record 2. profits/losses - record 1.profits/losses
    greatest increase in profits (date , value) =  record 2. profits/losses - record 1.profits/losses 
    greatest decrease in profits (date, value) = record 2. profits/losses - record 1.profits/losses 
    */
read record i from 3 until end of file
    total months as integer = total months + 1
    total profits/loses as integer = total profits/losses + record(i).profits/losses
    total change = total change + record (i). profits/losses - record (i-1).profits/losses
    ifrecord (i). profits/losses - record (i-1).profits/losses > greatest increase in profits (date , value) then
         greatest increase in profits (date , value) =  record (i). profits/losses - record (i-1).profits/losses 
    if record (i). profits/losses - record (i-1).profits/losses < greatest decrease in profits (date , value)
        greatest decrease in profits (date, value) = record (i). profits/losses - record (i-1).profits/losses 

average change as integer = total change / (total months - 1)

print total months
print total profits/loses
print average change
print greatest increase in profits (date , value)
print greatest decrease in profits (date, value)

write a text file with the output
greatest_inc[0] = row[0]
        greatest_inc[1] = row[1]
        greatest_dec[0] = row[0]
        greatest_dec[1] = row[1]
"""
import os
import csv
total_months = 0
total_turnover = 0
total_change = 0
previous = 0
greatest_inc = ["date", 0]
greatest_dec = ["date", 0]
#csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")
with open("budget_data.csv", newline='') as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
     # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
     # Read each row of data after the header
    print(csvreader)
    for row in csvreader:
        print(row[0] + " first loop " + row[1])
        total_months = total_months + 1
        total_turnover = total_turnover + int(row[1])   
        previous = int(row[1])
        break
    for row in csvreader:
        print(row[0] + " second loop " + row[1] + "  " + str(int(row[1]) - previous))
        total_months = total_months + 1
        total_turnover = total_turnover + int(row[1])   
        total_change = total_change + (int(row[1]) - previous)
        if (int(row[1]) - previous) > int(greatest_inc[1]): 
            greatest_inc[0] = row[0]
            greatest_inc[1] = int(row[1]) - previous
        if  greatest_dec[1] == 0:
            greatest_dec[0] = row[0]
            greatest_dec[1] = int(row[1]) - previous
        elif (int(row[1]) - previous) < int(greatest_dec[1]):
            greatest_dec[0] = row[0]
            greatest_dec[1] = int(row[1]) - previous
        previous = int(row[1])

    avg_change = total_change / (total_months-1)
    print("Financial Analysis " + "\n" + "---------------------")
    print("Total months : " + str(total_months))
    print("Total : $" + str(total_turnover))
    print("Average Change : $" + str(round(avg_change,2)))
    #file1.write("total_change  " + str(total_change) + "\n")
    print("Greatest increase in profits : " + greatest_inc[0] + "  " + "($" + str(greatest_inc[1]) + ")")
    print("Greatest decrease in profits : " + greatest_dec[0] + "  " + "($" + str(greatest_dec[1]) + ")")
file1 = open("pyBank.txt","w") 
file1.write("Financial Analysis " + "\n" + "---------------------" + "\n")
file1.write("Total months : " + str(total_months) + "\n")
file1.write("Total : $" + str(total_turnover) + "\n")
file1.write("Average Change : $" + str(round(avg_change,2)) + "\n" )
#file1.write("total_change  " + str(total_change) + "\n")
file1.write("Greatest increase in profits : " + greatest_inc[0] + "  " + "($" + str(greatest_inc[1]) + ")\n")
file1.write("Greatest decrease in profits : " + greatest_dec[0] + "  " + "($" + str(greatest_dec[1]) + ")\n")
file1.close(0)