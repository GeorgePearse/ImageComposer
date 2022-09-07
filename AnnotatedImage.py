import cv2
import cvzone 
from matplotlib import pyplot as PLT

class BoundingBox:
  def __init__(
    self,
    x1,
    x2,
    y1,
    y2
  ):
    self.x1 = x1
    self.x2 = x2
    self.y1 = y1 
    self.y2 = y2

# remember, down is up.
class AnnotatedImage:
    def __init__(
        self,
        bounding_box,
        foreground_position,
        foreground_path, 
        background_path
    ):
        self.foreground_path = foreground_path
        self.background_path = background_path
        self.foreground_x = foreground_position[0]
        self.foreground_y = foreground_position[1]
        
        self.composed_image = flexible_overlay(
            background_path, 
            foreground_path, 
            self.foreground_x,
            self.foreground_y
        )
        
        x1, y1, x2, y2 = bounding_box
        self.x1 = x1 
        self.y1 = y1
        self.x2 = x2 
        self.y2 = y2

        self.image_with_box = add_bounding_box(
            self.composed_image, 
            self.x1, 
            self.y1, 
            self.x2, 
            self.y2
        )
        
    def update(self):
        self.composed_image = flexible_overlay(
            self.background_path, 
            self.foreground_path, 
            self.foreground_x,
            self.foreground_y
        )
        
        self.image_with_box = add_bounding_box(
            self.composed_image, 
            self.x1, 
            self.y1, 
            self.x2, 
            self.y2
        )
    
    def shift(self, x, y):
        self.x1 = self.x1 + x
        self.x2 = self.x2 + x
        self.y1 = self.y1 + y
        self.y2 = self.y2 + y
        self.foreground_x = self.foreground_x + x
        self.foreground_y = self.foreground_y + y 
        self.update()
        
    
    def display(self):
        plot_composed_image(self.image_with_box)
        
        
bounding_box = (160, 100, 190, 150)
foreground_position = (150, 100)

annotated_image = AnnotatedImage(
    bounding_box, 
    foreground_position,
    "./favpng_tin-can-metal-aluminium-aluminum-can-lid.png",
    "./conveyor_belt.jpeg"
)

annotated_image.display()
 
