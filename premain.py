from database import DatabaseManager
from preanalysis import DataAnalysis
from visualization import Visualizer

def main():
    try:
        db_manager = DatabaseManager('sqlite:///my_data.db')
        analysis = DataAnalysis(db_manager)
        visualizer = Visualizer()

        # Fetching data with error handling
        try:
            training_data = db_manager.fetch_data('training_data')
            ideal_functions = db_manager.fetch_data('ideal_functions')
            test_data = db_manager.fetch_data('test_data')
        except Exception as e:
            print(f"Error fetching data from database: {e}")
            return

        # Calculate least squares with error handling
        try:
            sse_results = analysis.calculate_least_squares(training_data, ideal_functions)
            best_functions = analysis.select_best_functions(sse_results)
            print("Best functions selected:", best_functions)
        except Exception as e:
            print(f"Error processing data analysis: {e}")
            return
        
        # Example additional logic to map test data
        try:
            max_deviations = analysis.calculate_max_deviations(training_data, ideal_functions, best_functions)
            mapped_results = analysis.map_test_data(test_data, ideal_functions, best_functions, max_deviations)
            visualizer.plot_data(mapped_results)  # Visualize the mapping results
        except Exception as e:
            print(f"Error in mapping or visualization: {e}")

    except Exception as e:
        print(f"Unexpected error in main function: {e}")

if __name__ == '__main__':
    main()
