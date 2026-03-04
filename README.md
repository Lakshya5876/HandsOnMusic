# HandsOnMusic

## Overview
A gesture-controlled music player that uses real-time hand tracking with OpenCV and MediaPipe. Control your music playback with intuitive hand gestures - play, pause, skip, and rewind tracks effortlessly without touching any device.

## Tech Stack
- Python
- OpenCV (computer vision)
- MediaPipe (hand tracking)
- PyAutoGUI (keyboard automation)
- NumPy (numerical computations)

## Features
- Real-time hand gesture recognition
- Play/Pause control with gestures
- Skip to next track gesture
- Rewind to previous track gesture
- Volume control with hand positioning
- Smooth gesture detection
- Support for all major media players
- Adjustable sensitivity settings
- Visual feedback for recognized gestures

## Architecture
Request flow:
1. Webcam captures video frames in real-time
2. OpenCV processes and prepares frames
3. MediaPipe detects hand positions and landmarks
4. GestureRecognizer analyzes hand position and movement
5. Gesture is matched against predefined patterns
6. PyAutoGUI sends corresponding keyboard commands to media player
7. Visual feedback is displayed to user
8. Loop continues for continuous gesture detection

## How to Run
1. Clone the repository: `git clone https://github.com/Lakshya5876/HandsOnMusic.git`
2. Navigate to project: `cd HandsOnMusic`
3. Install dependencies:
   ```bash
   pip install opencv-python mediapipe pyautogui numpy
   ```
4. Run the application:
   ```bash
   python main.py
   ```
5. Ensure your webcam is working and properly positioned
6. Open your favorite media player (Spotify, YouTube, VLC, etc.)
7. Perform hand gestures in front of the camera

## Gesture Controls
```
Thumbs Up: Play/Pause
Victory Sign (two fingers): Next Track
Fist: Previous Track
Open Palm: Increase Volume
Closed Fist: Decrease Volume
Pointing Finger: Seek Forward
```