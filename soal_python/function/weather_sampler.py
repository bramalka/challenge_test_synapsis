import requests
import json
import os
from datetime import datetime
import pytz


class WeatherSampler:
    """Class to handle weather data sampling from OpenWeatherMap API"""
    
    def __init__(self):
        self.API_KEY = "f7469b6761c410964085a0a8c8c05493"  # Replace with actual API key
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
        self.log_dir = os.path.join(os.path.dirname(__file__), "..", "log")
        self.ensureLogDirectory()
    
    
    def ensureLogDirectory(self):
        """Ensure log directory exists"""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
    
    
    def getCurrentTimestamp(self):
        """Get current timestamp in GMT+7 format"""
        jakarta_tz = pytz.timezone("Asia/Jakarta")
        current_time = datetime.now(jakarta_tz)
        return current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    
    def saveToJsonFile(self, temperature, humidity):
        """Save weather data to JSON file"""
        weather_data = {
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": self.getCurrentTimestamp(),
            "unit_temperature": "Celsius",
            "unit_humidity": "Percent"
        }
        
        json_file_path = os.path.join(self.log_dir, "data_weather.json")
        
        try:
            with open(json_file_path, "w") as file:
                json.dump(weather_data, file, indent=4)
        except Exception as e:
            print(f"Error saving to JSON file: {e}")
    
    
    def sampleWeatherData(self, city_name):
        """Sample weather data from OpenWeatherMap API"""
        timestamp = self.getCurrentTimestamp()
        
        try:
            # Construct API URL
            url = f"{self.BASE_URL}?q={city_name}&appid={self.API_KEY}&units=metric"
            
            # Make API request
            response = requests.get(url, timeout=10)
            print(response)
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract temperature and humidity
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                
                # Save to JSON file
                self.saveToJsonFile(temperature, humidity)
                
                # Print success message
                print(f"({timestamp}) - Success Running Sampling Data Weather with Result Temperature {temperature} Celsius & Humidity {humidity} Percent")
                
            else:
                # Print error message
                error_msg = "Unknown error"
                try:
                    error_data = response.json()
                    error_msg = error_data.get("message", "Unknown error")
                except:
                    error_msg = response.text if response.text else "Unknown error"
                
                print(f"({timestamp}) - Failed Running Sampling Data Weather with Status Code {response.status_code} - {error_msg}")
                
        except requests.exceptions.Timeout:
            print(f"({timestamp}) - Failed Running Sampling Data Weather with Status Code Timeout - Request timeout")
        except requests.exceptions.ConnectionError:
            print(f"({timestamp}) - Failed Running Sampling Data Weather with Status Code Connection Error - No internet connection")
        except Exception as e:
            print(f"({timestamp}) - Failed Running Sampling Data Weather with Status Code Error - {str(e)}")