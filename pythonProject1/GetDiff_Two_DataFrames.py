import pandas as pd


def get_differences(df1, df2, output_file=None):
    # Find differences by concatenating the two DataFrames and keeping only the unique rows
    differences = pd.concat([df1, df2]).drop_duplicates(keep=False)

    # Optionally save the differences to a CSV file
    if output_file:
        differences.to_csv(output_file, index=False)

    return differences


# Example usage
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [1, 2, 6]
})

df2 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [8, 9, 10]
})

differences = get_differences(df1, df2)
print("Differences:")
print(differences)
