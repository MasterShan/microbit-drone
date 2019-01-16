import microbit
import radio

radio.on()
radio.config(channel=10)

while True:
    signal = radio.receive()
    if signal is not None:
        microbit.display.show(microbit.Image(signal))
        radio.send('rcv');
        parts = signal.split(':')