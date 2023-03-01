'''
ozzmanmuhammad
'''

from django.db import models
from django.conf import settings

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
# from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, decode_predictions, preprocess_input
from tensorflow.keras.models import load_model

import os
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

model = load_model(os.path.join(settings.MEDIA_ROOT, 'model', 'final_model.h5'))

def interpret_output(cls, boxes, img_size=(500, 333)):
    img_resize = 224
    filters = ['dog', 'cat', 'bird', 'cow', 'horse']
    idx2labels = {k: v for k, v in enumerate(filters)}
    labels2idx = {v: k for k, v in idx2labels.items()}
    cls_idx = np.argmax(cls)
    confidence = cls[cls_idx]
    classname = idx2labels[cls_idx]
    cx, cy = boxes[0], boxes[1]
    w, h = boxes[2], boxes[3]
    
    small_box = [max(0, cx - w / 2), max(0, cy - h / 2),
                 min(img_resize, cx + w / 2), min(img_resize, cy + h / 2)]
    fullsize_box = [int(small_box[0] * img_size[0] / img_resize),
                    int(small_box[1] * img_size[1] / img_resize),
                    int(small_box[2] * img_size[0] / img_resize),
                    int(small_box[3] * img_size[1] / img_resize)]
    output = {'class': classname, 'confidence': confidence, 'bbox': fullsize_box}
    return output


# Create your models here.
class animalIdentifier(models.Model):
    picture = models.ImageField()
    predicted = models.ImageField(blank=True)
    classified = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image classfied at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))

    def save(self, *args, **kwargs):
        try:
            print("Loading image")
            org_img = Image.open(self.picture)

            # Convert the image to a NumPy array and get its dimensions
            height, width, channels = np.array(org_img).shape
            org_img_1 = np.array(org_img)
            
            img = org_img.resize((224,224))
            img_arr = np.array(img)

            test_img_arr = np.expand_dims(img_arr, 0)
            test_img_arr = tf.keras.applications.resnet50.preprocess_input(test_img_arr)
            res = model.predict(test_img_arr)
            
            output = interpret_output(res[0][0], res[1][0], img_size=(width, height))
            print(output)
            
            x1 = output['bbox'][0]
            x2 = output['bbox'][2]
            y1 = output['bbox'][1]
            y2 = output['bbox'][3]
            
            label = output['class']
            
            color = (0, 255, 0)
            text_color = (0, 0, 0)
            
            # For bounding box
            img = cv2.rectangle(org_img_1, (x1, y1), (x2, y2), color, 2)
            
            # For the text background
            # Finds space required by the text so that we can put a background with that amount of width.
            (w, h), _ = cv2.getTextSize(
                    label, cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

            # Prints the text.    
            img = cv2.rectangle(img, (x1, y1 - 20), (x1 + w, y1), color, -1)
            img = cv2.putText(img, label, (x1, y1 - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imwrite(os.path.join(settings.MEDIA_ROOT, self.picture.name), img)
            
            self.classified = str(label)
            self.predicted = self.picture.name
            print('success')
        except Exception as e:
            print('classification failed', e)
        super().save(*args, **kwargs)

