from sqlalchemy import create_engine
import pandas as pd
import pytest

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
    query_orcl_src = "SELECT * FROM city ORDER BY city_id"
    df_orcl_src = pd.read_sql(query_orcl_src, connect_to_oracle_SRC)
    print("Source data:", df_orcl_src)

    query_mysql_tgt = "SELECT * FROM city ORDER BY city_id"
    df_mysql_tgt = pd.read_sql(query_mysql_tgt, connect_to_mysql_TGT)
    print("Target data:", df_mysql_tgt)

    difference_df = get_differences(df_mysql_tgt, df_orcl_src, 'TestResult_Output/Data_Mismatch.csv')

    if not difference_df.empty:
        print("There are differences in source and target data. They are saved in 'TestResult_Output/database.csv'")

    assert df_orcl_src.equals(df_mysql_tgt), "Source (Oracle) and target (MySQL) data do not match"


def get_differences(df1, df2, output_file):
    differences = pd.concat([df1, df2]).drop_duplicates(keep=False)
    if not differences.empty:
        differences.to_csv(output_file, index=False)
    return differences

if __name__ == "__main__":
    pytest.main()

    
