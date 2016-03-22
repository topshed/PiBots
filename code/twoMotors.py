from gpiozero import Motor
from time import sleep

m1 = Motor(14,15) # Set which GPIO pins the motor is using
m2 = Motor(23,24)

def drive_fwd(speed): # a functon to move both motors
    m1.forward(speed) 
    m2.forward(speed)

def all_stop(): # a function to stop both motors
    m1.stop()
    m2.stop()

drive_fwd(0.5) # Move forward at half speed
sleep(1)
all_stop() # STOP!
