import paho.mqtt.client as mqtt
from random import uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"

#Specify the callback API version
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Temperature_Inside")
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
