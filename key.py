import keyboard

keyboard.add_hotkey('ctrl + shift + a', print, args =('you entered', 'hotkey'))
  

keyboard.wait('ctrl + c')
keyboard.write('The quick brown fox jumps over the lazy dog.')


