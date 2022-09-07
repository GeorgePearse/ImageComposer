import cv2
import cvzone 
from matplotlib import pyplot as PLT

def flexible_overlay(background_path, foreground_path, target_x, target_y):
    """
    target_x: higher number = further to the right
    target_y: higher number = further down
    """
    imgBack = cv2.imread(background_path)
    imgFront = cv2.imread(foreground_path, cv2.IMREAD_UNCHANGED)
    imgFront = cv2.resize(imgFront, (0, 5), None, 0.04, 0.04)


    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape

    result = cvzone.overlayPNG(imgBack, imgFront, 
                               #[target_x, hb-hf])
                               [target_x, target_y])
    return result


def add_bounding_box(img, x1, y1, x2, y2):
    image_copy = img.copy()
    image_with_box = cv2.rectangle(image_copy, (x1, y1), (x2, y2), (255,0,0), 2)
    return image_with_box
    
    
def plot_composed_image(result):
    PLT.imshow(result)
    PLT.show()
