#!/usr/bin/env python
# coding: utf-8

# In[29]:


#import csv library
import csv

#open csv file
with open("/Users/austin2/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv","r") as bankinfo:
    #csv reader
    info = csv.reader(bankinfo,delimiter = ",")
    #csv header
    header = next(info)

    #set months list
    num_months = []
    #set list for profit for each month
    profit_month = []
    #start calculation of total profit at 0
    total_profit = 0
    #start comparision for greatest increase at 0 and look for next largest number
    greatest_in = 0
    #start comparision for greatest decrease at 0 and look for the next lowest number
    greatest_de = 0
    
    #for loop that runs through csv data
    for data in info:
        #add each month into the num_months list to calculate total months
        num_months.append(data[0])
        #add profit made each month to the profit_month list in order to pull the first and last profits to caluculate average change
        profit_month.append(data[1])
        #add each month's profit to total_profit
        total_profit = total_profit + int(data[1])
        #if statement to determine month with the greatest increase
        if int(data[1]) > greatest_in:
            #if the profit is greater then greatest_in, then set the profit at greatest_in, and that month as the greatest_month
            greatest_in = int(data[1])
            greatest_month = data[0]
        #if statement to determine month with the greatest decrease
        if int(data[1]) < greatest_de:
            #if the profit is lower than greatest_de, then set the profit at greatest_de, and that month as the lowest_month
            greatest_de = int(data[1])
            lowest_month = data[0]
        
    
    #calculate the total number of months in the list using the length function
    total_months = (len(num_months))
    #calculate the profit from the first month of the csv
    first_month = profit_month[0]
    #calculate the profit from the last month of the csv
    last_month = profit_month[total_months-1]
    #calculate the average profit
    av_profit = (int(last_month) - int(first_month))/total_months
    
    #formating how analysis is printed
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months:",total_months)
    print("Total:","${:,}".format(int(total_profit)))
    print("Average Change:","${:,.6}".format(av_profit))
    print("Greatest Increase in Profits:",greatest_month,"(" + str("${:,}".format(greatest_in)) + ")")
    print("Greatest Decrease in Profits:",lowest_month,"(" + str("${:,}".format(greatest_de)) + ")")
    
        


# In[30]:


# write to a file with the analysis

#this function either creates a new file if one doesn't exist or rewrites a file at this destination
f = open("/Users/austin2/Documents/GitHub/python-challenge/PyBank/analysis/profit_analysis.txt","w")
#formating the printing with dollar signs and commas for currency
f.write("Financial Analysis\n")
f.write("-----------------------------\n")
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: " + str("${:,}".format(total_profit)) + "\n")
f.write("Average Change:" + str("${:,.6}".format(av_profit)) + "\n")
f.write("Greatest Increase in Profits: " + str(greatest_month) + " (" + str("${:,}".format(greatest_in)) + ")\n")
f.write("Greatest Decrease in Profits: " + str(lowest_month) + " (" + str("${:,}".format(greatest_de)) + ")\n")
#closes the file that was just writen
f.close()


    

