from sqlalchemy import create_engine, MetaData, Table, select
import pandas as pd

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData(bind=self.engine)

    def fetch_data(self, table_name):
        table = Table(table_name, self.metadata, autoload=True, autoload_with=self.engine)
        return pd.read_sql(select([table]), self.engine)
