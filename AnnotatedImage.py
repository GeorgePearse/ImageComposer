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


class AnnotatedImage: 
    def __init__(
        self, 
        background, 
        foreground, 
        foreground_position,
        bounding_box
    ):
        self.background = background
        self.foreground = foreground
        self.foreground_position = foreground_position
        self.bounding_box = bounding_box 
        self.display()
        
    def display():
        PLT.imshow(result)
        PLT.show()
    
    def shift(x, y):
        self.bounding_box.x1 = self.bounding_box.x1 + x
        self.bounding_box.x2 = self.bounding_box.x2 + x
        self.bounding_box.y1 = self.bounding_box.y1 + x
        self.bounding_box.y2 = self.bounding_box.y2 + x
