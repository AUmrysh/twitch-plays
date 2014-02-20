import sys

if sys.platform.startswith('win'):
    import win32api
    import win32con
if sys.platform.startswith('linux'):
    from predestinate import KeyGod

import time
from misc import pbutton

class Game:

    keymap = {
        'q':"q",
        'w':"w",
        'o':"o",
        'p':"p",
        'space':"space"
    }

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        try:
            return [self.keymap[button], 0.1]
        except KeyError:
            #try a command with a timing
            if len(button) is 2:
                try:
                    btnpart = str(button[:1])
                    numpart = int(button[1:])
                except ValueError:
                    return None
                if button[:1] in self.keymap and int(button[1:]) in xrange(1, 6):
                    return [self.keymap[btnpart], 0.1*numpart]

    def push_button(self, button):
        if sys.platform.startswith('win'):
            win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
            win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
        if sys.platform.startswith('linux'):
            btn = self.button_to_key(button)
            if btn is not None:
                pbutton(nick, btn)
                keypress(btn)

def keypress(seq):
    kg = KeyGod()
    kg.key_down(seq[0])
    time.sleep(seq[1])
    kg.key_up(seq[0])
