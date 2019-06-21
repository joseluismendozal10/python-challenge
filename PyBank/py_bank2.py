import os
import csv
import textwrap


# Path to collect data from the Resources folder
csvpath = os.path.join("Py_Bank.csv")
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # for row in csvreader:
    #     print (row[1])
    
    next(csvreader, None) # Skip first row

    months=0 # define variable for counting months
    profits=0 # define variable for adding profits
    profits_list = []
    months_list=[]
    for row in csvreader:
        months += 1 # The total number of months included in the dataset
        profits_list.append(row[1]) # List of profits/losses
        profits=profits+int(row[1]) # Total profits
        months_list.append(row[0]) # List of months
 
print("Financial Analysis \n---------------------")
print ("Total months: " + str(months))              
print("total profits: $"+ str(profits))
# for x in range(len(months_list)): 
#     print (months_list[x]) 

#Create a dictionary with months and profits

dict_profits = dict(zip(months_list, profits_list))
#print(dict_profits)


# The average of the changes in "Profit/Losses" over the entire period

change_list=[0]
change=0
for i in range(len(profits_list)-1):
    change=int(profits_list[i+1])-int(profits_list[i])
    change_list.append(change)

change_list_mnth=[]
change=0
for i in range(len(profits_list)-1):
    change=int(profits_list[i+1])-int(profits_list[i])
    change_list.append(change)

# for x in range(len(change_list)): 
#     print (change_list[x])
            
change_average=sum(change_list)/len(change_list) 

print("Average change: $" +str(round(change_average, 2)))

# # The greatest increase in profits (date and amount) over the entire period

change_greatest=0
change_lowest=0

for i in range(len(change_list)-1):
    if change_list[i] > change_greatest :
        change_greatest=change_list[i]
    if change_list[i] < change_lowest :
        change_lowest=change_list[i]

dict_change = dict(zip(months_list, change_list))

for month, profchan in dict_change.items(): 
    if profchan==change_greatest:
        print("Greatest Increase in Profits: " + month + ", ($" + str(change_greatest) +")" )
    if profchan==change_lowest:
        print("Greatest Decrease in Profits: " + month + ", ($" + str(change_lowest) +")" ) 
        

