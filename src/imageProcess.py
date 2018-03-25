import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
def image_capture():
    # Read image
    img = cv2.imread('./../res/image1.png', 1)
    r = cv2.selectROI(img)
    while True:
        imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("end")
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    image_capture()


