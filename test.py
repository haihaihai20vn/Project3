import numpy as np
import cv2
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

path_train = "data/"
file = [f for f in listdir(path_train) if isfile(join(path_train, f))]

'''training_data, labels = [], []
for i, files in enumerate(file):
    train_image_path = path_train + file[i]
    images = cv2.imread(train_image_path, cv2.IMREAD_GRAYSCALE)
    training_data.append(np.asarray(images, dtype=np.uint8))
    labels.append(i)

labels = np.asarray(labels, dtype=np.int32)'''

model = cv2.face.LBPHFaceRecognizer_create()
#model.train(np.asarray(training_data), np.asarray(labels))
model.read("classifier.xml")
print("Model training complete")



cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is():
        return img, []
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi
acc = []
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    image, face = detect(frame)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        res = model.predict(face)

        # Get accuracy values
        if res[1] < 100:
            confidence = float("{0:.2f}".format((100*(1-(res[1])/300))))
            b = (1-(res[1])/300)
            acc.append(confidence)
            dis = str(confidence) + "% similar to Thanh Hai"
            print(b)
        font = cv2.FONT_HERSHEY_DUPLEX
        name = dis
        color = (255, 0, 0)
        stroke = 2
        cv2.putText(image, name, (100, 120), font, 1, color, stroke)

        # unlock device for high accuracy
        if confidence > 80:
            font = cv2.FONT_HERSHEY_DUPLEX
            name = "Device Unlocked"
            color = (0, 255, 0)
            stroke = 2
            cv2.putText(image, name, (250, 450), font, 1, color, stroke)
            cv2.imshow("Face croper", image)

        # keep device locked for low accuracy
        else:
            font = cv2.FONT_HERSHEY_DUPLEX
            name = "Device locked"
            color = (0, 0, 255)
            stroke = 2
            cv2.putText(image, name, (250, 450), font, 1, color, stroke)
            cv2.imshow("Face croper", image)
    except:
        # cannot detect face
        font = cv2.FONT_HERSHEY_DUPLEX
        name = "Cannot detect face"
        color = (255, 0, 0)
        stroke = 2
        cv2.putText(image, name, (250, 450), font, 1, color, stroke)
        cv2.imshow("Face croper", image)
        pass

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

print("Highest accuracy generated is" + str((np.max(acc))))

plt.plot(acc)
plt.ylabel('Accuracy')
plt.xlabel('Runtime')
plt.title('Confidence Plot')
plt.show()

cap.release()
cv2.destroyAllWindows()




