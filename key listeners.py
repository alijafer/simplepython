from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
  
    try:
       c = key.char  # single-char keys
    except:
        c = key.name  # other keys
    if c in ['1', '2', 'left', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + c)
        return False  # stop listener; remove this if want more keys

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
