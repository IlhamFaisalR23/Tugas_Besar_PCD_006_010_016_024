from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse, HTMLResponse
import cv2
import uvicorn
from gesture_detector import GestureDetector
from keyboard_controller import KeyboardController
import time
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os

templates = Jinja2Templates(directory="templates")

app = FastAPI(title="Metal Slug Gesture Controller")
gesture_detector = GestureDetector()
keyboard_controller = KeyboardController()

# Global variables
camera = None
is_running = False

def generate_frames():
    global camera, is_running
    camera = cv2.VideoCapture(0)
    
    while is_running:
        success, frame = camera.read()
        if not success:
            break
        
        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Detect gesture and get action
        action, annotated_frame = gesture_detector.detect_gesture(frame)
        
        # Execute keyboard action
        keyboard_controller.execute_action(action)
        
        # Encode frame
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
        time.sleep(0.03)  # ~30 FPS

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/start")
async def start_detection():
    global is_running
    is_running = True
    return {"status": "Detection started"}

@app.get("/stop")
async def stop_detection():
    global is_running, camera
    is_running = False
    if camera:
        camera.release()
    keyboard_controller.release_all_keys()
    return {"status": "Detection stopped"}

@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/gestures")
async def get_gestures():
    return {
        "gestures": {
            "idle": "Diam - tidak menekan apapun",
            "run": "Gerakan tangan ke kiri layar - tombol Panah Kanan",
            "backward": "Menoleh ke kiri - tombol Panah Kiri", 
            "shoot": "Tangan diangkat dengan jari telunjuk lurus - tombol X", 
            "shoot_up": "Tangan diangkat tinggi dengan jari telunjuk ke atas - Panah Atas + X",
            "grenade": "Tangan di belakang - tombol S",
            "jump": "Tangan diangkat tinggi - tombol Z",
            "crouch": "Tangan di bagian bawah layar - tombol Panah Bawah"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)