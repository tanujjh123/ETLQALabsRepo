import json

# Specify the file name
filename = 'employees.json'

# Reading JSON data from the file
with open(filename, 'r') as json_file:
    data = json.load(json_file)

# Print the data
print(json.dumps(data, indent=4))
