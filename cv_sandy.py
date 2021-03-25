import cv2
import numpy as np
import glob

if __name__ == '__main__':
   def callback(*arg):
       print (arg)

hsv_min = np.array((0, 0, 0), np.uint8)
hsv_max = np.array((255, 255, 158), np.uint8)

for fn in glob.glob("cv_imgs/*"):
    print(fn)
    img = cv2.imread(fn)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)

    cv2.imwrite("cv_masks/"+fn[8:-4]+"_mask.jpg",thresh)
