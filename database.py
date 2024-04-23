from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

class DatabaseManager:

    #first we create an engine
    def __init__(self, db_url):
        try:
            self.engine = create_engine(db_url)
            self.metadata = MetaData(bind=self.engine)
        except SQLAlchemyError as e:
            print(f"Database connection failed: {e}")
            raise
    # here we fetch the data from the table in question from the database       
    def fetch_data(self, table_name):
        try:
            table = Table(table_name, self.metadata, autoload=True, autoload_with=self.engine)
            return pd.read_sql(select([table]), self.engine)
        except SQLAlchemyError as e:
            print(f"Failed to fetch data from {table_name}: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise
