import cv2
import mediapipe as mp
import numpy as np
from config import GestureConfig

class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
    def detect_gesture(self, frame):
        """Detect gesture from frame and return action"""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Get hand and pose results
        hand_results = self.hands.process(rgb_frame)
        pose_results = self.pose.process(rgb_frame)
        
        # Draw annotations
        annotated_frame = frame.copy()
        
        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    annotated_frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        
        if pose_results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                annotated_frame, pose_results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        
        # Analyze gesture and determine action
        action = self._analyze_gesture(hand_results, pose_results, frame.shape)
        
        # Display current action on frame
        cv2.putText(annotated_frame, f"Action: {action}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        return action, annotated_frame
    
    def _analyze_gesture(self, hand_results, pose_results, frame_shape):
        """Analyze landmarks to determine gesture"""
        h, w = frame_shape[:2]
        
        # Default action
        action = "idle"
        
        # Check for hand gestures
        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark
                
                # Get key points
                wrist = landmarks[0]
                thumb_tip = landmarks[4]
                index_tip = landmarks[8]
                middle_tip = landmarks[12]
                ring_tip = landmarks[16]
                pinky_tip = landmarks[20]
                
                # Convert to pixel coordinates
                wrist_pos = (int(wrist.x * w), int(wrist.y * h))
                thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))
                index_pos = (int(index_tip.x * w), int(index_tip.y * h))
                middle_pos = (int(middle_tip.x * w), int(middle_tip.y * h))
                
                # Gesture detection logic
                # Shoot gesture: Hand raised like holding a gun
                if self._is_shooting_gesture(landmarks, w, h):
                    action = "shoot"
                # Grenade gesture: Hand behind back motion
                elif self._is_grenade_gesture(landmarks, w, h):
                    action = "grenade"
                # Run gesture: Hand moving forward
                elif self._is_running_gesture(landmarks, w, h):
                    action = "run"
                # Backward gesture: Hand on right side and lower/middle height
                elif self._is_backward_gesture(landmarks, w, h):
                    action = "backward"
        
        # Check for pose gestures (jumping and crouching)
        if pose_results.pose_landmarks:
            landmarks = pose_results.pose_landmarks.landmark
            if self._is_jumping_gesture(landmarks, w, h):
                action = "jump"
            elif self._is_turning_right_down_gesture(landmarks, w, h):
                action = "turn_right_down"
            elif self._is_turning_left_down_gesture(landmarks, w, h):
                action = "turn_left_down"
            elif self._is_turning_left_gesture(landmarks, w, h):
                action = "turn_left"
            elif self._is_turning_right_gesture(landmarks, w, h):
                action = "turn_right"
            elif self._is_head_down_gesture(pose_results.pose_landmarks.landmark, w, h):
                action = "crouch"
        
        return action
    
    def _is_shooting_gesture(self, landmarks, w, h):
        """Detect shooting gesture - hand raised like holding weapon"""
        wrist = landmarks[0]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        
        # Hand should be raised (wrist higher than usual)
        # Index finger extended, other fingers curled
        wrist_y = wrist.y * h
        index_y = index_tip.y * h
        middle_y = middle_tip.y * h
        
        # Check if hand is raised and fingers are in gun position
        if wrist_y < h * 0.6 and index_y < wrist_y and abs(index_y - middle_y) > 20:
            return True
        return False
    
    def _is_turning_left_gesture(self, pose_landmarks, w, h):
        """Detect if head is turned 45 degrees to the left"""
        nose = pose_landmarks[0]
        left_ear = pose_landmarks[7]
        right_ear = pose_landmarks[8]

        # Hitung posisi piksel
        nose_x = nose.x * w
        left_ear_x = left_ear.x * w
        right_ear_x = right_ear.x * w

        # Hitung jarak hidung ke masing-masing telinga
        dist_left = abs(nose_x - left_ear_x)
        dist_right = abs(nose_x - right_ear_x)

        # Jika hidung lebih dekat ke telinga kanan daripada telinga kiri,
        # maka kemungkinan menengok ke kiri
        if dist_right < dist_left * 0.5:
            return True
        return False
    
    def _is_turning_right_gesture(self, pose_landmarks, w, h):
        """Detect if head is turned 45 degrees to the right"""
        nose = pose_landmarks[0]
        left_ear = pose_landmarks[7]
        right_ear = pose_landmarks[8]

        # Hitung posisi piksel
        nose_x = nose.x * w
        left_ear_x = left_ear.x * w
        right_ear_x = right_ear.x * w

        # Hitung jarak hidung ke masing-masing telinga
        dist_left = abs(nose_x - left_ear_x)
        dist_right = abs(nose_x - right_ear_x)

        # Jika hidung lebih dekat ke telinga kiri daripada telinga kanan,
        # maka kemungkinan menengok ke kanan
        if dist_left < dist_right * 0.5:
            return True
        return False
    
    def _is_turning_right_down_gesture(self, pose_landmarks, w, h):
        """Detect if head is turned to the right and slightly downward"""
        nose = pose_landmarks[0]
        left_ear = pose_landmarks[7]
        right_ear = pose_landmarks[8]

        # Koordinat piksel
        nose_x = nose.x * w
        nose_y = nose.y * h
        left_ear_x = left_ear.x * w
        right_ear_x = right_ear.x * w
        left_ear_y = left_ear.y * h
        right_ear_y = right_ear.y * h

        # Deteksi arah kanan
        dist_left = abs(nose_x - left_ear_x)
        dist_right = abs(nose_x - right_ear_x)
        looking_right = dist_left < dist_right * 0.5

        # Deteksi arah bawah (dari posisi hidung terhadap rata-rata telinga)
        ear_avg_y = (left_ear_y + right_ear_y) / 2
        looking_down = nose_y > ear_avg_y + (h * 0.03)

        return looking_right and looking_down


    def _is_turning_left_down_gesture(self, pose_landmarks, w, h):
        """Detect if head is turned to the left and slightly downward"""
        nose = pose_landmarks[0]
        left_ear = pose_landmarks[7]
        right_ear = pose_landmarks[8]

        # Koordinat piksel
        nose_x = nose.x * w
        nose_y = nose.y * h
        left_ear_x = left_ear.x * w
        right_ear_x = right_ear.x * w
        left_ear_y = left_ear.y * h
        right_ear_y = right_ear.y * h

        # Deteksi arah kiri
        dist_left = abs(nose_x - left_ear_x)
        dist_right = abs(nose_x - right_ear_x)
        looking_left = dist_right < dist_left * 0.5

        # Deteksi arah bawah
        ear_avg_y = (left_ear_y + right_ear_y) / 2
        looking_down = nose_y > ear_avg_y + 10  # offset toleransi

        return looking_left and looking_down

    
    def _is_grenade_gesture(self, landmarks, w, h):
        """Detect grenade throwing gesture"""
        wrist = landmarks[0]
        thumb_tip = landmarks[4]
        
        # Hand should be in throwing position (behind and then forward)
        wrist_x = wrist.x * w
        wrist_y = wrist.y * h
        
        # Simple detection: hand on the right side and elevated
        if wrist_x > w * 0.7 and wrist_y < h * 0.5:
            return True
        return False
    
    def _is_running_gesture(self, landmarks, w, h):
        """Detect running gesture - hand moving forward"""
        wrist = landmarks[0]
        
        # Hand extended forward
        wrist_x = wrist.x * w
        if wrist_x < w * 0.3:  # Hand on left side (forward in mirror)
            return True
        return False
    
    def _is_backward_gesture(self, landmarks, w, h):
        """Detect backward movement gesture"""
        wrist = landmarks[0]
        
        # Hand on right side of screen and lower/middle height
        wrist_x = wrist.x * w
        wrist_y = wrist.y * h
        
        if wrist_x > w * 0.7 and wrist_y > h * 0.4 and wrist_y < h * 0.7:
            return True
        return False
    
    def _is_jumping_gesture(self, pose_landmarks, w, h):
        """Detect jumping gesture from pose"""
        if not pose_landmarks:
            return False
            
        # Get key pose points
        left_shoulder = pose_landmarks[11]
        right_shoulder = pose_landmarks[12]
        left_hip = pose_landmarks[23]
        right_hip = pose_landmarks[24]
        
        # Calculate average shoulder and hip heights
        shoulder_avg_y = (left_shoulder.y + right_shoulder.y) / 2 * h
        hip_avg_y = (left_hip.y + right_hip.y) / 2 * h
        
        # If arms are raised above shoulders (jumping motion)
        if shoulder_avg_y < h * 0.3:
            return True
        return False

    def _is_head_down_gesture(self, pose_landmarks, w, h):
        """Detect head down gesture (nodding)"""
        if not pose_landmarks:
            return False
            
        # Get key pose points for head
        nose = pose_landmarks[0]  # Landmark 0 is the nose
        left_ear = pose_landmarks[7]  # Landmark 7 is the left ear
        right_ear = pose_landmarks[8]  # Landmark 8 is the right ear
        
        # Calculate average ear height
        ear_avg_y = (left_ear.y + right_ear.y) / 2 * h
        nose_y = nose.y * h
        
        # If nose is below the ears (head is down)
        if nose_y > ear_avg_y + 20:  # Threshold of 20 pixels
            return True
        return False