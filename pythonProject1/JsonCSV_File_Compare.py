import pandas as pd
import pytest
import os
@pytest.fixture()
def json_file_path():
    return "C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/employees.json"
@pytest.fixture()
def csv_file_path():
    return "C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/employees.csv"
@pytest.fixture()
def error_csv_path():
    return "C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/errors.csv"
def test_json_extract_Validation(json_file_path, csv_file_path, error_csv_path):
    # Read the JSON file and normalize the nested data
    df_src_json = pd.read_json(json_file_path)
    df_src_json = pd.json_normalize(df_src_json['employees'])
    print("Source JSON data:")
    print(df_src_json)

    # Read the CSV file
    df_tgt_csv = pd.read_csv(csv_file_path)
    print("Target CSV data:")
    print(df_tgt_csv)

    # Find differences
    differences = pd.concat([df_src_json, df_tgt_csv]).drop_duplicates(keep=False)

    # Save differences to error CSV if there are any
    if not differences.empty:
        save_errors(differences, error_csv_path)
        print(f"Differences found and saved to '{error_csv_path}'")

    assert df_src_json.equals(df_tgt_csv), "JSON extraction failed - Data mismatch"


def save_errors(differences, error_csv_path):
    # Ensure the directory exists
    directory = os.path.dirname(error_csv_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the differences to the error CSV file
    differences.to_csv(error_csv_path, index=False)


if __name__ == "__main__":
    pytest.main()
