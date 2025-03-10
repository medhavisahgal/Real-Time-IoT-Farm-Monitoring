import os
import certifi
from azure.iot.device import IoTHubDeviceClient, Message
import random
import time
os.environ["SSL_CERT_FILE"] = certifi.where()
CONNECTION_STRING = "For security purpose here I am not adding my connection string"

def simulate_sensor():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    while True:
        soil_moisture = random.randint(20, 80)  
        temperature = random.randint(15, 40)  
        msg = Message(f'{{"soil_moisture": {soil_moisture}, "temperature": {temperature}}}')
        client.send_message(msg)
        print(f"Sent: Moisture={soil_moisture}%, Temp={temperature}°C")
        time.sleep(10) 
if __name__ == "__main__":
    simulate_sensor()
