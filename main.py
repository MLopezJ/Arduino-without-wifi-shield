import serial
import time

usbport ='/com3'
serialConnection = 9600 #bits per second 
arduino = serial.Serial(usbport, serialConnection)
time.sleep(2)

while True:
    value = arduino.readline()         # read a byte string
    string_n_value = value.decode()  # decode byte string into Unicode  
    string_value = string_n_value.rstrip() # remove \n and \r
    print(string_value)
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

#arduino.close()
