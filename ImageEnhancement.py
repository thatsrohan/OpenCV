import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r'C:\Users\LENOVO\OneDrive\Pictures\enhc.jfif')
matrix=np.ones(img.shape,dtype="uint8")*50
img_brighter=cv2.add(img,matrix)
img_darker=cv2.subtract(img,matrix)
matrix1=np.ones(img.shape)*.8
matrix2=np.ones(img.shape)*1.2
img_high_contrast=np.uint8(np.clip(cv2.multiply(np.float64(img),matrix2),0,255))
img_low_contrast=np.uint8(cv2.multiply(np.float64(img),matrix1))
img_new=cv2.imshow(r'C:\Users\LENOVO\Downloads\piano_sheet_music',0)
thresholded_img_1=cv2.threshold(img_new,50,255,cv2.THRESH_BINARY)
thresholded_img_2=cv2.threshold(img_new,130,255,cv2.THRESH_BINARY)
plt.imshow(thresholded_img_1,cmap='gray')
plt.imshow(thresholded_img_2,cmap='gray')




