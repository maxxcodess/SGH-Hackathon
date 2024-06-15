import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # SIG0001/Dir:1/Time:5
    # device1/relay1/4
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

# message = input("enter message2 :")
# client.publish('esp/test1', message)
while 1:
    message1 = input("enter message1 :")
    client.publish('device1/relay1', message1)
    time.sleep(2)
    message2 = input("enter message2 :")
    client.publish('device2/relay1', message2)
    time.sleep(2)
    message3 = input("enter message3 :")
    client.publish('device3/relay1', message3)
    time.sleep(2)
client.loop_forever()
