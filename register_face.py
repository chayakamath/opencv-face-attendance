import cv2
import os

name = input("Enter Name: ")

if not os.path.exists("dataset"):
    os.makedirs("dataset")

cam = cv2.VideoCapture(0)
img_count = 0

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture Face - Press 's' to Save, 'q' to Quit", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        img_path = f"dataset/{name}_{img_count}.jpg"
        cv2.imwrite(img_path, gray)
        print(f"Saved {img_path}")
        img_count += 1

    elif key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
