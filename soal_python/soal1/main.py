import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "function"))

from statistical_functions import StatisticalCalculator # type: ignore

def main():
    """Main function to test statistical calculations"""
    # Sample data
    test_data = [23, 45, 90, 67, 23, 89, 34, 23, 56, 78]
    
    calculator = StatisticalCalculator()
    
    # Calculate
    max_value = calculator.calculateMaximum(test_data)
    min_value = calculator.calculateMinimum(test_data)
    avg_value = calculator.calculateAverage(test_data)
    mode_value = calculator.calculateMode(test_data)
    
    # Results
    print(f"Value : {test_data}")
    print(f"Nilai Maksimum : {max_value}")
    print(f"Nilai Minimum : {min_value}")
    print(f"Nilai Rata-Rata : {avg_value}")
    print(f"Nilai Modbus : {mode_value}")


if __name__ == "__main__":
    main()