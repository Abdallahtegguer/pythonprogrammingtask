import numpy as np

# is analysis.py should we shouls run after running the pre_analysis.py file because the pre_analysis.py file is the one we are using to findn ideal functions

class DataAnalysis:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Existing functions...

    def map_test_data(self, test_data, ideal_functions, best_functions, max_deviations):
        mapping_results = []
        try:
            for index, row in test_data.iterrows():
                x = row['x']
                y = row['y']
                mapped = False
                for func in best_functions:
                    if func in ideal_functions.columns and 'x' in ideal_functions.columns:
                        # Ensure there is a row in ideal_functions where 'x' matches the test_data 'x'
                        filtered_ideal = ideal_functions[ideal_functions['x'] == x]
                        if not filtered_ideal.empty:
                            ideal_y = filtered_ideal[func].iloc[0]
                            deviation = abs(y - ideal_y)
                            allowed_deviation = np.sqrt(2) * max_deviations[func]
                            if deviation <= allowed_deviation:
                                mapping_results.append((x, y, func, deviation))
                                mapped = True
                                break  # Assuming one match is enough
                if not mapped:
                    mapping_results.append((x, y, 'None', None))  # No function matched
        except KeyError as e:
            print(f"Key error: {e} - Check column names and DataFrame structure.")
        except IndexError as e:
            print(f"Index error: {e} - Check if DataFrame indexes are aligned or if DataFrame is empty.")
        except Exception as e:
            print(f"Unexpected error during mapping: {e}")

        return mapping_results
