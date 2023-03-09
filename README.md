# python-challenge
I completed both PyBank and PyPoll challenge using the csv libraries to read the csv files

For PyBank:
I created two main lists to work off of for calculations: num_months and profit_months. I added to the list using a for loop to go through all the rows of data in the csv.
  -num_months: added a item in the list for each month represented on the csv. Total_month is then calculated using the length function
  -profit_months: adds the profits made/loss each month into a list. For the average change, I was able to pull the first month using pofit_months[0] and the last month using profit_months. First_month is then subtracted from last_month and then divided by Total_month.
  -A counter (total_profit) were set to all of the profits made each month
  -and the greatest_in and greatest_de were made as counters and set to 0. In the for loop, each profit was compared to the counter. If the profit was greater tthan greatest_in, then greatest_in was set as that month's profit. The same was done for greatest_de, but the comparision was for if it was lower.

The information needed to be printed to the terminal using a series of print functions, and the dollars needed to be formated for currency.
And the information needed to be added to a .txt file. The destination was set using with with open function and set to "w". This allows for the file to be created if there is no file present, or for the file to be rewritten.
  -.write was used instead of print, and all the numbers needed to be converted to stings
  -to get the next line to make the data readable "\n" had to be used for a line break.
  
For PyPoll
I opened the csv file again with the with open function
-i then created lists that I would store the necessary data for calculations in (num_votes, condidates, and cand_unique)
-I then ran a for loop to go through each row of data in the csv and added the number of votes into the num_votes list and used the length function to calculate total number of votes. I also added the candidate indicated on each row to the list candidates.
-To get the unique candidates, I ran a for loop on the list "candidates", and ran a count of each item in "candidates". If the count was 0 then the cadidate was added. Otherwise the script when to the next row of data
-To get the number of votes per candidate, I ran a count of how many times each candidate appeared in the list "candidates" and stored the count in a variable.
-I then calculated the vote percentage by dividing the count of votes for each candidate by the total vote
-An if statement with an and statement was used to compare the vote for each candidate to see if they were greater than the other two candidates.

I then printed to the terminal and set a destination for a .txt file with the with open function set to "w". I used the .write function again instead of print and converted all the integers to strings.
