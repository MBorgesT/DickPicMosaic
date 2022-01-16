import numpy as np
import cv2
import os
from alive_progress import alive_it

def is_similar(image1, image2):
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())

deleted_img = cv2.imread('dataset_v2/deleted.jpg')
count = 0
files = os.listdir('dataset_v2/pics/')
for file in alive_it(files):
    img = cv2.imread(f'dataset_v2/pics/{file}')
    try:
        if is_similar(deleted_img, img):
            os.remove(f'dataset_v2/pics/{file}')
            count += 1
    except Exception:
        os.remove(f'dataset_v2/pics/{file}')
        count += 1
print(f'Files deleted: {count}\nProportion: {count/len(files):.2f}')