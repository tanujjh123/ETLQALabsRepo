from sqlalchemy import create_engine
import cx_Oracle
import pandas as pd
import pytest

@pytest.fixture
def connect_oracle_db_SRC():
    engine = create_engine('oracle+cx_oracle://sys:admin@localhost:1521/?service_name=XE&mode=SYSDBA')
    connection_orcl = engine.connect()
    yield connection_orcl
    connection_orcl.close()

@pytest.fixture
def connect_mysql_db_STG():
    engine = create_engine('mysql+pymysql://root:Omnitech%407329@localhost:3306/student')
    connection_mysql = engine.connect()
    yield connection_mysql
    connection_mysql.close()

def test_row_counts_consistency(connect_oracle_db_SRC,connect_mysql_db_STG):
    query_orcl = 'SELECT COUNT(*) AS count FROM dept'
    query_mysql = 'SELECT COUNT(*) AS count FROM  dept'
    count_orcl = pd.read_sql(query_orcl, connect_oracle_db_SRC).iloc[0, 0]
    count_mysql = pd.read_sql(query_mysql, connect_mysql_db_STG).iloc[0, 0]
    print("\nRow count from Oracle Source: ", count_orcl)
    print("\nRow count from MYSQL Target: ", count_mysql)
    assert count_orcl == count_mysql, f"Row count mismatch: Oracle has"


