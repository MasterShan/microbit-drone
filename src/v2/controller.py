from microbit import *
import radio

radio.on()
radio.config(channel=10)

height = 1

display_left = '00000:09900:00000'
display_right = '00000:00990:00000'
display_up = '00900:00900:00000'
display_down = '00000:00900:00900'
display_none = '00000:00900:00000'

display_floor = '00000'

def gesture():
    return accelerometer.current_gesture()

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

def disp(gesture, height):
    if gesture == 'up':
        return height + display_down + display_floor
    elif gesture == 'down':
        return height + display_up + display_floor
    elif gesture == 'right':
        return height + display_right + display_floor
    elif gesture == 'left':
        return height + display_left + display_floor
    else:
        return height + display_none + display_floor

while True:
    if button_a.was_pressed():
        if height < 5:
            height += 1

    if button_b.was_pressed():
        if height > 1:
            height -= 1

    direction = gesture()
    top = bar(height)
    face = disp(direction, top)

    radio.send(face)

    display.show(Image(face))
    sleep(100)
