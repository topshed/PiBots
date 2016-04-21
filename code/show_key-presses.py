from evdev import InputDevice, ecodes, list_devices, categorize

for x in list_devices(): # List all devices attached to Pi
    dev = InputDevice(x)
    if dev.name == " Mini Keyboard" and dev.phys[-6:] == "input0":
        print("found") # If this is the deviec we're looking for...
        controller = dev # set it to be our controller

for event in controller.read_loop(): # look at every event from that device
    if event.type == ecodes.EV_KEY: # if it is a key-press
        print(categorize(event)) # print what it is
