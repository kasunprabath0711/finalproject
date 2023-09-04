import serial

# Open the serial port (update port and baud rate as needed)
ser = serial.Serial('COM7', 9600)

while True:
        # Read data from the serial port
        data = ser.readline().decode().strip()
        print(data)