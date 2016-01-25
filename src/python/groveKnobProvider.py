    # -*- coding: utf-8 -*-
import time
import grovepi
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("bastideGroveProvider")
mqttc.connect("test.mosquitto.org", 1883)
mqttc.loop_start()

# Connect the Rotary Angle Sensor to analog port A2
potentiometer = 2

time.sleep(1)

oldValue = -1
newValue = 0

while True:
    try:
        # Read resistance from Potentiometer
        newValue = grovepi.analogRead(potentiometer)
        print "Read: " + str(newValue)
        if (newValue != oldValue):
            oldValue = newValue
            print "Sending: " + str(newValue)
            mqttc.publish("bastide/grove/potentiometer", newValue)
        
        time.sleep(1)
        
    except KeyboardInterrupt:   
        break

    except IOError:
        print "Error"

mqttc.loop_stop()
