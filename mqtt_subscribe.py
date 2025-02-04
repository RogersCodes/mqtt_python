import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
#callback API Version

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Smartphone")
client.connect(mqttBroker)

#on_message callback
client.on_message = on_message

client.subscribe("TEMPERATURE")

client.loop_start()

client.on_message = on_message
time.sleep(30)
client.loop_stop()
