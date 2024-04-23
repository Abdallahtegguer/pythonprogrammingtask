import unittest
from unittest.mock import MagicMock
from pandas import DataFrame
import numpy as np
from analysis import DataAnalysis

class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        # Setup with a mock db_manager
        self.db_manager = MagicMock()
        self.analysis = DataAnalysis(self.db_manager)

    def test_map_test_data(self):
        # Mock data setup
        test_data = DataFrame({
            'x': [1, 2, 3],
            'y': [10, 20, 30]
        })
        ideal_functions = DataFrame({
            'x': [1, 2, 3],
            'y48': [9, 19, 29],
            'y49': [11, 21, 31]
        })
        best_functions = ['y48', 'y49']
        max_deviations = {'y48': 1.5, 'y49': 1.5}

        # Expected results
        expected_results = [
            (1, 10, 'y48', 1),  # Example result: x, y, func, deviation
            (2, 20, 'y48', 0),
            (3, 30, 'y49', 1)
        ]

        # Execute
        results = self.analysis.map_test_data(test_data, ideal_functions, best_functions, max_deviations)

        # Validate
        self.assertEqual(results, expected_results)

    def test_map_test_data_no_match(self):
        # Data setup where no matches should occur
        test_data = DataFrame({
            'x': [1, 2, 3],
            'y': [10, 20, 30]
        })
        ideal_functions = DataFrame({
            'x': [1, 2, 3],
            'y48': [50, 60, 70]  # Large deviation values
        })
        best_functions = ['y48']
        max_deviations = {'y48': 1.0}  # Small max deviation not allowing any matches

        # Expected: all results marked as 'None'
        expected_results = [
            (1, 10, 'None', None),
            (2, 20, 'None', None),
            (3, 30, 'None', None)
        ]

        # Execute
        results = self.analysis.map_test_data(test_data, ideal_functions, best_functions, max_deviations)

        # Validate
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()
