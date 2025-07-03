import cv2
import sqlite3
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {}
with open("labels.txt", "r") as f:
    for line in f:
        label, name = line.strip().split(":")
        labels[int(label)] = name

# Create DB
conn = sqlite3.connect('attendance.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS attendance (name TEXT, date TEXT, time TEXT)''')
conn.commit()

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(roi)

        if confidence < 70:  # confidence threshold (lower = better)
            name = labels[label]
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            now = datetime.now()
            date, time = now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")

            # Check if already marked
            c.execute("SELECT * FROM attendance WHERE name=? AND date=?", (name, date))
            if c.fetchone() is None:
                c.execute("INSERT INTO attendance VALUES (?, ?, ?)", (name, date, time))
                conn.commit()
                print(f"Attendance marked for {name} at {time}")
        else:
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('Attendance System', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
conn.close()
