from database import DatabaseManager
from preanalysis import DataAnalysis
from visualization import Visualizer

def main():
    db_manager = DatabaseManager('sqlite:///my_data.db')
    analysis = DataAnalysis(db_manager)
    visualizer = Visualizer()

    training_data = db_manager.fetch_data('training_data')
    ideal_functions = db_manager.fetch_data('ideal_functions')
    test_data = db_manager.fetch_data('test_data')

    sse_results = analysis.calculate_least_squares(training_data, ideal_functions)
    best_functions = analysis.select_best_functions(sse_results)
    
    print("Best functions selected:", best_functions)

    # Assuming you add more logic to map test data and save results...
    # visualizer.plot_data(mapped_results)  # Visualize the mapping results

if __name__ == '__main__':
    main()
