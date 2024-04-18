import numpy as np

class DataAnalysis:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Existing functions...

    def map_test_data(self, test_data, ideal_functions, best_functions, max_deviations):
        mapping_results = []
        for index, row in test_data.iterrows():
            x = row['x']
            y = row['y']
            mapped = False
            for func in best_functions:
                ideal_y = ideal_functions.at[index, func]  # Get ideal y-value for the same x
                deviation = abs(y - ideal_y)
                allowed_deviation = np.sqrt(2) * max_deviations[func]
                if deviation <= allowed_deviation:
                    mapping_results.append((x, y, func, deviation))
                    mapped = True
                    break  # Assuming one match is enough
            if not mapped:
                mapping_results.append((x, y, 'None', None))  # No function matched
        return mapping_results
