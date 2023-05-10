import csv

# open the CSV file and create a csv reader object
with open("attendancerecords.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)

    # initialize a counter for the rows with the specified value
    active_members = 0

    # loop through each row in the CSV file
    for row in reader:
        # check if the specified value is in the specified column of the current row
        if row[4] == "Yes":
            active_members += 1

    # print the count of rows with the specified value
    print(f'There are {active_members} active members in SBCS.')
