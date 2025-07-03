# opencv-face-attendance

# 🎯 Face Attendance System using Face Recognition

A real-time Face Recognition Attendance System built with Python, OpenCV, SQLite, and Streamlit.  
This system detects and recognizes faces from webcam input, marks attendance into a local database, and provides a user-friendly dashboard to view/export attendance records.

---

## 📌 Features

- 🧑‍💼 Register new faces using webcam
- 🧠 Train model using LBPH algorithm (OpenCV)
- 📸 Recognize and mark attendance in real-time
- 💾 Attendance stored in SQLite database
- 📊 Export daily attendance as CSV
- 🌐 Web dashboard using Streamlit

---

## 🧠 Tech Stack

- **Python**
- **OpenCV** (with contrib module)
- **SQLite3**
- **Streamlit**
- **dlib** (indirectly for `face_recognition`)

---

## 📁 Folder Structure

📂 face-attendance-system-python/
├── register_face.py # Register new user's face via webcam
├── train_model.py # Train the model on collected faces
├── recognize_and_mark.py # Detect and mark attendance
├── export_attendance.py # Export attendance to CSV
├── streamlit_ui.py # Streamlit dashboard
├── requirements.txt # All dependencies
├── dataset/ # Face images of users
├── trainer.yml # Trained model file
├── attendance.db # SQLite database
└── attendance/ # (Optional) CSV exports


---

## 🚀 How to Run

### 1. Clone the Repository

bash
git clone https://github.com/chayakamath/opencv-face-attendance
cd face-attendance-system-python

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # for Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Register Face
python register_face.py

### 5. Train Model
python train_model.py

### 6. Run Recognition and Mark Attendance
python recognize_and_mark.py


### 7. Export Attendance as CSV
python export_attendance.py

### 8. Web Dashboard
streamlit run streamlit_ui.py


