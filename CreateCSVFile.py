import csv

# Data to be written to CSV file
data = [
    ["Name", "Age", "Department"],
    ["John Doe", 30, "Sales"],
    ["Anna Smith", 27, "Marketing"],
    ["Peter Jones", 45, "HR"],
    ["Peter Jones", 45, "HR"]
]

# Specify the file name
filename = 'emp.csv'

# Writing data to a CSV file
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header
    csvwriter.writerow(data[0])

    # Write the data rows
    csvwriter.writerows(data[1:])
