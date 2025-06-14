# Metal Slug Gesture Controller

Control Metal Slug game using hand gestures and body movements detected by MediaPipe.

## Features
- Real-time gesture detection using MediaPipe
- FastAPI web interface with live video feed
- Keyboard automation for game control
- Support for 5 different gestures/actions

## Gestures
- **Idle**: No movement - no key press
- **Run**: Hand forward - 'Right Arrow' key (move forward)
- **Shoot**: Hand raised like holding weapon - 'X' key
- **Grenade**: Hand behind back throwing motion - 'S' key  
- **Jump**: Arms raised - 'Z' key

## Instalasi
Klone repositori ini
```bash
git clone https://github.com/IlhamFaisalR23/Tugas_Besar_PCD_QuadroPipe-006_010_016_024.git
```
Pindah ke direktori hasil clone repositori
```bash
cd Tugas_Besar_PCD_QuadroPipe-006_010_016_024
```
Pindah ke direktori yang berisikan aplikasi utama
```bash
cd 02_FastAPI_Interface
```
OPTIONAL : Gunakan Virtual Environment lalu lakukan
instalasi modul modul dari requirements.txt
```bash
pip install -r requirements.txt
```
Jalankan aplikasi utama
```bash
python main.py
```