from microbit import *
import radio

radio.on()
radio.config(channel=10)

while True:
    signal = radio.receive()
    if signal is not None:
        display.show(Image(signal))
        
        parts = signal.split(':')