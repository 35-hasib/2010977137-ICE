import serial
import time

def get_gps_coordinates():
    # Open the serial port that the GPS device is connected to
    # Replace 'COM3' with the appropriate COM port (you can check in Device Manager)
    gps = serial.Serial('COM3', baudrate=9600, timeout=1)
    
    while True:
        data = gps.readline()  # Read a line of data from the GPS
        if data:
            print(data)  # Print raw NMEA data (GPS data)
            # You can parse the NMEA sentence here to extract latitude and longitude
        time.sleep(1)  # Add a delay to avoid overwhelming the serial connection

# Example usage
get_gps_coordinates()
