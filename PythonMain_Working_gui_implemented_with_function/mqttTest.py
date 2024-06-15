from publish_MQTT_2 import *
import time

SignalHardware = ['signal1/relay1', 'signal2/relay1', 'signal3/relay1']

Send_MQTT_Message(SignalHardware[0], '10')
time.sleep(5)
Send_MQTT_Message(SignalHardware[1], '5')
time.sleep(5)
Send_MQTT_Message(SignalHardware[2], '5')