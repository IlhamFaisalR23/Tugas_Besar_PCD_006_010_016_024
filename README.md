# Metal Slug Gesture Controller

Control Metal Slug game using hand gestures and body movements detected by MediaPipe.

## Features
- Real-time gesture detection using MediaPipe
- FastAPI web interface with live video feed
- Keyboard automation for game control
- Support for 5 different gestures/actions

## Gestures
- **Idle**: No movement - no key press
- **Run**: Hand forward - 'D' key (move forward)
- **Shoot**: Hand raised like holding weapon - 'J' key
- **Grenade**: Hand behind back throwing motion - 'L' key  
- **Jump**: Arms raised - 'K' key

## Installation
```bash
cd 02_FastAPI_Interface
```
```bash
pip install -r requirements.txt
```
```bash
python main.py
```