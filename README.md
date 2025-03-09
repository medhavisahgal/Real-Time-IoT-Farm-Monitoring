# Farm Monitoring IoT Sensor Simulator

This repository contains a Python script that simulates soil moisture and temperature sensors and sends the data to Azure IoT Hub.

## Prerequisites
- Python 3.9+
- Azure IoT Hub & registered device
- `pip install -r requirements.txt`

## Usage
1. Update `CONNECTION_STRING` in `sensor_simulator.py`.
2. Run the script:
   ```sh
   python sensor_simulator.py
   ```
3. Stop with `CTRL + C`.

## Troubleshooting
- Update SSL certificates:
  ```sh
  pip install --upgrade certifi
  ```
- Force stop if needed:
  ```sh
  taskkill /F /IM python.exe  # Windows
  killall python              # Linux/Mac
  ```

## License
MIT License - see [LICENSE](LICENSE).
