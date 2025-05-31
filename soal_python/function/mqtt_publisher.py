import paho.mqtt.client as mqtt
import json
import random
import os
import csv
from datetime import datetime
import pytz


class MqttDataPublisher:
    """Class to handle MQTT data publishing and logging"""
    
    def __init__(self, candidate_name):
        self.candidate_name = candidate_name
        self.broker_host = "test.mosquitto.org"
        self.broker_port = 1883
        self.topic = f"mqtt/{candidate_name}/data"
        self.log_dir = os.path.join(os.path.dirname(__file__), "..", "log")
        
        self.client = mqtt.Client()
        self.client.on_connect = self.onConnect
        self.client.on_publish = self.onPublish
        
        self.ensureLogDirectory()
        self.connectToBroker()
    
    
    def ensureLogDirectory(self):
        """Ensure log directory exists"""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
    
    
    def connectToBroker(self):
        """Connect to MQTT broker"""
        try:
            self.client.connect(self.broker_host, self.broker_port, 60)
            self.client.loop_start()
        except Exception as e:
            print(f"Error connecting to MQTT broker: {e}")
    
    
    def onConnect(self, client, userdata, flags, rc):
        """Callback for when client connects to broker"""
        if rc == 0:
            print("Connected to MQTT broker successfully")
        else:
            print(f"Failed to connect to MQTT broker, return code {rc}")
    
    
    def onPublish(self, client, userdata, mid):
        """Callback for when message is published"""
        pass
    
    
    def getCurrentTimestampGmt7(self):
        """Get current timestamp in GMT+7 format"""
        jakarta_tz = pytz.timezone("Asia/Jakarta")
        current_time = datetime.now(jakarta_tz)
        return current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    
    def getCurrentTimestampUtc(self):
        """Get current timestamp in UTC format"""
        utc_time = datetime.utcnow()
        return utc_time.strftime("%Y-%m-%d %H:%M:%S")
    
    
    def getWeatherData(self):
        """Get weather data from JSON file"""
        json_file_path = os.path.join(self.log_dir, "data_weather.json")
        
        try:
            with open(json_file_path, "r") as file:
                data = json.load(file)
                return data["temperature"], data["humidity"]
        except Exception as e:
            print(f"Error reading weather data: {e}")
            return 25.0, 60.0  # Default values
    
    
    def generateSensorData(self):
        """Generate random sensor data"""
        temperature, humidity = self.getWeatherData()
        
        sensor_data = {
            "nama": self.candidate_name,
            "data": {
                "sensor1": random.randint(0, 100),
                "sensor2": round(random.uniform(0, 1000), 2),
                "sensor3": random.choice([True, False]),
                "sensor4": float(temperature),
                "sensor5": float(humidity)
            },
            "timestamp": self.getCurrentTimestampUtc()
        }
        
        return sensor_data
    
    
    def publishSensorData(self):
        """Publish sensor data to MQTT broker"""
        sensor_data = self.generateSensorData()
        json_payload = json.dumps(sensor_data)
        timestamp_gmt7 = self.getCurrentTimestampGmt7()
        
        try:
            result = self.client.publish(self.topic, json_payload)
            
            if result.rc == 0:
                status = "Success"
                print(f"Timestamp : {timestamp_gmt7}")
                print(f"Action : Publish")
                print(f"Topic : {self.topic}")
                print(f"Data : {json_payload}")
                print(f"State : {status}")
                print("-" * 50)
            else:
                status = "Failed"
                print(f"Timestamp : {timestamp_gmt7}")
                print(f"Action : Publish")
                print(f"Topic : {self.topic}")
                print(f"Data : {json_payload}")
                print(f"State : {status}")
                print("-" * 50)
            
            # Log to CSV file
            self.logToCsv(sensor_data, status, timestamp_gmt7)
            
        except Exception as e:
            status = "Failed"
            print(f"Error publishing data: {e}")
            self.logToCsv(sensor_data, status, timestamp_gmt7)
    
    
    def logToCsv(self, sensor_data, status, timestamp_gmt7):
        """Log data to CSV file"""
        # Generate filename based on current date
        current_date = datetime.now().strftime("%d%m%y")
        csv_filename = f"mqtt_log_{current_date}.csv"
        csv_file_path = os.path.join(self.log_dir, csv_filename)
        
        # Check if file exists to determine if we need to write header
        file_exists = os.path.exists(csv_file_path)
        
        try:
            with open(csv_file_path, "a", newline="") as csvfile:
                fieldnames = ["timestamp", "sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "status"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
                
                # Write header if file is new
                if not file_exists:
                    writer.writeheader()
                
                # Write data row
                writer.writerow({
                    "timestamp": timestamp_gmt7,
                    "sensor1": sensor_data["data"]["sensor1"],
                    "sensor2": sensor_data["data"]["sensor2"],
                    "sensor3": sensor_data["data"]["sensor3"],
                    "sensor4": sensor_data["data"]["sensor4"],
                    "sensor5": sensor_data["data"]["sensor5"],
                    "status": status
                })
                
        except Exception as e:
            print(f"Error logging to CSV: {e}")
    
    
    def disconnect(self):
        """Disconnect from MQTT broker"""
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected from MQTT broker")