from sqlalchemy import create_engine
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

@pytest.fixture()
def connect_to_oracle_SRC():
    engine = create_engine('oracle+cx_oracle://sys:admin@localhost:1521/?service_name=XE&mode=SYSDBA')
    connection_oracle = engine.connect()
    yield connection_oracle
    connection_oracle.close()

@pytest.fixture()
def connect_to_mysql_TGT():
    engine = create_engine('mysql+pymysql://root:Omnitech%407329@localhost:3306/student')
    connection_mysql = engine.connect()
    yield connection_mysql
    connection_mysql.close()

@pytest.mark.smoke
def test_dataExtractionFromOracleToLoadIntoMYSQL(connect_to_oracle_SRC, connect_to_mysql_TGT):
    query_orcl_src = "SELECT QUANTITY FROM SALES WHERE CUSTOMER_ID='1001'"
    df_orcl_src = pd.read_sql(query_orcl_src, connect_to_oracle_SRC)
    print("Source data from Oracle:", df_orcl_src)
    print("Oracle data types:\n", df_orcl_src.dtypes)

    if df_orcl_src.empty:
        print("No data found for CUSTOMER_ID='1001' in Oracle database.")
    else:
        query_mysql_tgt = "SELECT CAST(ROUND(quantity/10, 0) AS SIGNED) AS QUANTITY FROM sales WHERE CUSTOMER_ID=1001"
        df_mysql_tgt = pd.read_sql(query_mysql_tgt, connect_to_mysql_TGT)
        print("Target data from MySQL:", df_mysql_tgt)
        print("MySQL data types:\n", df_mysql_tgt.dtypes)

        if df_mysql_tgt.empty:
            print("No data found for CUSTOMER_ID=1001 in MySQL database.")
        else:
            # Standardize column names
            df_orcl_src.columns = df_orcl_src.columns.str.upper()
            df_mysql_tgt.columns = df_mysql_tgt.columns.str.upper()

            # Reset indices before comparison
            df_orcl_src = df_orcl_src.reset_index(drop=True)
            df_mysql_tgt = df_mysql_tgt.reset_index(drop=True)

            # Use assert_frame_equal for better comparison
            try:
                assert_frame_equal(df_orcl_src, df_mysql_tgt, check_dtype=False)
                print("Source (Oracle) and target (MySQL) data match.")
            except AssertionError as e:
                print("Source (Oracle) and target (MySQL) data do not match.")
                difference_df = get_differences(df_mysql_tgt, df_orcl_src, 'TestResult_Output/Data_Mismatch.csv')
                if not difference_df.empty:
                    print(
                        "There are differences in source and target data. They are saved in 'TestResult_Output/Data_Mismatch.csv'")
                raise e


def get_differences(df1, df2, output_file):
    differences = pd.concat([df1, df2]).drop_duplicates(keep=False)
    if not differences.empty:
        differences.to_csv(output_file, index=False)
    return differences


if __name__ == "__main__":
    pytest.main()
