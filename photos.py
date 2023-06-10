import time
from PIL import Image
from tkinter import filedialog
import numpy as np
import cv2
import fileinput
import os
import sys
import pathlib
import subprocess

filename = filedialog.askopenfilename()

def open_file_photo():
    filename = filedialog.askopenfilename()
    if filename:
        subprocess.run(["python", "main.py", filename])

def get_image_path(filename):
    return f'images/{pathlib.PurePath(filename).name}'

def get_detected_objects(net, image_path, min_confidence, classes, colors, width, height):
    image = cv2.imread(image_path)
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007 , (300, 300), 130) # Binary Large OBject
    net.setInput(blob)
    detected_objects = net.forward()

    objects = []

    for i in range(detected_objects.shape[3]):

        confidence = detected_objects[0][0][i][2]

        if confidence > min_confidence:

            class_index = int(detected_objects[0, 0, i, 1])

            upper_left_x = int(detected_objects[0, 0, i, 3] * width)
            upper_left_y = int(detected_objects[0, 0, i, 4] * height)
            lower_left_x = int(detected_objects[0, 0, i, 5] * width)
            lower_left_y = int(detected_objects[0, 0, i, 6] * height)

            prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
            objects.append((upper_left_x, upper_left_y, lower_left_x, lower_left_y, prediction_text, colors[class_index]))

    return objects
def draw_detected_objects(image, detected_objects):
    for obj in detected_objects:
        cv2.rectangle(image, (obj[0], obj[1]), (obj[2], obj[3]), obj[5], 3)
        cv2.putText(image, obj[4], (obj[0], obj[1] - 15 if obj[1] > 30 else obj[1] + 15),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, obj[5], 2)

image_path = get_image_path(filename)
protoxtx_path = 'models/MobileNetSSD_deploy.prototxt'
model_path = 'models/MobileNetSSD_deploy.caffemodel'
min_confidence = 0.2

classes = ['background', 'aeroplane', 'bycycle', 'bird', 'boat',
'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep',
'sofa', 'train', 'tvmonitor']
# np.random.seed(543210)
colors = np.random.uniform(0, 255, size=(len(classes), 3))

net = cv2.dnn.readNetFromCaffe(protoxtx_path, model_path)

image = cv2.imread(image_path)
height , width = image.shape[0], image.shape[1]
detected_objects = get_detected_objects(net, image_path, min_confidence, classes, colors, width, height)

draw_detected_objects(image, detected_objects)

normal_size = os.path.getsize(filename)

cv2.imshow("Detected Objects", image)
cv2.waitKey()

cv2.destroyAllWindows()

current_time = int(time.time() * 1000)

cv2.imwrite(f"used_images/output{format(current_time)}.jpg", image)




