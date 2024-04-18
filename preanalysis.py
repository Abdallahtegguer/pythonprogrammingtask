import numpy as np
import pandas as pd

class DataAnalysis:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def calculate_least_squares(self, training_data, ideal_functions):
        results = {}
        try:
            for func in [f'y{i}' for i in range(1, 51)]:  # Assumes 'Y1' to 'Y50' are correct column names
                sse = 0
                for i in range(1, 5):  # Assumes 'Y1' to 'Y4' in training_data
                    train_col = f'y{i}'
                    if train_col in training_data.columns and func in ideal_functions.columns:
                        sse += ((training_data[train_col] - ideal_functions[func]) ** 2).sum()
                    else:
                        print(f"Missing column in DataFrame: {train_col} or {func}")
                results[func] = sse
        except Exception as e:
            print(f"Error calculating least squares: {e}")
        return results

    def select_best_functions(self, sse_results):
        try:
            return sorted(sse_results, key=sse_results.get)[:4]
        except Exception as e:
            print(f"Error selecting best functions: {e}")
            return []

    def map_test_data(self, test_data, ideal_functions, best_functions, max_deviations):
        mapping_results = []
        try:
            for index, row in test_data.iterrows():
                x, y = row['x'], row['y']
                mapped = False
                for func in best_functions:
                    filtered = ideal_functions[ideal_functions['x'] == x]
                    if not filtered.empty and func in filtered.columns:
                        ideal_y = filtered[func].iloc[0]
                        deviation = abs(y - ideal_y)
                        if deviation <= np.sqrt(2) * max_deviations.get(func, float('inf')):
                            mapping_results.append((x, y, func, deviation))
                            mapped = True
                            break
                if not mapped:
                    mapping_results.append((x, y, 'None', None))
        except Exception as e:
            print(f"Error mapping test data: {e}")
        return mapping_results

    def calculate_max_deviations(self, training_data, ideal_functions, best_functions):
        max_deviations = {}
        try:
            for func in best_functions:
                deviations = []
                for index, row in training_data.iterrows():
                    x = row['x']
                    if 'x' in ideal_functions.columns and func in ideal_functions.columns:
                        ideal_y = ideal_functions.loc[ideal_functions['x'] == x, func].iloc[0]
                        deviations.append((row[['y1', 'y2', 'y3', 'y4']] - ideal_y).abs().max())
                max_deviations[func] = max(deviations) if deviations else 0
        except Exception as e:
            print(f"Error calculating max deviations for {func}: {e}")
        return max_deviations
