import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')

def grayscale():
  gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  cv.imshow('Gray', gray)

def blur():
  blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT) # ksize = blur effect, odd number
  cv.imshow("Blur", blur)

def edgeCascade():
  #blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) # less edges
  canny = cv.Canny(blur,125,175)
  cv.imshow('Canny', canny)

def dilate():
  blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # less edges
  canny = cv.Canny(blur,125,175)
  dilated = cv.dilate(canny, (7,7), iterations=3)
  cv.imshow('Dilated', dilated)

def erode():
  blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # less edges
  canny = cv.Canny(blur,125,175)
  dilated = cv.dilate(canny, (7,7), iterations=3)
  eroded = cv.erode(dilated,(3,3),iterations=1)
  cv.imshow('Eroded', eroded)
  return eroded

def resize():
  resize = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
  cv.imshow('Resize', resize)

def crop():
  cropped = img[50:200,200:400]
  cv.imshow('Cropped', cropped)
  
crop()
cv.waitKey(0)