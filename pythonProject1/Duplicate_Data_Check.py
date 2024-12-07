import pandas as pd

# Load the CSV file
filename = 'C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/emp.csv'
df = pd.read_csv(filename)
# Check for duplicate rows
duplicates = df[df.duplicated()]
# Print duplicates
print("Duplicate rows:")
print(duplicates)
# Save the duplicate records to a separate CSV file
duplicates.to_csv('C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/duplicates.csv', index=False)
# Optionally, print a message if no duplicates are found
if duplicates.empty:
    print("No duplicate records found.")
else:
    print(f"Duplicate records saved to 'duplicates.csv'")


