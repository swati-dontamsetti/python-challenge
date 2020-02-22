# Modules
import os
import csv

# Create path
csvpath = os.path.join("employee_data.csv")

# Set empty lists
emp_id = []
name = []
dob = []
ssn = []
state = []
first_name = []
last_name = []
new_date = []
new_ssn = []
abbs = []

# Create dictionary of State and ABBs
state_abbs = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY'
            }

with open(csvpath, encoding='utf=8') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Identify the header
    csvheader = next(csvreader)

    # Loop through the rows and append the empty lists
    for row in csvreader:
        emp_id.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(state_abbs[row[4]])
        
        # Split Names and identify first and last name
        first_last = row[1].split(" ")
        first_name.append(first_last[0])
        last_name.append(first_last[1])

        # Convert Date
        date = row[2].split("-")
        new_date.append(f"{date[1]}/{date[2]}/{date[0]}")

        # Convert SSN
        old_ssn = row[3].split("-")
        new_ssn.append(f"***-**-{old_ssn[2]}")

#zip lists together into a tuple
final_data = zip(emp_id,first_name,last_name,new_date,new_ssn,state)

#set variable for output file
output_file = os.path.join("employee_final.csv")

#open the output file
with open(output_file, "w") as datafile:
    writer =csv.writer(datafile)

    #write the headers
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    #write in the zipped rows
    writer.writerows(final_data)
