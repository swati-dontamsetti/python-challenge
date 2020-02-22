# Modules
import os
import csv

# Set starter variables
count = 0
candidates = []
unique_candidates = []
kvotes = []
cvotes = []
lvotes = []
ovotes = []

# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

# Open and read csv
with open(csvpath, encoding='utf=8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)

    # Loop through all the rows to find the info
    for row in csvreader:
        
        # Count number of rows
        count += 1

        # Fill in all candidates voted for
        candidates.append(row[2])
        
        # Create a set from the candidates to get the unique candidate names
        for x in candidates:
            if x not in unique_candidates:
                unique_candidates.append(x)
                # print(x) <- initially I printed this so I would know who the unique candidate were for the next part

        # Find how many vote for Khan
        for v in candidates:
            if v == "Khan":
                kvotes.append(v)
            elif v == "Correy":
                cvotes.append(v)
            elif v == "Li":
                lvotes.append(v)
            elif v == "O'Tooley":
                ovotes.append(v)
        
        # Percentages of each candidate
        kpercent = round((len(kvotes))/count,3)
        cpercent = round((len(cvotes))/count,3)
        lpercent = round((len(lvotes))/count,3)
        opercent = round((len(ovotes))/count,3)

        # Identify the winner
        if int(kpercent) > int(cpercent) & int(kpercent) > int(lpercent) & int(kpercent) > int(opercent):
            winner = unique_candidates[0]
        elif int(cpercent) > int(kpercent) & int(cpercent) > int(lpercent) & int(cpercent) > int(opercent):
            winner = unique_candidates[1]
        elif int(lpercent) > int(kpercent) & int(lpercent) > int(cpercent) & int(lpercent) > int(opercent):
            winner = unique_candidates[2]
        elif int(opercent) > int(kpercent) & int(opercent) > int(cpercent) & int(opercent) > int(lpercent):
            winner = unique_candidates[3]

# Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {count:,}")
print("-------------------------")
print(f"{unique_candidates[0]}: {kpercent}% ({len(kvotes)})")
print(f"{unique_candidates[1]}: {cpercent}% ({len(cvotes)})")
print(f"{unique_candidates[2]}: {lpercent}% ({len(lvotes)})")
print(f"{unique_candidates[3]}: {opercent}% ({len(ovotes)})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")