# 🎯 Face Direction Tracker

A Python project that uses **OpenCV** to detect a face in real time and track its movement direction (Left, Right, Up, Down) with smoothed speed estimation.  
The system calculates how fast and in which direction the face moves between frames, displaying this information directly on the live video feed.

---

## 🚀 Features
- Real-time face detection using OpenCV Haar Cascade  
- Tracks face movement direction (Up, Down, Left, Right)  
- Calculates motion speed (in pixels per second)  
- Smoothed and stable readings — no jitter or flicker  
- Displays bounding box, direction, and speed overlay on video  

---

## 🧠 How It Works
1. The camera feed is captured using OpenCV.  
2. A Haar Cascade model detects the face region.  
3. The program computes the **center (cx, cy)** of the detected face.  
4. Movement between consecutive frames is analyzed to determine direction.  
5. Speed (in pixels/second) is calculated based on distance and time difference.  
6. Small jitters are ignored and readings are stabilized using smoothing buffers.

---

## 🧩 Requirements
Make sure you have Python **3.8–3.12** (OpenCV may not yet fully support 3.13).  
Install dependencies:
```bash
pip install opencv-python
```

Optional (for advanced features):
```bash
pip install opencv-contrib-python
```

---

## ▶️ Usage
1. Clone or download this repository.  
2. Run the Python script:
```bash
python face_tracker.py
```
3. The webcam will open and display a live video feed.  
4. Move your face around — the app will show **direction** and **speed**.  
5. Press **‘q’** to quit.

---

## 📸 Example Output
- A **green bounding box** surrounds the detected face.  
- **Direction** and **speed** are displayed on the video window.  
- Movements smaller than a threshold are ignored for stability.

---

## 🧰 File Structure
```
Face-Direction-Tracker/
│
├── face_tracker.py      # Main Python script
├── README.md            # Project documentation
└── requirements.txt     # (Optional) List of dependencies
```

---

## ⚙️ Future Improvements
- Support for multiple faces  
- Integration with Arduino for motor or servo control  
- Face tracking with DNN-based detector for higher accuracy  

---

## 👨‍💻 Author
**Your Name Here**  
📧 Email: your.email@example.com  
🌐 GitHub: [https://github.com/yourusername](https://github.com/yourusername)

---

### 🧠 Description for GitHub:
> A real-time face movement tracker built with OpenCV that detects face position, calculates direction and speed, and displays it with smooth and stable visuals.
