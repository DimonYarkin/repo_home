'''
необходимые зависимости
pip3 install numpy

pip3 install opencv-python # Только основные методы
pip3 install opencv-contrib-python # Все методы если не ошибаюсь


'''



import cv2

def output_video():
    '''
    Процедура подключает камеру

    '''
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 24) # Частота кадров
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.

    while True:
        ret, img = cap.read()
        cv2.imshow("camera", img)
        if cv2.waitKey(10) == 27: # Клавиша Esc
            break
    cap.release()
    cv2.destroyAllWindows()


def save_video():
    cap = cv2.VideoCapture(0)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('/media/dimon/data2/qrimage/captured.avi',codec, 25.0, (640,480))
    while(cap.isOpened()):
     ret, frame = cap.read()
     if cv2.waitKey(10) == 27:
        break
     cv2.imshow('frame', frame)
     out.write(frame)
    out.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    #output_video()
    save_video()
