import serial, sys, time

ser = serial.Serial('/dev/ttyACMgi0')
ser.write(b'1')
time.sleep(1)
ser.write(b'0')