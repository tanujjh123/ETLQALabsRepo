import pandas as pd
import pytest

# Fixture for the actual data file path
@pytest.fixture()
def csv_file_path():
    # Uncomment the appropriate line for your file path
    # return 'employee.csv'
    # return "C:/Users/hetur/PycharmProjects/ObjectOrientedP/employee.csv"
    return "C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/employees.csv"

# Fixture for the expected data
@pytest.fixture()
def expected_csv_data():
    return pd.DataFrame({
        'Name': ['John Doe', 'Anna Smith', 'Peter Jones'],
        'Age': [30, 27, 45],
        'Department': ['Sales', 'Marketing', 'HR']
    })

def test_csv_extraction(csv_file_path, expected_csv_data):
    # Read data from the CSV file
    data = pd.read_csv(csv_file_path)

    # Print data for debugging
    print("Actual Data from CSV:\n", data)
    print("Expected Data:\n", expected_csv_data)

    # Assert if the dataframes are equal
    assert data.equals(expected_csv_data), "Data extraction failed"

if __name__ == "__main__":
    pytest.main()
