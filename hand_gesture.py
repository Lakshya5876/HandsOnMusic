import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
cap = cv2.VideoCapture(0)

prev_play_pause = False
prev_next = False
prev_prev = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    height, width, _ = frame.shape

    if result.multi_hand_landmarks and len(result.multi_hand_landmarks) == 1:  # Ensure only one hand is detected
        hand_landmarks = result.multi_hand_landmarks[0]
        bbox_x = [lm.x for lm in hand_landmarks.landmark]
        bbox_y = [lm.y for lm in hand_landmarks.landmark]
        x_min, x_max = min(bbox_x) * width, max(bbox_x) * width
        y_min, y_max = min(bbox_y) * height, max(bbox_y) * height

        cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        little_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

        # Closed fist detection for Play/Pause
        fist_closed = all(
            hand_landmarks.landmark[i].y > hand_landmarks.landmark[i - 2].y
            for i in [8, 12, 16, 20]
        )

        if fist_closed and not prev_play_pause:
            pyautogui.press('playpause')
            prev_play_pause = True
        elif not fist_closed:
            prev_play_pause = False

        # Index finger touching thumb for Next
        next_track = abs(index_tip.x - thumb_tip.x) < 0.05 and abs(index_tip.y - thumb_tip.y) < 0.05
        if next_track and not prev_next:
            pyautogui.press('nexttrack')
            prev_next = True
        elif not next_track:
            prev_next = False

        # Little finger touching thumb for Previous
        prev_track = abs(little_tip.x - thumb_tip.x) < 0.05 and abs(little_tip.y - thumb_tip.y) < 0.05
        if prev_track and not prev_prev:
            pyautogui.press('prevtrack')
            prev_prev = True
        elif not prev_track:
            prev_prev = False

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
