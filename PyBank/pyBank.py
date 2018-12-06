#Election.python-challenge/PyBank
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
#set file path
csvpath = os.path.join("..", "/Users/sghosh/Documents/Suv/Personal/Berkeley/python-challenge/PyBank", "budget_data.csv")



total = 0
tot_change = 0
prev_amt = 0
count = 0
max_change = 0
min_change = 0
avg_change = 0
max_change_month = " "
min_change_month = " "
change = 0
PL_list = []

#get the list od rows in the csv file
file = open(csvpath)
numline = len(file.readlines())
#print("Number of rows in the file = " + str(numline))


with open(csvpath, newline='') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	next(readcsv, None)  # skip the headers #Skip reading header line


	for rows in readcsv:
			total = total + int(rows[1]) #total profit or loss

			if count == 0:
				prev_amt = int(rows[1])
				#tot_change = rows[1] #save the month P/L
			
			if count > 0: 
				change = int(rows[1]) - int(prev_amt)
				tot_change += change
				#PL_list.append(tot_change) #save in list
			
			if int(tot_change) > int(max_change): #Calc monthly change in P/L
				max_change = tot_change
				max_change_month = rows[0]
			elif tot_change < min_change:
				min_change = tot_change
				min_change_month = rows[0]
				
			
			count = count + 1
			prev_amt = rows[1]

#calc average change 
avg_change = tot_change/(count -1)
avg_change = round(avg_change, 2)

#print details
print("Total Months : " + str(count))
print("Total : $ " +  str(total))
print("Average Change : $ " + str(avg_change))
print("Greatest Increase in Profits : " + max_change_month + "  $ " +  str(max_change))
print("Greatest Decrease in Profits : " + min_change_month + " $ " +  str(min_change))








