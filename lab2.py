from statistics import mode
from skimage import io, img_as_float
import cv2
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage.filters import convolve

img = img_as_float(io.imread("/Users/adityabiswal/Desktop/computer_vision/puppy.jpeg", as_gray=True))

kernel = np.ones((5,5),np.float32)/25

gaussian_kernel = np.array([[1/16, 1/8, 1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]])


conv_using_cv2 = cv2.filter2D(img,-1,kernel,borderType=cv2.BORDER_CONSTANT)

conv_using_scipy_signal = convolve2d(img,kernel,mode='same')
conv_using_scipy_ndimage = convolve(img,kernel,mode='constant',cval=0.4)


cv2.imshow("Original",img)
cv2.imshow("cv2 filter",conv_using_cv2)
#cv2.imshow("using scipy signal",conv_using_scipy_signal)
#cv2.imshow("using nd",conv_using_scipy_ndimage)

cv2.waitKey(0)
cv2.destroyAllWindows()

