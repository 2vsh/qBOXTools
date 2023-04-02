from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard_controller = Controller()

def on_press(key):
    try:
        if key == Key.up:
            keyboard_controller.release(Key.up)
            keyboard_controller.press('w')
        elif key == Key.down:
            keyboard_controller.release(Key.down)
            keyboard_controller.press('s')
        elif key == Key.left:
            keyboard_controller.release(Key.left)
            keyboard_controller.press('a')
        elif key == Key.right:
            keyboard_controller.release(Key.right)
            keyboard_controller.press('d')
    except AttributeError:
        pass

def on_release(key):
    if key == Key.up:
        keyboard_controller.release('w')
    elif key == Key.down:
        keyboard_controller.release('s')
    elif key == Key.left:
        keyboard_controller.release('a')
    elif key == Key.right:
        keyboard_controller.release('d')

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
