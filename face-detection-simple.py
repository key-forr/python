import cv2

image_path = "/home/rotory-ken/Pictures/ddayeena&key.forr1/5460845957185930789.jpg"  

image = cv2.imread(image_path)

if image is None:
    print(f"Помилка: не вдалося завантажити зображення з {image_path}")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)


if len(faces) > 0:
    largest_face = max(faces, key=lambda face: face[2] * face[3])
    x, y, w, h = largest_face
    
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow("Detected Face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()