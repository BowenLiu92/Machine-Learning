import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#Method 1
image = mpimg.imread("C:\Efake\e1133rio_0280.jpg",
                       cv2.IMREAD_COLOR)
#plt.imshow(image)
#plt.show()

#Method 2
from PIL import Image
Image.open("C:\Efake\e1133rio_0280.jpg")

#Method 3

#Only works in Ipython

from IPython.display import Image as IPimg
IPimg("C:\fake\e1133rio_0280.jpg")