import numpy as np
import pandas as pd

class DataAnalysis:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def calculate_least_squares(self, training_data, ideal_functions):
        results = {}
        # Assuming that training_data and ideal_functions are DataFrames
        for func in [f'y{i}' for i in range(1, 51)]:  # Correct column names 'Y1' to 'Y50'
            sse = 0
            for i in range(1, 5):  # There are four Y columns in training_data 'Y1' to 'Y4'
                train_col = f'y{i}'
                sse += ((training_data[train_col] - ideal_functions[func]) ** 2).sum()
            results[func] = sse
        return results

    def select_best_functions(self, sse_results):
        return sorted(sse_results, key=sse_results.get)[:4]

    def map_test_data(self, test_data, ideal_functions, best_functions, max_deviations):
        mapping_results = []
        for index, row in test_data.iterrows():
            x, y = row['x'], row['y']  # Make sure to use 'X' if that's the correct column name
            mapped = False
            for func in best_functions:
                # Filter ideal_functions based on 'X' and extract the ideal y-value for the function
                filtered = ideal_functions[ideal_functions['X'] == x]
                if not filtered.empty:
                    ideal_y = filtered[func].iloc[0]
                    deviation = abs(y - ideal_y)
                    if deviation <= np.sqrt(2) * max_deviations[func]:
                        mapping_results.append((x, y, func, deviation))
                        mapped = True
                        break
            if not mapped:
                mapping_results.append((x, y, 'None', None))  # Append a result for unmapped data points
        return mapping_results


    def calculate_max_deviations(self, training_data, ideal_functions, best_functions):
        max_deviations = {}
        for func in best_functions:
            deviations = []
            for index, row in training_data.iterrows():
                x = row['x']
                y_values = row[['y1', 'y2', 'y3', 'y4']]
                ideal_y = ideal_functions.loc[ideal_functions['x'] == x, func].iloc[0]
                deviations.append((y_values - ideal_y).abs().max())
            max_deviations[func] = max(deviations)
        return max_deviations
