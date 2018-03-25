import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
def image_capture():

    # Read image
    img = cv2.imread('./../res/image1.png', 1)
    fromCenter = False

    r = cv2.selectROI("Select ROI", img, fromCenter)
    while True:

        imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("end and save")
            path = "./../res/modify_img/"
            # filename = "test" + (1) +".jpg"
            cv2.imwrite(path + "test1.jpg", imCrop)
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    image_capture()


