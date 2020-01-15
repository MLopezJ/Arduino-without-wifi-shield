# Posting data with Arduino to an API without wifi shield

This is a prove of concept trying to solve a situacion with the resources available. 

The solution consist in read the sensor data with the Arduino and use another controller as a server (in this case, a computer), this server will be able to read the sensor data in the Arduino and then, it will make a post to an external API. The server require to have internet conexion. 

## Hardware used
+ Arduino UNO
+ Soil humidity sensor 

## Software used 
+ soil_moisture.ino (read sensor)
+ main.py (server)
+ Thingspeak API

The result can be found here: https://thingspeak.com/channels/907210