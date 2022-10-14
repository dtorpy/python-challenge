import os
import csv

#path of csv
csvpath=os.path.join('Resources','election_data.csv')

#veriable
total_votes=0
stockham=0
DeGette=0
Doane=0

#Blank list
canidate_list=[]
unique_canidate=[]
votes=[]
Canidate_dictionary={}



#fill list with respective columns

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #removes header for consideration
    header = next(csvreader)
    #loop through rows
    for row in csvreader:
        #add total votes for each row
        total_votes= total_votes+1
        #fill canidate list
        canidate_list.append(row[2])
        #loop through canidates and add votes
        if row[2]=="Charles Casper Stockham":
            stockham=stockham+1
        elif row[2]=="Diana DeGette":
            DeGette=DeGette+1
        elif row[2]=="Raymon Anthony Doane":
            Doane=Doane+1
        #appened canidates votes to a list
        votes.append(stockham)
        votes.append(DeGette)
        votes.append(Doane)

    #create a dictinary of key values
    Canidate_dictionary["Charles Casper Stockham"]=stockham
    Canidate_dictionary["Diana DeGette"]=DeGette
    Canidate_dictionary["Raymon Anthony Doane"]=Doane
    
    winner=max(Canidate_dictionary, key=Canidate_dictionary.get)    

        
    for canidate in canidate_list:
        if canidate not in unique_canidate:
            unique_canidate.append(canidate)

        


#votes cast
print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("----------------")
print(f"{unique_canidate[0]} {round(float((stockham/total_votes)*100),2)}% ({stockham})")
print(f"{unique_canidate[1]} {round(float((DeGette/total_votes)*100),2)}% ({DeGette})")
print(f"{unique_canidate[2]} {round(float((Doane/total_votes)*100),2)}% ({Doane})")
print("----------------")
print(f"Winner: {winner}")
print("----------------")
#print(f'Winner: {unique_canidate[winner_index]}')


#output results
output_file = os.path.join("..","PyPoll","analysis","Election.Txt")

with open(output_file,'w') as file:
    file.write("Election Results")
    file.write("----------------")
    file.write(f"Total Votes: {total_votes}")
    file.write("----------------")
    file.write(f"{unique_canidate[0]} {round(float((stockham/total_votes)*100),2)}% ({stockham})")
    file.write(f"{unique_canidate[1]} {round(float((DeGette/total_votes)*100),2)}% ({DeGette})")
    file.write(f"{unique_canidate[2]} {round(float((Doane/total_votes)*100),2)}% ({Doane})")
    file.write("----------------")
    file.write(f"Winner: {winner}")
    file.write("----------------")
    
