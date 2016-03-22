from gpiozero import Motor
from time import sleep
m1 = Motor(14,15)

speed = 0.5

m1.forward(speed)
sleep(1)
m1.stop()
speed = 1
m1.backward(speed)
sleep(1)
m1.stop()
