import paho.mqtt.client as mqtt
from random import randrange
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Temperature_Outside")
client.connect(mqttBroker)

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
