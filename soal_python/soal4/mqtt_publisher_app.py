import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "function"))

import time
from mqtt_publisher import MqttDataPublisher # type: ignore


class MqttSensorApp:
    """Main application class for MQTT sensor data publishing"""
    
    def __init__(self):
        self.candidate_name = "bram"
        self.publisher = MqttDataPublisher(self.candidate_name)
        self.PUBLISH_INTERVAL = 5  # 5 seconds
    
    
    def runPublishing(self):
        """Run the MQTT publishing process"""
        print("=== MQTT Sensor Data Publisher ===")
        print(f"Kandidat: {self.candidate_name}")
        print(f"Server: mosquitto.org")
        print(f"Topic: mqtt/{self.candidate_name}/data")
        print(f"Interval: {self.PUBLISH_INTERVAL} detik")
        print("Tekan Ctrl+C untuk menghentikan program")
        print("-" * 50)
        
        try:
            while True:
                self.publisher.publishSensorData()
                time.sleep(self.PUBLISH_INTERVAL)
                
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh user")
        finally:
            self.publisher.disconnect()


def main():
    """Main function to run MQTT sensor application"""
    app = MqttSensorApp()
    app.runPublishing()


if __name__ == "__main__":
    main()