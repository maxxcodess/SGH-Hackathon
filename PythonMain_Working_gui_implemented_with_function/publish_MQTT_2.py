import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # SIG0001/Dir:1/Time:5
    # device1/relay1/4
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

def Send_MQTT_Message(device = '', message = '') :
# message = input("enter message1 :")
    client.publish(device, message)
    print("~~~~~~~~~~~~~~sent mqtt command ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(0.05)
# message2 = input("enter message2 :")
# client.publish('esp/test2', message2)
# time.sleep(2)
# client.loop_forever()
