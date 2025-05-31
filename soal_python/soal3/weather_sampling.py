import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "function"))

import time
from weather_sampler import WeatherSampler


class WeatherSamplingApp:
    """Main application class for weather data sampling"""
    
    def __init__(self):
        self.sampler = WeatherSampler()
        self.city_name = "Bandung"  # Default city
    
    
    def getUserInput(self):
        """Get sampling interval from user input"""
        while True:
            try:
                user_input = input("Masukkan nama kota (default: Bandung): ")
                if user_input.strip() == "":
                    self.city_name = "Bandung"
                else:
                    self.city_name = user_input.strip()

                user_input = input("Masukkan interval sampling (detik, angka diatas 0): ")
                interval = float(user_input)
                
                if interval <= 0:
                    print("Error: Masukkan angka diatas 0")
                    continue
                
                return int(interval)
                
            except ValueError:
                print("Error: Masukkan angka diatas 0")
    
    
    def runSampling(self):
        """Run the weather sampling process"""
        print("=== Weather Data Sampling Application ===")
        print(f"Kota yang digunakan: {self.city_name}")
        
        interval = self.getUserInput()
        
        print(f"Memulai sampling data weather dengan interval {interval} detik...")
        print("Tekan Ctrl+C untuk menghentikan program")
        
        try:
            while True:
                self.sampler.sampleWeatherData(self.city_name)
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh user")


def main():
    """Main function to run weather sampling application"""
    app = WeatherSamplingApp()
    app.runSampling()


if __name__ == "__main__":
    main()