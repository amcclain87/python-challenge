#import csv library
import csv

#open the csv file
with open("/Users/austin2/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv","r") as election_info:
    info = csv.reader(election_info,delimiter = ",")
    #csv header
    header = next(election_info)
    
    
    #create new lists
    num_votes = []
    candidates = []
    cand_unique = []
    
    #add each row into defined lists to call back in calculations
    for data in info:
        num_votes.append(data[0])
        candidates.append(data[2])
        
    
#calculations
    #total votes
    total_votes = len(num_votes)
    #for loop for candidates who received votes
    for unique in candidates:
        #count the candidate in row, if the count is 0 then add to the cand_unique list
        if cand_unique.count(unique) == 0:
            cand_unique.append(unique)
    #votes per candidate
    votes_1 = candidates.count(cand_unique[0])
    votes_2 = candidates.count(cand_unique[1])
    votes_3 = candidates.count(cand_unique[2])
    
    #percentages of votes per candidate
    percent_1 = votes_1 / total_votes
    percent_2 = votes_2 / total_votes
    percent_3 = votes_3 / total_votes
    
    #winner
    #if statement if the first candidate has more votes than both candidate two and three
    if votes_1 > votes_2 and votes_3:
        winner = cand_unique[0]
    #else if statement if candidate two has the most votes
    elif votes_2 > votes_3 and votes_3:
        winner = cand_unique[1]
    #else candidate 3 has the most votes
    else:
        winner = cand_unique[2]
    
    
    
    #final print
    print("Election Results")
    print("-------------------------")
    print("Total Votes:",total_votes)
    print("-------------------------")
    print(cand_unique[0], f"{percent_1:.3%}","(" + str(votes_1) + ")")
    print(cand_unique[1], f"{percent_2:.3%}","(" + str(votes_2) + ")")
    print(cand_unique[2], f"{percent_3:.3%}","(" + str(votes_3) + ")")
    print("-------------------------")
    print(winner)
    print("-------------------------")


# In[40]:


# write to a file with the analysis
f = open("/Users/austin2/Documents/GitHub/python-challenge/PyPoll/analysis/election_analysis.txt","w")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")
f.write(cand_unique[0] + ": " + f"{percent_1:.3%}" + " (" + str(votes_1) + ")\n")
f.write(cand_unique[1] + ": " + f"{percent_2:.3%}" + " (" + str(votes_2) + ")\n")
f.write(cand_unique[2] + ": " + f"{percent_3:.3%}" + " (" + str(votes_3) + ")\n")
f.write("-------------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-------------------------\n")
f.close()





