# Add your Python code here. E.g.
from microbit import *
import radio

radio.on();
radio.config(channel=18)

while True:
    signal = radio.receive();
    if signal is not None:
        display.show(Image(signal))
        sleep(100);
