import cv2
import cvzone 
from matplotlib import pyplot as PLT

def overlay(foreground_path, background_path): 

    background = cv2.imread(background_path)
    foreground = cv2.imread(foreground_path, cv2.IMREAD_UNCHANGED)

    height, width, _ = foreground.shape
    dim = (width, height)

    # resize image
    resized_background = cv2.resize(background, dim, interpolation = cv2.INTER_AREA)

    result = cvzone.overlayPNG(resized_background, foreground, [0,0])
    PLT.imshow(result)
    PLT.show()
