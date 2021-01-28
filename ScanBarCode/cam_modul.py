'''
необходимые зависимости
pip3 install numpy

pip3 install opencv-python # Только основные методы
pip3 install opencv-contrib-python # Все методы если не ошибаюсь


'''

import cv2
import numpy as np  # модуль обработки массивов
import sys  # системный модуль
import time


#  Создание функции выводящей в отдельном окне изображение QR с синим обрамлением.
def display(im, bbox):
    n = len(bbox)

    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[(j + 1) % n][0]), (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im)


def output_video():
    '''
    Процедура подключает камеру

    '''

    qrDecoder = cv2.QRCodeDetector()  # создание объекта детектора

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 24)  # Частота кадров
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)  # Ширина кадров в видеопотоке.
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Высота кадров в видеопотоке.

    while True:
        ret, img = cap.read()
        cv2.imshow("camera", img)
        cv2.imwrite("/media/dimon/hrcdisk/qrimage/11.jpg", img)

        # Первый блок проверяет условие, передан ли скрипту в командной строке дополнительный аргумент в виде картинки **QR кода**. Если первое условие ложно, то считывается указанная нами картинка.

        inputImage = cv2.imread(
            "/media/dimon/hrcdisk/qrimage/11.jpg")  # стандартный метод opencv для считывания изображения

        data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)

        if len(data) > 0:
            print("Decoded Data : {}".format(data))  # вывод декодированной строки

            display(inputImage, bbox)
            break

        if cv2.waitKey(10) == 27:  # Клавиша Esc
            cv2.imwrite("/media/dimon/hrcdisk/qrimage/11.jpg", img)
            break

    cap.release()
    cv2.destroyAllWindows()


def save_video():
    cap = cv2.VideoCapture(0)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('/media/dimon/hrcdisk/qrimage/captured.avi', codec, 25.0, (640, 480))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if cv2.waitKey(10) == 27:
            break
        cv2.imshow('frame', frame)
        out.write(frame)
    out.release()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    output_video()
    # save_video()
    # В Opencv имеется  встроенный метод детектор QR
