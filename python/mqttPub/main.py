#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2010-2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# Copyright (c) 2010,2011 Roger Light <roger@atchoo.org>
# All rights reserved.

# This shows a simple example of waiting for a message to be published.

#import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.client as mqtt
import random

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

a = random.randint(0, 1)
b = random.randint(0, 1)
c = random.randint(0, 1)
d = random.randint(0, 1)
e = random.randint(0, 1)

jsonVar = "{ \"thumbFinger\": " + "\"" + str(a) + "\"" + ", \"indexFinger\": " + "\"" + str(b) + "\"" + ", \"middleFinger\": " \
          + "\"" + str(c) + "\"" + ", \"ringFinger\": " + "\"" + str(d) + "\"" + ", \"pinkyFinger\": " + "\"" + str(e) + "\"" + " }"

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("test.mosquitto.org", 1883, 60)

mqttc.loop_start()

#(rc, mid) = mqttc.publish("tuple", "bar", qos=2)
#print("class")



infot = mqttc.publish("robothand", jsonVar, qos=2)

infot.wait_for_publish()