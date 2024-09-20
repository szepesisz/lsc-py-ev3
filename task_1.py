
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import sys

from umqtt.robust import MQTTClient



client = MQTTClient('asd', '192.168.0.123')
client.connect()

print(sys.version)

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
test_motor = Motor(Port.B)

# Write your program here

# Play a sound.
# ev3.speaker.beep()

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
test_motor.run_angle(rotation_angle=90, speed=360)

test_motor.run_angle(rotation_angle=90, speed=-360)

# Play another beep sound.