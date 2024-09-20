from ev3dev2.sound import Sound

import paho.mqtt.client as mc

sound = Sound()
sound.speak('Hello world!')