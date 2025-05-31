class StatisticalCalculator:
        
    def calculateMaximum(self, data_list):
        """Calculate maximum value from a list without using built-in max function"""
        if not data_list:
            return None
        
        max_val = data_list[0]
        for value in data_list:
            if value > max_val:
                max_val = value
        return max_val


    def calculateMinimum(self, data_list):
        """Calculate minimum value from a list without using built-in min function"""
        if not data_list:
            return None
        
        min_val = data_list[0]
        for value in data_list:
            if value < min_val:
                min_val = value
        return min_val


    def calculateAverage(self, data_list):
        """Calculate average value from a list without using built-in functions"""
        if not data_list:
            return None
        
        total_sum = 0
        count = 0
        
        for value in data_list:
            total_sum += value
            count += 1
        
        return total_sum / count


    def calculateMode(self, data_list):
        """Calculate mode value from a list without using built-in functions"""
        if not data_list:
            return None
        
        # Count frequency of each element
        frequency_dict = {}
        for value in data_list:
            if value in frequency_dict:
                frequency_dict[value] += 1
            else:
                frequency_dict[value] = 1
        
        # Find the maximum frequency
        max_frequency = 0
        for freq in frequency_dict.values():
            if freq > max_frequency:
                max_frequency = freq
        
        # Find all values with maximum frequency
        mode_values = []
        for value, freq in frequency_dict.items():
            if freq == max_frequency:
                mode_values.append(value)
        
        # Return the smallest mode value if multiple modes exist
        if mode_values:
            mode_result = mode_values[0]
            for mode_val in mode_values:
                if mode_val < mode_result:
                    mode_result = mode_val
            return mode_result
        
        return None