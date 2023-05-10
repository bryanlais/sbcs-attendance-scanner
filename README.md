# SBCS Attendance Scanner

## attendance.py

This Python script `attendance.py` is designed to add attendance data from a CSV file to an existing CSV file with records of attendance. The script takes one command line argument, which is the path to the CSV file containing attendance data. The CSV file must contain three columns named `First Name`, `Last Name`, and `Email`. If any of these columns have different names, the script will fail to execute.

The script reads the attendance data from the CSV file, and checks if each attendee's email address already exists in the attendance records. If an attendee already exists, the script updates their record to reflect that they attended another event. If an attendee does not already exist, the script adds a new record to the attendance records.

The script assumes that the attendance records are stored in a file called `attendancerecords.csv`. The attendance records file must have the following columns, in order:

1. `First Name`
2. `Last Name`
3. `Email`
4. `# of events attended`
5. `Active Member`

The script also assumes that the `# of events attended` column contains integers, and that the `Active Member` column contains either the string `"Yes"` or `"No"`. If the attendance records file has different column names or formats, the script will fail to execute.

## active_members.py

This Python script `active_members.py` is designed to count the number of active members in SBCS based on attendance records stored in a CSV file. The script assumes that the attendance records are stored in a file called `attendancerecords.csv`. The attendance records file must have the following columns, in order:

1. `First Name`
2. `Last Name`
3. `Email`
4. `# of events attended`
5. `Active Member`

The script reads the attendance records from the CSV file, and counts the number of rows where the `Active Member` column contains the string `"Yes"`. The script then prints the number of active members.

If the attendance records file has different column names or formats, the script will fail to execute.
