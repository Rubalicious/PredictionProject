import numpy as np
import cv2
from pprint import pprint
from matplotlib import pyplot as plt

img = cv2.imread('dontspeed.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

# rect = (500,10,400,450)
# cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

# mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# img = img*mask2[:,:,np.newaxis]

# newmask is the mask image I manually labelled
newmask = cv2.imread('dontspeed_mask2.jpg',0)

# whereever it is marked white (sure foreground), change mask=1
# whereever it is marked black (sure background), change mask=0
mask[newmask == 0] = 1
mask[newmask == 255] = 0

# mask, bgdModel, fgdModel = 
cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

mask = np.where((mask==1)|(mask==0),1,0).astype('uint8')
pprint(mask)
img = img*mask[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()