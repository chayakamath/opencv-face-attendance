import cv2
import os
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}
label_count = 0

for file in os.listdir("dataset"):
    path = os.path.join("dataset", file)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    name = file.split('_')[0]

    if name not in label_map:
        label_map[name] = label_count
        label_count += 1

    faces.append(img)
    labels.append(label_map[name])

recognizer.train(faces, np.array(labels))
recognizer.save("trainer.yml")

with open("labels.txt", "w") as f:
    for name, label in label_map.items():
        f.write(f"{label}:{name}\n")

print("Training complete.")
