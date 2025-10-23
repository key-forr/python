import cv2
import random

image_path = "images/multiple-2.jpg"  

image = cv2.imread(image_path)

if image is None:
    print(f"Помилка: не вдалося завантажити зображення з {image_path}")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

print(f"Знайдено облич: {len(faces)}")

if len(faces) > 0:
    for i, (x, y, w, h) in enumerate(faces, 1):
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        
        cv2.putText(image, f"#{i}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        
        print(f"Обличчя #{i}: позиція ({x}, {y}), розмір {w}x{h}, колір {color}")
else:
    print("Обличчя не знайдено!")

cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()