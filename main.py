from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(48, Pin.OUT)   
np = NeoPixel(pin, 1)   
np[0] = (10,0,0) 
np.write()              
r, g, b = np[0]

print("RGB Demo")

while True:

    print("50%R")
    np[0] = (127, 0, 0)
    np.write()
    time.sleep_ms(1000)
    
    print("50%G")
    np[0] = (0, 127, 0)
    np.write()
    time.sleep_ms(1000)

    print("50%B")
    np[0] = (0, 0, 127)
    np.write()
    time.sleep_ms(1000)