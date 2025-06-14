from pynput.keyboard import Key, Controller
import time
from config import KeyBindings

class KeyboardController:
    def __init__(self):
        self.keyboard = Controller()
        self.current_action = "idle"
        self.key_pressed = []
        self.pressed_keys = set()
        self.last_action_time = time.time()

    def execute_action(self, action):
        current_time = time.time()

        if action == "shoot":
            if current_time - self.last_action_time >= 0.15:
                self._tap_key('x')
                self.last_action_time = current_time
            return

        if current_time - self.last_action_time < 0.1:
            return

        if action != self.current_action:
            self._release_all_keys()
            self._press_action_keys(action)
            self.current_action = action
            self.last_action_time = current_time

    def _tap_key(self, key):
        try:
            self.keyboard.press(key)
            time.sleep(0.02)
            self.keyboard.release(key)
            print(f"Tapped: {key}")
        except Exception as e:
            print(f"Error tapping key {key}: {e}")

    def _press_action_keys(self, action):
        key_map = KeyBindings.ACTION_KEYS
        if action in key_map:
            keys = key_map[action]
            if not isinstance(keys, list):
                keys = [keys]
            try:
                for key in keys:
                    self.keyboard.press(key)
                    self.pressed_keys.add(key)
                    print(f"Pressed: {key} for action: {action}")
            except Exception as e:
                print(f"Error pressing keys {keys}: {e}")

    def _release_all_keys(self):
        for key in list(self.pressed_keys):
            try:
                self.keyboard.release(key)
                print(f"Released: {key}")
            except Exception as e:
                print(f"Error releasing key {key}: {e}")
        self.pressed_keys.clear()
        self.current_action = "idle"

    def release_all_keys(self):
        self._release_all_keys()
