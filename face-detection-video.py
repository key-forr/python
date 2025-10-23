import cv2
import random

print("Виберіть джерело:")
print("1 - Вебкамера")
print("2 - Відеофайл (videos/people-2.mp4)")
choice = input("Ваш вибір (1/2): ")

if choice == "1":
    video_source = 0
    print("Використовується вебкамера...")
elif choice == "2":
    video_source = "videos/people-2.mp4"
    print(f"Використовується відеофайл: {video_source}")
else:
    print("Невірний вибір!")
    exit()

cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print(f"Помилка: не вдалося відкрити відео '{video_source}'")
    print("Перевірте, чи існує файл та чи правильний шлях")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

display_width = 800  

print("Натисніть 'q' для виходу")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Кінець відео або помилка читання кадру")
        break
    
    original_height, original_width = frame.shape[:2]
    
    aspect_ratio = original_height / original_width
    display_height = int(display_width * aspect_ratio)
    
    frame = cv2.resize(frame, (display_width, display_height))
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for i, (x, y, w, h) in enumerate(faces, 1):
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, f"Face #{i}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Face Detection - Video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Звільняємо ресурси
cap.release()
cv2.destroyAllWindows()
print("Завершено")