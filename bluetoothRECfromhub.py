import serial
import time


COM_PORT = "COM5"
BAUD_RATE = 115200

ser = serial.Serial(COM_PORT, BAUD_RATE)
time.sleep(2)  

print("Type motor speed values, Press Ctrl+C to exit.")
try:
    while True:
        user_input = input("Speed: ")
        if user_input.strip().isdigit() or (user_input.startswith("-") and user_input[1:].isdigit()):
            ser.write((user_input + "\n").encode())
        else:
            print("Invalid input. Use an integer.")
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser.close()
