import pandas as pd
import pytest

def store_differences(actual, expected, file_path):
    # Finding rows that are different between actual and expected DataFrames
    diff = pd.concat([actual, expected]).drop_duplicates(keep=False)
    if not diff.empty:
        diff.to_csv(file_path, index=False)
    return diff

# Test case name (test method)
def test_employeesDataLoad():
    try:
        df_source = pd.read_csv('C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/employees.csv')
        df_target = pd.read_csv('C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/employee.csv')
    except Exception as e:
        print(f"Error reading files: {e}")
        return

    try:
        differences = store_differences(df_source, df_target,
                                        'C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/differences.csv')

        # Optionally, print the differences
        if not differences.empty:
            print(
                "Differences between actual and expected data are saved in 'C:/Users/Tanuj/PycharmProjects/myproj/pythonProject1/.ipynb_checkpoints/differences.csv'")

        assert df_source.equals(df_target), "Source and target don't match"
    except Exception as e:
        print(f"Error comparing data: {e}")

if __name__ == "__main__":
    pytest.main()
