class GestureConfig:
    """Configuration for gesture detection"""
    
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
    """Key bindings for Metal Slug actions"""
    
    ACTION_KEYS = {
        "idle": None,      # No key press
        "run": 'd',        # Move forward
        "shoot": 'j',      # Shoot weapon
        "grenade": 'l',    # Throw grenade
        "jump": 'k'        # Jump
    }

class APIConfig:
    """API configuration"""
    
    HOST = "0.0.0.0"
    PORT = 8000
    CAMERA_INDEX = 0
    FPS = 60