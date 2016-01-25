# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import grovepi

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("bastide/grove/potentiometer")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print "Topic: " + msg.topic + "\nValue: " + msg.payload
    # Send PWM signal to LED
    grovepi.analogWrite(led,int(msg.payload)/4)


# Connect the LED to digital port D5
led = 5

grovepi.pinMode(led,"OUTPUT")
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
    
client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

grovepi.analogWrite(led,0)
