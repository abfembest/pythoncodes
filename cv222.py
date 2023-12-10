import os
import cv2
def mypic():
    a = input('Enter the image name to search ')
    ext = ['.jpg', '.png', '.gif']
    for i in ext:
        b = a + i
        if os.path.exists(b):
            b2= cv2.imread(b)
            cv2.imshow('New image', b2)
            h,w,c = (b2.shape)
            print('The hiegth is ', h)
            break
        else:
            print('Image not exists')
