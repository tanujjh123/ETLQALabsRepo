import pandas as pd
import pytest
# for connecting mysql database
from sqlalchemy import create_engine
# for connecting oracle database
import cx_Oracle

@pytest.fixture()
def connect_to_oracle_SRC():
    engine = create_engine("oracle+cx_oracle://system:admin@localhost:1521/?service_name=XE&mode=SYSDBA")
    connection_oracle = engine.connect()
    yield connection_oracle
    connection_oracle.close()

def test_dataExtractionCheckInDatabase(connect_to_oracle_SRC):
    query_orcl_src = 'SELECT city_id,name FROM CITY'
    df_orcl_src = pd.read_sql(query_orcl_src,connect_to_oracle_SRC)
    expected_datatypes = {'city_id':'int64','name':'O'}

    #print(df_orcl_src.dtypes)
    assert df_orcl_src.dtypes.to_dict() == expected_datatypes," dataYpes not matching with expected"
