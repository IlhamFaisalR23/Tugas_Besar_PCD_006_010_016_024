from pynput.keyboard import Key, Controller
import time
from config import KeyBindings

class KeyboardController:
    def __init__(self):
        self.keyboard = Controller()
        self.current_action = "idle"
        self.key_pressed = None
        self.last_action_time = time.time()
        
    def execute_action(self, action):
        """Execute keyboard action based on gesture"""
        current_time = time.time()
        
        # Prevent too frequent key presses
        if current_time - self.last_action_time < 0.1:
            return
            
        # If action changed, release previous key and press new one
        if action != self.current_action:
            self._release_current_key()
            self._press_action_key(action)
            self.current_action = action
            self.last_action_time = current_time
    
    def _press_action_key(self, action):
        """Press key corresponding to action"""
        key_map = KeyBindings.ACTION_KEYS
        
        if action in key_map:
            key = key_map[action]
            try:
                self.keyboard.press(key)
                self.key_pressed = key
                print(f"Pressed: {key} for action: {action}")
            except Exception as e:
                print(f"Error pressing key {key}: {e}")
    
    def _release_current_key(self):
        """Release currently pressed key"""
        if self.key_pressed:
            try:
                self.keyboard.release(self.key_pressed)
                print(f"Released: {self.key_pressed}")
                self.key_pressed = None
            except Exception as e:
                print(f"Error releasing key: {e}")
    
    def release_all_keys(self):
        """Release all keys when stopping"""
        self._release_current_key()
        self.current_action = "idle"