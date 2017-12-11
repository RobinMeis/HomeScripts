import urllib.request, urllib.parse
import json
import paho.mqtt.client as mqtt

def get_departures(stop_id): #Gets the current departures of a stop. Get the stop ID by sniffing post requests of https://www.aseag.de/fahrplan/abfahrtsmonitor/ (Post parameter stage)
    data = {
    'res' : 'timetable',
    'stage' : stop_id,
    }
    data = bytes( urllib.parse.urlencode( data ).encode() )
    handler = urllib.request.urlopen( 'https://ifa.aseag.de/index.php?id=344&eID=mbient_ifa', data );
    return handler.read().decode('UTF-8')

def on_connect(client, userdata, flags, rc): #Fetch and publish aseag data after successfull connection to  MQTT server
    print("Connected with result code "+str(rc))

    client.publish("aseag/departures/Viktoriallee", get_departures(401), 1) #Specify your topics / bus stops here
    client.publish("aseag/departures/Normaluhr", get_departures(61), 1)
    client.publish("aseag/departures/Scheibenstrasse", get_departures(109), 1)
    client.disconnect()


client = mqtt.Client()
client.on_connect = on_connect

client.connect("server", 1883, 60) #Specify your MQTT server here
client.loop_forever()
