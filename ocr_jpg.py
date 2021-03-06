from cv2 import cv2 
import pytesseract
import numpy as np
from pytesseract import Output


image = cv2.imread('page_1.jpg')


# point to the tesseract install location
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'




# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)






# Creating a text file to write the output
outfile = "out_text1.txt"
  
# Open the file in append mode so that 
# All contents of all images are added to the same file
f = open(outfile, "a")  


# Adding custom options
custom_config = r'--oem 3 --psm 6'
text1=pytesseract.image_to_string(image, config=custom_config)
text=pytesseract.image_to_data(image,output_type=Output.DICT)#, config=custom_config)
pytesseract.image_to_boxes

f.write(text1)
f.close()

# OPEN CV stuffs
# gray = get_grayscale(image)
# thresh = thresholding(gray)
# opening = opening(gray)
# canny = canny(gray)

# n_boxes = len(text['text'])
# for i in range(n_boxes):
#     if int(text['conf'][i]) > 60:
#         (x, y, w, h) = (text['left'][i], text['top'][i], text['width'][i], text['height'][i])
#         img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# imS = cv2.resize(image, (1440, 1080))  
# cv2.imshow('img', imS)
# cv2.waitKey(0)






