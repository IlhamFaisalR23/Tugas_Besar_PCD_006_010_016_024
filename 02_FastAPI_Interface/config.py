from pynput.keyboard import Key, Controller

class GestureConfig:
    """Konfigurasi untuk deteksi"""
    
    # MediaPipe confidence thresholds
    HAND_DETECTION_CONFIDENCE = 0.7
    HAND_TRACKING_CONFIDENCE = 0.5
    POSE_DETECTION_CONFIDENCE = 0.7
    POSE_TRACKING_CONFIDENCE = 0.5
    
    # Gesture detection thresholds
    SHOOTING_WRIST_THRESHOLD = 0.6
    GRENADE_X_THRESHOLD = 0.7
    GRENADE_Y_THRESHOLD = 0.5
    RUNNING_X_THRESHOLD = 0.9
    JUMPING_Y_THRESHOLD = 0.3

class KeyBindings:
    """Key bindings untuk Metal Slug"""
    
    ACTION_KEYS = {
        "idle": None,      # No key press
        "turn_right": Key.right,        # Move forward
        "turn_left": Key.left,        # Move backward
        "turn_right_down": [Key.right, Key.down],        # Move forward while crouching
        "turn_left_down": [Key.left, Key.down],        # Move backward while crouching
        "run": Key.right,        # Move forward
        "backward": Key.left,    # Move backward
        "shoot": 'x',     # Shoot weapon
        "shoot_up": [Key.up, 'x'],
        "grenade": 's',    # Throw grenade
        "jump": 'z',       # Jump
        "crouch": Key.down       # Crouch
    }

class APIConfig:
    """Konfigurasi API"""
    
    HOST = "0.0.0.0"
    PORT = 8000
    CAMERA_INDEX = 0
    FPS = 30