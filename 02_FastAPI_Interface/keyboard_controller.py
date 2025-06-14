from pynput.keyboard import Key, Controller
import time
from config import KeyBindings

class KeyboardController:
    def __init__(self):
        self.keyboard = Controller()
        self.current_action = "idle"
        self.pressed_keys = set()  # Gunakan set untuk melacak tombol yang ditekan
        self.last_action_time = time.time()
        
    def execute_action(self, action):
        """Execute keyboard action based on gesture"""
        current_time = time.time()
        
        # Prevent too frequent key presses
        if current_time - self.last_action_time < 0.1:
            return
            
        # Jika aksi berubah, lepaskan tombol sebelumnya dan tekan tombol baru
        if action != self.current_action:
            self._release_all_keys()
            self._press_action_key(action)
            self.current_action = action
            self.last_action_time = current_time
    
    def _press_action_key(self, action):
        """Press key corresponding to action"""
        key_map = KeyBindings.ACTION_KEYS
        
        if action in key_map:
            key = key_map[action]
            try:
                # Tangani satu tombol
                if isinstance(key, (str, Key)):
                    self.keyboard.press(key)
                    self.pressed_keys.add(key)
                    print(f"Pressed: {key} for action: {action}")
                
                # Tangani kombinasi tombol
                elif isinstance(key, list):
                    for combo_key in key:
                        self.keyboard.press(combo_key)
                        self.pressed_keys.add(combo_key)
                    print(f"Pressed combination: {key} for action: {action}")
            except Exception as e:
                print(f"Error pressing key {key}: {e}")
    
    def _release_all_keys(self):
        """Lepaskan semua tombol yang sedang ditekan"""
        for key in list(self.pressed_keys):
            try:
                self.keyboard.release(key)
                print(f"Released: {key}")
            except Exception as e:
                print(f"Error releasing key {key}: {e}")
        
        # Kosongkan set tombol yang ditekan
        self.pressed_keys.clear()
        self.current_action = "idle"
    
    def release_all_keys(self):
        """Release all keys when stopping"""
        self._release_all_keys()