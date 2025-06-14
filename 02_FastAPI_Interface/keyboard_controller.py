from pynput.keyboard import Key, Controller
import time
from config import KeyBindings

class KeyboardController:
    def __init__(self):
        self.keyboard = Controller()
        self.current_action = "idle"
        self.key_pressed = []
        self.last_action_time = time.time()

    def execute_action(self, action):
        current_time = time.time()

        # Special case for repeated shoot presses
        if action == "shoot":
            if current_time - self.last_action_time >= 0.15:  # spam every 150ms
                self._tap_key('x')
                self.last_action_time = current_time
            return

        # Normal behavior for other actions
        if current_time - self.last_action_time < 0.1:
            return

        if action != self.current_action:
            self._release_current_keys()
            self._press_action_keys(action)
            self.current_action = action
            self.last_action_time = current_time

    def _tap_key(self, key):
        """Tap a key (press + release quickly)"""
        try:
            self.keyboard.press(key)
            time.sleep(0.02)  # short hold
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
                    print(f"Pressed: {key}")
                self.key_pressed = keys
            except Exception as e:
                print(f"Error pressing keys {keys}: {e}")

    def _release_current_keys(self):
        if self.key_pressed:
            try:
                for key in self.key_pressed:
                    self.keyboard.release(key)
                    print(f"Released: {key}")
                self.key_pressed = []
            except Exception as e:
                print(f"Error releasing keys: {e}")

    def release_all_keys(self):
        self._release_current_keys()
        self.current_action = "idle"
