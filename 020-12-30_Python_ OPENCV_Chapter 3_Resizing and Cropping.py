#LEARN OPENCV in 3 HOURS-Murtaza Workshop- March 25 2020
# Chapter 3: Resizing and Cropping

#EXAMPLE 2: CROPPING AN IMAGE
""" IMAGE itself is matrix or array of pixels """
import cv2

img = cv2.imread("webcamdimesions.png")
print(img.shape)

imgResize = cv2.resize(img,(500,250))
print(imgResize.shape)

# CROPPING FUNCTION: We dont need cv2 to crop
#imgCropped = img[height,width]
imgCropped = img[0:350,350:600]


cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)


cv2.waitKey(0)


#--------------------------------------------------------
#-EXAMPLE 1: RESIZING AN IMAGE
"""
import cv2

img = cv2.imread("webcamdimesions.png")

# checking the image size
print(img.shape)
#printout(height,width,BGR Number)

# RESIZING AN IMAGE
imgResize = cv2.resize(img,(500,250))
print(imgResize.shape)


cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)

cv2.waitKey(0)
"""
#------------------------------------------------------------
