# AI Virtual Mouse 🖱️

AI Virtual Mouse is a computer vision–based project that allows users to control
the mouse cursor using hand gestures captured through a webcam. It uses real-time
hand tracking to move the cursor and perform click actions without any physical mouse.

---

## 🚀 Features
- Real-time hand detection and tracking
- Mouse cursor movement using index finger
- Click actions using hand gestures
- Smooth and responsive control
- No external hardware required

---

## 🛠️ Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI

---

## 📋 Requirements
- Python 3.8 or above
- Webcam
- Supported OS: Windows / Linux / macOS

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/JASH-SHAH2606/AI-Virtual-Mouse.git
```

### 2. Navigate to the project directory
```bash
cd AI-Virtual-Mouse
```

### 3. Create a virtual environment
```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 5. Install dependencies
```bash
pip install -r requirements.txt
```
### 6. Run the Project
```bash
python AiVirtualMouseProject.py
```
---


## 🖐️ How It Works
- Webcam captures real-time video
- MediaPipe detects hand landmarks
- Index finger movement controls the cursor
- Hand gestures perform mouse click actions

---

## 📁 Project Structure
```text
AI Virtual Mouse/
├── AiVirtualMouseProject.py
├── HandTrackingModule.py
├── requirements.txt
└── README.md
```

---

## ⚠️ Notes
- Ensure your webcam is connected and working
- Good lighting improves hand detection accuracy
- Close other applications using the webcam

---

## 👨‍💻 Author
**Jash Shah**

---

