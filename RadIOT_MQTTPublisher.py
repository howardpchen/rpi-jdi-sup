#!/usr/bin/python
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import sys

client_id = "RadIOT_phone1"
server = "iot.eclipse.org"
location = "testLocation"
try:
    message = ' '.join(sys.argv[1:].replace('@',''))
except:
    message = "Test Message"

def init_mqtt():
    client=mqtt.Client(client_id)
    client.connect(server)
    return client
    
def publish_msg(c, txt):
    result = c.publish("/".join([location, client_id]), 
                       "@".join([txt, str(time.time())]))
    if (result[0] == mqtt.MQTT_ERR_SUCCESS):
        print("Successfully published message", txt)
    else:
        print("Failed publishing message", txt, ". Error code", result[0])

client = init_mqtt();
publish_msg(client, message)
