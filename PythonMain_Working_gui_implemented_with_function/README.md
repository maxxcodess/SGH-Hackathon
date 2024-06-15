main() = GUI_Class2.py


## Overview

This app is designed to allow smart switching of traffic signals for Emergency Vehicles. The main components of this system are 
1. Master Control application
2. Android App for navigation
3. IOT devices at each Signal 

## Working Explaination

- Whenever an Emergency vehicle starts it's journey it. It starts app and registers it's starting and destination coordinates. And starts sending it's Live location to Google Firebase.

- Master Control application registers the journey and uses MapMyIndia Navigation and Direction API to find the path of journey (that is assumed to remain same in whole journey) and lists down all the signal crossings in it's path.

- The master app also maintains a list of all the coordinates of signal crossing in the city and uses them to find which signals are going to come in the path of jouney of emergency vehicle in order.

- Then it continously tracks the Live location of Emergency vehicle and check it distance from the signals in order continously. Whenever the vehicle distance is less then 500 meters from the signal, it signals the IOT device at that signal to turn ON Green so that any traffic in it's way is cleared before the vehicle approches the signal. Hence the Signal is Clear for the Emergency Vehicle to pass smoothly.

- This is repeated continously until the vehicle reaches it's destination.


## Technical

- This App maintains a list of all the coordinates of signal crossing in a city in file Signal_Coords_1.py.

- This app uses MapMyIndia API Navigation and Direction free Keys to get directions and coordinates mentioned in mapmyClass.py file in keyList variable.

- Each free key comes with per day limited request (around 50 requests).

- This App is designed in a way that when the limit is exceeded for one key then it automatically switches to new key.

- Each web request to MapMyIndia, gives back a long JSON string, that needs to be parsed to read coordinates and directions. This app parses the JSON strings and finds the distance between 2 coordinates.

- When Distance is less than 500 meters then the app triggers the IOT device that is the ESP32 connected with RGB leds. Messaging is done using MQTT.

- This app has some hardcoded variables like credentials for MapMyIndia Keys, Firebase, mqtt, Signal coordinates in city, WiFi etc.
