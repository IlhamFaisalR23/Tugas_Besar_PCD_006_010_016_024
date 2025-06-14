from pynput.keyboard import Key, Controller
import time
from config import KeyBindings

class KeyboardController:
    def __init__(self):
        self.keyboard = Controller()
        self.current_action = "idle"
        self.key_pressed = []  # support multiple keys
        self.last_action_time = time.time()

    def execute_action(self, action):
        """Execute keyboard action based on gesture"""
        current_time = time.time()

        if current_time - self.last_action_time < 0.1:
            return

        if action != self.current_action:
            self._release_current_keys()
            self._press_action_keys(action)
            self.current_action = action
            self.last_action_time = current_time

    def _press_action_keys(self, action):
        """Press key(s) corresponding to action"""
        key_map = KeyBindings.ACTION_KEYS

        if action in key_map:
            keys = key_map[action]
            if not isinstance(keys, list):
                keys = [keys]  # convert to list if single key

            try:
                for key in keys:
                    self.keyboard.press(key)
                    print(f"Pressed: {key}")
                self.key_pressed = keys
            except Exception as e:
                print(f"Error pressing keys {keys}: {e}")

    def _release_current_keys(self):
        """Release currently pressed key(s)"""
        if self.key_pressed:
            try:
                for key in self.key_pressed:
                    self.keyboard.release(key)
                    print(f"Released: {key}")
                self.key_pressed = []
            except Exception as e:
                print(f"Error releasing keys: {e}")

    def release_all_keys(self):
        """Release all keys when stopping"""
        self._release_current_keys()
        self.current_action = "idle"
