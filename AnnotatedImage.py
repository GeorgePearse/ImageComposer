import cv2
import cvzone 
from matplotlib import pyplot as PLT

class ValidForegroundSpace: 
    """
    Just use some method for defining polygons in opencv. 
    
    Will be easiest if you just sample x and y values and 
    either allow or disallow them. 
    """
    def __init__(self):
        pass

# remember, down is up.
class ForegroundObject: 
    def __init__(
        self,
        path,
        position
    ):
        self.path = path
        self.x, self.y = position[0], position[1]

class Background:
    def __init__(
        self, path
    ):
        self.path = path
        
    def flexible_overlay(
        self, foreground, target_x, target_y
    ):
        """
        target_x: higher number = further to the right
        target_y: higher number = further down
        """
        imgBack = cv2.imread(self.path)
        imgFront = cv2.imread(foreground.path, cv2.IMREAD_UNCHANGED)
        imgFront = cv2.resize(imgFront, (0, 5), None, 0.04, 0.04)


        hf, wf, cf = imgFront.shape
        hb, wb, cb = imgBack.shape

        result = cvzone.overlayPNG(imgBack, imgFront, 
                                   [target_x, target_y])
        return result
        
class BoundingBox:
    def __init__(
        self,
        x1,
        y1,
        x2,
        y2
    ):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1 
        self.y2 = y2
        

class AnnotatedImage:
    def __init__(
        self,
        bounding_box,
        foreground,
        background
    ):
        self.background = background
        self.foreground = foreground
        self.bounding_box = bounding_box
        
        self.composed_image = flexible_overlay(
            self.background.path, 
            self.foreground.path, 
            self.foreground.x,
            self.foreground.y
        )

        self.image_with_box = add_bounding_box(
            self.composed_image, 
            self.bounding_box.x1, 
            self.bounding_box.y1, 
            self.bounding_box.x2, 
            self.bounding_box.y2
        )
        
    def update(self):
        self.composed_image = flexible_overlay(
            self.background.path, 
            self.foreground.path, 
            self.foreground.x,
            self.foreground.y
        )

        self.image_with_box = add_bounding_box(
            self.composed_image, 
            self.bounding_box.x1, 
            self.bounding_box.y1, 
            self.bounding_box.x2, 
            self.bounding_box.y2
        )
    
    def shift(self, x, y):
        self.bounding_box.x1 = self.bounding_box.x1 + x
        self.bounding_box.x2 = self.bounding_box.x2 + x
        self.bounding_box.y1 = self.bounding_box.y1 + y
        self.bounding_box.y2 = self.bounding_box.y2 + y
        self.foreground.x = self.foreground.x + x
        self.foreground.y = self.foreground.y + y 
        self.update()
        
    
    def display(self):
        PLT.imshow(self.image_with_box)
        PLT.show()
        
        
bounding_box = BoundingBox(160, 100, 190, 150)
foreground = ForegroundObject("./favpng_tin-can-metal-aluminium-aluminum-can-lid.png", (150, 100))
background = Background("./conveyor_belt.jpeg")

annotated_image = AnnotatedImage(
    bounding_box, 
    foreground,
    background
)

annotated_image.display()
 
