#Method 1
import cv2
image_original = cv2.imread("C:\Everything\koizumi1460.jpg",
                       cv2.IMREAD_COLOR)
save_dir = "C:\SomewhereElse\some_name.jpg"
cv2.imwrite(save_dir, image_original)

#Method 2
from PIL import Image
to_save = Image.open("C:\Everything\koizumi1460.jpg")
to_save.save(save_dir)