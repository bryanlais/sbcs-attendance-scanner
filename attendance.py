import csv
import sys

def index_of_col_names(new_file):
    with open(new_file, 'r') as file:
        csv_reader = csv.reader(file)
        header_row = next(csv_reader)
        column_indexes = []
        for column_name in ['First Name', 'Last Name', 'Email']:
            if column_name in header_row:
                column_indexes.append(header_row.index(column_name))
            else:
                column_indexes.append(None)
    return column_indexes

#Returns either False or [row_idx, row_values]
def member_exists(email):
    with open("attendancerecords.csv", "r") as file:
        csv_reader = csv.reader(file)
        row_idx = 0
        for row in csv_reader:
            if(row[2] == email):
                return [row_idx, row]
            row_idx += 1
        return False

def edit_csv_row(row_index, new_row_values):
    with open("attendancerecords.csv", 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    # Update the row values
    rows[row_index] = new_row_values

    # Write the updated rows back to the CSV file
    with open("attendancerecords.csv", 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)

def add_to_attendance_csv(new_file):
    #Some attendance forms may have first name, last name and email at different indices. 
    fn_idx, ln_idx, email_idx = index_of_col_names(new_file)
    with open(new_file, 'r') as source, open("attendancerecords.csv", 'a', newline='') as target:
        source_reader = csv.reader(source)
        attendance_writer = csv.writer(target)
        next(source_reader)
        #Checks to see if a new entry is present
        new_entry = False
        for row in source_reader:
            #Check to see if this row already exists by checking email.
            #row_two_vals --> 0 OR [row_idx, row_to_be_updated]
            row_two_vals = member_exists(row[email_idx])
            if(row_two_vals):
                row_idx, row_to_be_updated = row_two_vals
                #Increase the # of events for the updated row by 1.
                num_of_events = int(row_to_be_updated[3])
                num_of_events += 1
                row_to_be_updated[3] = str(num_of_events)
                #Check to see if the # of events attended is greater than 2 - if so, then they are an active member. 
                if(num_of_events >= 2):
                    row_to_be_updated[4] = "Yes"
                edit_csv_row(row_idx, row_to_be_updated)
            #Add new entry to attendance.
            else:
                new_entry = [row[fn_idx], row[ln_idx], row[email_idx], 1, "No"]
                attendance_writer.writerow(new_entry)

args = sys.argv
if(len(args) < 2):
    print("Correct Usage: python attendance.py <csv-file> ")
else:
    event_name = args[1][7:-4]
    add_to_attendance_csv(args[1])
    print("Completed attendance submission of: " + event_name)


