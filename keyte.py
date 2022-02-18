import keyboard
import sys


def asd(y:int):
    print(f"the number is {y}")
def quit():
    try:
       print("sd") 
    except KeyboardInterrupt:
       print("bey")
    


keyboard.add_hotkey('e',print, args=("ret",""))


keyboard.add_hotkey('ctrl+shift+a', print, args=('footer', 'fg'))

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('a',lambda: asd(7))
#ekeyboard.add_hotkey('ctrl + c',quit)

# Block forever, like `while True`.
keyboard.wait('ctrl+c')