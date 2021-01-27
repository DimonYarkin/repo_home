
'''
# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image file")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute the Scharr gradient magnitude representation of the images
# in both the x and y direction
gradX = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 1, dy = 0, ksize = -1)
gradY = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 0, dy = 1, ksize = -1)

# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
'''
''':arg
Как установить нужные билиотеки 
pip3 install pillow qrcode
'''
import qrcode

import os

# пример данных
data = "@mail: dmitryyarkin@yandex.ru"
# имя конечного файла
filename = "/media/dimon/data2/qrimage/qr.png"
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)



# команда для перемещения QR-кода на рабочий стол

#os.system("sudo mv " + my_QR.filename + " /media/dimon/data2/qrimage")