#needed modules
import os
import csv


#Empty List:
profit=0
num_month=0
profit_list=[]
profit_change_list = []
month_list=[]


csvpath=os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #removes header for consideration
    header = next(csvreader)
    
    for row in csvreader:
        #Month count
        num_month = num_month + 1
        #Total profit
        profit = profit + int(row[1])

        #fill empty list
        profit_list.append(int(row[1]))
        month_list.append(row[0])

    #calculate the change ex. row 2-row 1 through range and add to new list
    for x in range(len(profit_list)-1):
        profit_change_list.append(profit_list[x+1]-profit_list[x])

        #find max and min of list
        increase_change = max(profit_change_list)
        decrease_change = min(profit_change_list)

        #find location of max and min
        increase_change_loc= profit_change_list.index(max(profit_change_list))+1
        decrease_change_loc= profit_change_list.index(min(profit_change_list))+1

    #Print results
    print("Financial Analysis")
    print("-------------------")
    print(f'Total Months: {num_month}')
    print(f"Total: ${profit}")
    print(f'Average Change: ${sum(profit_change_list)/(len(profit_change_list))}')
    print(f'Greatest Increase in Profits: {month_list[increase_change_loc]} ${increase_change}')
    print(f'Greatest Decrease in Profits: {month_list[decrease_change_loc]} ${decrease_change}')


    #output results
    output_file = os.path.join("..","PyBank","analysis","Financial_Analysis.Txt")

with open(output_file,'w') as file:
    file.write("Financial Analysis")
    file.write("-------------------")
    file.write(f'Total Months: {num_month}')
    file.write(f"Total: ${profit}")
    file.write(f'Average Change: ${sum(profit_change_list)/(len(profit_change_list))}')
    file.write(f'Greatest Increase in Profits: {month_list[increase_change_loc]} ${increase_change}')
    file.write(f'Greatest Decrease in Profits: {month_list[decrease_change_loc]} ${decrease_change}')


    

    