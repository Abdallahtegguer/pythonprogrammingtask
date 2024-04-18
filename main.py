from database import DatabaseManager
from analysis import DataAnalysis
from visualization import Visualizer

def main():
    db_manager = DatabaseManager('sqlite:///my_data.db')
    analysis = DataAnalysis(db_manager)
    visualizer = Visualizer()

    training_data = db_manager.fetch_data('training_data')
    ideal_functions = db_manager.fetch_data('ideal_functions')
    test_data = db_manager.fetch_data('test_data')

    # Assuming the selection and deviation calculation logic is already implemented
    best_functions = ['y48', 'y44', 'y50', 'y2']  # Placeholder for selected functions
    max_deviations = {'y48': 1.0, 'y44': 1.1, 'y50': 1.2, 'y2': 0.9}  # Example deviations

    mapping_results = analysis.map_test_data(test_data, ideal_functions, best_functions, max_deviations)
    visualizer.plot_data(mapping_results, "Test Data Mapping Results")

    except Exception as e:
        print(f"Failed to execute analysis or data fetching: {e}")


if __name__ == '__main__':
    main()
