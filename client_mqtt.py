import paho.mqtt.client as mqttClient
import time

def on_Connect(clent, userdata, flags, rc):
    if rc == 0:
        print ("Connected")
        global Connected
        Connected = True
    else:
        print ("Connection failed")

Connected = False

broker_addr="localhost"
port= 1883
user = ""
password = ""

client = mqttClient.Client("Python")
client.username_pw_set(user, password = password)
client.connect(broker_addr, port = port)
client.loop_start()

while Connected != True:
    time.sleep(0.1)

try:
    while True:
        v = taw_input("Enter the mqtt topic value")
        client.publish("harry/harry", v)
except KeyboardInterruption:
        client.disconnect()
        client.loop_stop()


