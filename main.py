import time

import mss
import numpy as np
import cv2
import pyautogui as pg


BOX_COORD = {'top': 300, 'left': 120, 'width': 30, 'height': 40}

#BOX_COORD = {'top': 340, 'left': 335, 'width': 30, 'height': 40}


def process_image(original_image):
    #Create copy of input image
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    #found borders of every object on image
    #use algorytm Canny
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def screen_record():
    # prepering class for screenshot
    sct = mss.mss()
    last_time = time.time()

    while True:
        # check down line
        # make a screenshot
        img = sct.grab(BOX_COORD)
        img = np.array(img)
        processed_image = process_image(img)
        #count average of every border, if this value !=0, it means there are some obstacles, so we have to
        #jump over
        mean = np.mean(processed_image)
        print('down mean = ', mean)

        if mean != float(0):
            pg.press('space')
            continue

        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()


if __name__ == '__main__':
    screen_record()
