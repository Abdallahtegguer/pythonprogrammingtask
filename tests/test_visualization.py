import unittest
from visualization import Visualizer
from unittest.mock import patch, MagicMock

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        self.visualizer = Visualizer()

    @patch('visualization.show')  # Mock the show function to not actually plot during tests
    def test_plot_data(self, mock_show):
        mapping_results = [
            (1, 10, 'y48', 1, 'green'),
            (2, 20, 'None', None, 'red')
        ]
        self.visualizer.plot_data(mapping_results, "Test Data Mapping Results")
        mock_show.assert_called_once()  # Ensure the show function was called

    # More tests can be added here

if __name__ == '__main__':
    unittest.main()
