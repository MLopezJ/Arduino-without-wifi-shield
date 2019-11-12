import serial
import time
import http.client
import urllib

usbport ='/com3'
serialConnection = 9600 #bits per second 
arduino = serial.Serial(usbport, serialConnection)
api_key = ''
time.sleep(2)

def post_humidity (humidity):

    params = urllib.parse.urlencode({'field1': humidity, 'api_key':api_key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")

    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print (humidity)
        print (response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")

def main ():

    try:
        while True:
            value = arduino.readline()         # read a byte string
            string_n_value = value.decode()  # decode byte string into Unicode  
            string_value = string_n_value.rstrip() # remove \n and \r
            humidity = int(string_value)

            post_humidity(humidity)
            
            if (humidity < 500):
                print("wet: ", humidity)  
            else:
                print("NOT wet: ", humidity)
            
        
            #time.sleep(5)            # wait (sleep) 5 seconds

    except KeyboardInterrupt:
        print('-Closed data reading-')
        arduino.close()

main()