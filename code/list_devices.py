from evdev import InputDevice, ecodes, list_devices, categorize

for x in list_devices(): # List all devices attached to Pi
    print(InputDevice(x)) # Print out info about it
