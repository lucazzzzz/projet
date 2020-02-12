import serial

ser = serial.Serial('COM5')
print(ser.name)
ser.write(b'hello')
ser.close()