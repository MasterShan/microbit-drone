import microbit
import radio

radio.on()
radio.config(channel=10)

height = 1

display_left = '00000:09900:00000'
display_right = '00000:00990:00000'
display_up = '00900:00900:00000'
display_down = '00000:00900:00900'
display_none = '00000:00900:00000'

display_rcv = '00009'
display_floor = '00000'
last = False

def gesture():
    return microbit.accelerometer.current_gesture()

def bar(arg):
    if arg == 1:
        return '90000'
    elif arg == 2:
        return '99000'
    elif arg == 3:
        return '99900'
    elif arg == 4:
        return '99990'
    elif arg == 5:
        return '99999'
    else:
        return '00000'

def disp(gesture, height, floor):
    if gesture == 'up':
        return height + ":" + display_down + ":" + floor
    elif gesture == 'down':
        return height + ":" + display_up + ":" + floor
    elif gesture == 'right':
        return height + ":" + display_right + ":" + floor
    elif gesture == 'left':
        return height + ":" + display_left + ":" + floor
    else:
        return height + ":" + display_none + ":" + floor

while True:
    if microbit.button_b.was_pressed():
        if height < 5:
            height += 1

    if microbit.button_a.was_pressed():
        if height > 1:
            height -= 1

    res = radio.receive()
    direction = gesture()
    top = bar(height)

    if res is 'rcv':
        if last is False:
            face = disp(direction, top, display_rcv)
            last = True
        elif last is True:
            face = disp(direction, top, display_floor)
            last = False
    else:
        face = disp(direction, top, display_floor)

    microbit.display.show(microbit.Image(face))
    radio.send(face)
