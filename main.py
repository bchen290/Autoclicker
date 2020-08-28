import time

import mouse
import keyboard

# Settings
delay = 1
toggle_pause_key = 'f6'
exit_key = 'esc'


running = True
pause = True


def stop():
    global running
    running = False


def toggle_pause():
    global pause
    print("Is paused: " + str(not pause))
    pause = not pause


if __name__ == '__main__':
    keyboard.add_hotkey(toggle_pause_key, toggle_pause)
    keyboard.add_hotkey(exit_key, stop)

    print('Started!')
    print('Press ' + toggle_pause_key + ' to start/pause')
    print('Press ' + exit_key + ' to exit')

    while running:
        if not pause:
            mouse.click(button='left')
            time.sleep(delay)
