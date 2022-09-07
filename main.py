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

class AnnotatedImage:
    def __init__(
        self,
        bounding_box,
        foreground_position,
        foreground_path, 
        background_path
    ):
        self.composed_image = flexible_overlay(
            background_path, 
            "./favpng_tin-can-metal-aluminium-aluminum-can-lid.png", 
            foreground_position[0],
            foreground_position[1]
        )
        x1, y1, x2, y2 = bounding_box
        self.image_with_box = add_bounding_box(result_one, x1, y1, x2, y2)
    
    
    def display(self):
        plot_composed_image(self.image_with_box)
        
bounding_box = (160, 100, 190, 150)
foreground_position = (150, 100)

annotated_image = AnnotatedImage(
    bounding_box, 
    foreground_position,
    foreground_path,
    background_path
)

annotated_image.display()
