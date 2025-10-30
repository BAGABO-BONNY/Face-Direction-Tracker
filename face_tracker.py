import cv2
import time
import math
from collections import deque

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture
cap = cv2.VideoCapture(0)

prev_cx, prev_cy = None, None
prev_time = time.time()
direction = "Center"
speed = 0.0

# --- Parameters ---
MOVEMENT_THRESHOLD = 10        # pixels (ignore jitter)
SPEED_SMOOTHING = 5            # number of frames for smoothing
DIRECTION_STABILITY = 3        # consecutive frames to confirm new direction

# --- Buffers for smoothing ---
speed_buffer = deque(maxlen=SPEED_SMOOTHING)
direction_buffer = deque(maxlen=DIRECTION_STABILITY)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cx = x + w // 2
        cy = y + h // 2

        # Draw face box and center
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

        if prev_cx is not None and prev_cy is not None:
            dx = cx - prev_cx
            dy = cy - prev_cy
            dist = math.sqrt(dx**2 + dy**2)

            # Ignore very small movements
            if dist > MOVEMENT_THRESHOLD:
                # Compute direction
                if abs(dx) > abs(dy):
                    new_dir = "Right" if dx > 0 else "Left"
                else:
                    new_dir = "Down" if dy > 0 else "Up"

                direction_buffer.append(new_dir)
                # Only update direction when consistent
                if len(direction_buffer) == DIRECTION_STABILITY and len(set(direction_buffer)) == 1:
                    direction = direction_buffer[-1]
                    direction_buffer.clear()

                # Calculate smoothed speed
                current_time = time.time()
                time_diff = current_time - prev_time
                if time_diff > 0:
                    current_speed = dist / time_diff
                    speed_buffer.append(current_speed)
                    speed = sum(speed_buffer) / len(speed_buffer)
                prev_time = current_time

        prev_cx, prev_cy = cx, cy

        # Display text
        cv2.putText(frame, f"Direction: {direction}", (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Speed: {speed:.2f}px/s", (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Face Direction Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
