# Smart Gujarat Hackathon 2019
## SGH175: Traffic Clearance for Ambulance/(or other priority Vehicle) through Artificial Intelligence


GUI_Class2 = main


### PROCESS to GIVE WORKING DEMO OF PROJECT

1.  Install python dependency packages on host PC using:
     ```
     sudo apt-get install python3-tk
     sudo pip install polyline
     sudo pip install firebase
     sudo pip install paho_mqtt
     ```

2.  Upload ino codes on 3 demo ESP32  (ie  Signal1, Signal2,  Signal3)
    Lights will start toggling on board whrn PYGAME_SIMULATION code will be started (change wifi credentials set as default)

3.  Setup Android application:
    - Install mobile appliction.
    - Enable GPS on mobile and open Test Mode in app.
    - Set origin & destination by first clicking on bottom option and then touch the point on map to set location.
    - Long press on Start Journey button (blue Arrow button in bottom) to start sending GPS coordinates to the Firebase.
4.  Open Folder PythonMain_Working_gui_implemented_with_function
    - Start GUI_Class2.py with command:
    ```
    python GUI_Class2.py
    ```

5.  In browser open Google Firebase realtime updates of coordinates.

6.  (Optional/Under testing) To start realtime Traffic simulaion, Open Folder TrafficSimulation_pygame_simulation
    - Install python dependency:
    ```
    sudo pip install pygame
    ```
    - Start simulation.py using python command:
    ```
    python simulation.py
    ```

### Overview

This app is designed to allow smart switching of traffic signals for Emergency Vehicles. The main components of this system are 
1. Master Control application
2. Android App for navigation
3. IOT devices at each Signal 

### Working Explaination

- Whenever an Emergency vehicle starts it's journey it. It starts app and registers it's starting and destination coordinates. And starts sending it's Live location to Google Firebase.

- Master Control application registers the journey and uses MapMyIndia Navigation and Direction API to find the path of journey (that is assumed to remain same in whole journey) and lists down all the signal crossings in it's path.

- The master app also maintains a list of all the coordinates of signal crossing in the city and uses them to find which signals are going to come in the path of jouney of emergency vehicle in order.

- Then it continously tracks the Live location of Emergency vehicle and check it distance from the signals in order continously. Whenever the vehicle distance is less then 500 meters from the signal, it signals the IOT device at that signal to turn ON Green so that any traffic in it's way is cleared before the vehicle approches the signal. Hence the Signal is Clear for the Emergency Vehicle to pass smoothly.

- This is repeated continously until the vehicle reaches it's destination.


### NOTE

1.  This code is only implimented for 1 emergency vehicle

2.  Traffic simulation is controlled by random number generator and is not the actual representation of traffic occurance on the roads

3.  Mobile application is made in kodular with email : rrohit22896@gmail.com on the Kodular version Eagle (current available kodular version is Fennix)
    in Eagle version we can use google map for free but in later version ie Fennix this map feature was not available for free some expected features like
    (driver nofication of next signal, show signals in route, start firebase to start journey wasn't implemented (bcz I wanted to use a JourneyState flag for this[see firebase output])) were not implemented in app because doing modification in app and then downloading will come with new map feature restrictions 

5.  Realtime Firebase Database was implimented on email : esp32.2.rohit@gmail.com

6.  Many other files are avaialble on Google Drive (almost all important ones are already here)
