# Modules
import os
import csv

# Set starter variables
Months = []
tChange = []
plChange = 0
currentVal = 0

# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(csvpath, encoding='utf=8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)

    #reading first row and setting current variables
    first_row = next(csvreader)
    currentVal = int(first_row[1])
    pl = int(first_row[1])
    
    # Loop through all the rows to find the info
    for row in csvreader:
        
        # Fill in Months list, add 1 for the first row that was taken out
        Months.append(row[0])
        Total_Months = len(Months) + 1

        # Add profit/loss values over entire time period
        pl += int(row[1])

        # Calculate change in Profits, add to list, set currentVal to the next line
        plChange= int(row[1])-currentVal
        tChange.append(plChange)
        currentVal = int(row[1])

        # Average change in profit/losses from month to month
        avgChange = sum(tChange)/len(tChange)

        # Greatest Increase in Profits
        increase = max(tChange)
        inc_index = tChange.index(increase)
        inc_date = Months[inc_index]

        # Greatest Decrease in Profits
        decrease = min(tChange)
        dec_index = tChange.index(decrease)
        dec_date = Months[dec_index]

    # Printing results
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total Profit/Losses: ${pl:,}")
    print(f"Average Change in Profit/Losses: ${round(avgChange,2):,}")
    print(f"Greatest Increase in Profits: {inc_date} (${increase:,})")
    print(f"Greatest Decrease in Profits: {dec_date} (${decrease:,})")

# Exporting results to a txt file
output_file = os.path.join("results.txt")

with open(output_file, 'w', newline='') as file:
    text = csv.writer(file)
    text.writerow(["Financial Analysis"])
    text.writerow(["----------------------------------------------------------"])
    text.writerow(["Total Months: " + str(Total_Months)])
    text.writerow(["Total Profit/Losses: $" + str(pl)])
    text.writerow(["Average Change in Profit/Losses: $" + str(round(avgChange,2))])
    text.writerow(["Greatest Increase in Profits: " + str(inc_date) + " ($" + str(increase) + ")"])
    text.writerow(["Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(decrease) + ")"])