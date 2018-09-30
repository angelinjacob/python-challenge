# main.py in pyPoll
#The total number of votes cast -> number of records in the CSV
#A complete list of candidates who received votes -> list of names unique and the total number of records for that candidate
# The percentage of votes each candidate won -> number of records the candidate has / total number of records in the file
# winner -> greatest total number of records for that candidate
import os
import csv

with open("election_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
     # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
     # Read first row of data after the header
    csv_header = next(csvreader)
    cname = csv_header[2]
    cvotes = 1
    candidates = {cname : cvotes} #dictionary created with name as key and count of votes as value
    for row in csvreader:
        if candidates.get(row[2]):
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
#csv file read complete
    total_votes = 0        
    total_candidates = len(candidates)
    for x in candidates.values():
        total_votes += x

    file1 = open("pyPoll.txt","w") 
    file1.write("Election Results\n")
    file1.write("-------------------------\n")
    file1.write("Total Votes: " + str(total_votes) + "\n") #3521001
    file1.write("-------------------------\n")        
    print("Election Results\n")
    print("-------------------------")
    print("Total Votes: " + str(total_votes) + "\n") #3521001
    print("-------------------------\n")
    winner_votes = 0
    winner =  ""
    for x in candidates:
        print(x + " : " + str(round(candidates[x] / total_votes * 100, 5)) + "% (" + str(candidates[x]) + ")")
        file1.write(x + " : " + str(round(candidates[x] / total_votes * 100, 5)) + "% (" + str(candidates[x]) + ")\n")
        if candidates[x] > winner_votes:
            winner_votes = candidates[x] 
            winner = x
    print("-------------------------")
    print("Winner : " + winner)
    print("-------------------------")
    file1.write("-------------------------\n")
    file1.write("Winner : " + winner + "\n")
    file1.write("-------------------------")
    file1.close()
"""
class candidates:
    cname = ""
    cvotes = 0

c = candidates()
c.cname = input("name :")
c.cvotes = input("votes :")
print(c.cname)
print(c.cvotes)

The winner of the election based on popular vote.
print("Election Results")
print("-------------------------")
print("Total Votes: " + total_votes) #3521001
print("-------------------------")
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
print("-------------------------")
Winner: Khan
-------------------------
"""
