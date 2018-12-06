#Election.python-challenge/PyPoll
#Author : Suvrangshu Ghosh
#Date : 12 Dec 2018
#Change log :
#------------
#
#
#
#-----------------------------
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv
import operator

#set file path
csvpath = os.path.join("..", "/Users/sghosh/Documents/Suv/Personal/Berkeley/python-challenge/PyPoll", "election_data.csv")

#set output .txt file
outputpath = "/Users/sghosh/Documents/Suv/Personal/Berkeley/python-challenge/PyPoll/election_result.txt"

filewrite = open(outputpath,"w") 

#Variables
#-----------------------------------------
count = 0
wintot = 0
cantot = 0
winner = " "
change = 0
vote = 0
voteprcnt = 00.00
candt = " "
PL_list = []
writetxt = " " 
#-----------------------------------------

#get the list of rows in the csv file
file = open(csvpath)
totline = len(file.readlines()) #get total records 
#print("Number of rows in the file = " + str(totline))

#total votes = totline - 1 (skip the header row)
totline = totline - 1
#------------------------------------------
print("Election Results")
print(f"_______________")
print('\n') #print newline
filewrite.write("Election Results" + '\n') #write to txt file

print("Total Votes : " + str(totline))
print(f"_____________________")
print('\n') #print newline
filewrite.write("Total Votes : " + str(totline) + '\n') #write to txt file
#------------------------------------------

with open(csvpath, newline='') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	next(readcsv, None)  # skip the headers #Skip reading header line
	sortedlist = sorted(readcsv, key=operator.itemgetter(2)) #sort with candidate_name
		# Read the header row first 
	#csv_header = next(readcsv)

	# for eachline in sortedlist:
		# print(eachline)

	for rows in sortedlist:

			if count == 0: # first line
				old_cndt = rows[2] #Get the candidate name

			if old_cndt == rows[2]: #if same candidate count votes
				vote += 1

			if old_cndt != rows[2]: #new candidate found
				#calculate % of vote - (vote/total)* 100
				voteprcnt = (vote/totline) * 100
				voteprcnt = round(voteprcnt, 2)
				print(old_cndt, " : ", str(voteprcnt) + " % " + str(vote))
				writetxt = f"{old_cndt} : {str(voteprcnt)}% {str(vote)}"
				filewrite.write(writetxt + '\n') 
				cantot = vote #Move total votes of a candidate
				candt = old_cndt #Saving the name of future winner
				voteprcnt = 0
				vote = 0
				old_cndt = rows[2] #get the new value
				vote += 1

			if cantot > wintot: #if candidate total > wining tot_change
				wintot = cantot
				winner = candt

			if count == (totline -1): # last row
				voteprcnt = (vote/totline) * 100
				voteprcnt = round(voteprcnt, 2)
				print(rows[2], " : ", str(voteprcnt) + " % " + str(vote))
				writetxt = f"{rows[2]} : {str(voteprcnt)}% {str(vote)}"
				filewrite.write(writetxt + '\n')
				cantot = vote #Move total votes of a candidate
				candt = rows[2] #Saving the name of future winner

			count = count + 1


print('\n')
print(f"_______________"'\n')
print("Winner : " + winner )
print(f"_______________")
writetxt = f"Winner : {winner}"
filewrite.write(writetxt + '\n')

filewrite.close()#close file

#------------------------------------------








