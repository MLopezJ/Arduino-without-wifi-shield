import serial
import time

usbport ='/com3'
serialConnection = 9600 #bits per second 
arduino = serial.Serial(usbport, serialConnection)
time.sleep(2)

try:
    while True:
        value = arduino.readline()         # read a byte string
        string_n_value = value.decode()  # decode byte string into Unicode  
        string_value = string_n_value.rstrip() # remove \n and \r
        humidity = int(string_value)
        if (humidity < 500):
            print("wet: ", humidity)  
        else:
            print("NOT wet: ", humidity)
        
    
        time.sleep(0.1)            # wait (sleep) 0.1 seconds

except KeyboardInterrupt:
    print('-Closed data reading-')
    arduino.close()