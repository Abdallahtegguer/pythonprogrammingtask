import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from database import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    @patch('database.create_engine')
    def test_init(self, mock_engine):
        # Test successful initialization
        db_url = 'sqlite:///my_data.db'
        manager = DatabaseManager(db_url)
        mock_engine.assert_called_once_with(db_url)

    @patch('database.create_engine')
    def test_init_fail(self, mock_engine):
        # Test initialization failure
        mock_engine.side_effect = SQLAlchemyError("Connection failed")
        with self.assertRaises(SQLAlchemyError):
            manager = DatabaseManager('invalid_db_url')

    @patch('database.pd.read_sql')
    @patch('database.Table')
    @patch('database.select')
    def test_fetch_data(self, mock_select, mock_table, mock_read_sql):
        # Setup
        mock_engine = MagicMock()
        manager = DatabaseManager('sqlite:///my_data.db')
        manager.engine = mock_engine

        # Mocks
        mock_table.return_value = MagicMock()
        mock_read_sql.return_value = pd.DataFrame()

        # Test fetch_data
        result = manager.fetch_data('test_table')
        assert isinstance(result, pd.DataFrame)

        # Check if exceptions are raised appropriately
        mock_read_sql.side_effect = SQLAlchemyError("Query failed")
        with self.assertRaises(SQLAlchemyError):
            result = manager.fetch_data('test_table')

if __name__ == '__main__':
    unittest.main()
