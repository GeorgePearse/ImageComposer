import cv2
import cvzone 
from matplotlib import pyplot as PLT
from dataclasses import dataclass
import glob
import fiftyone as fo


class ValidForegroundSpace: 
    """
    Just use some method for defining polygons in opencv. 
    
    Will be easiest if you just sample x and y values and 
    either allow or disallow them. 
    """
    def __init__(self):
        pass


@dataclass
class ForegroundObject: 
    path: str 
    x: int 
    y: int
        

class Background:
    def __init__(
        self, path: str
    ):
        self.path = path
        
    def flexible_overlay(
        self, foreground, target_x: int, target_y: int
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
        
@dataclass
class BoundingBox:
    x1: int 
    y1: int 
    x2: int 
    y2: int 
    classification: str
        

class AnnotatedImage:
    """
    There will definitely be some much better pattern for the update.
    """
    def __init__(
        self,
        bounding_box: BoundingBox,
        foreground: ForegroundObject,
        background: Background
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
        
        
    def export_to_coco(self, coco_label_path: str):
        """
        To do: 
        * [] Write composed image to images/ dir
        * [] Write corresponding bounding box to label.json (bounding boxes will need a class)
        * [] Write filepath and other metadata to label.json 
        
        https://voxel51.com/docs/fiftyone/user_guide/dataset_creation/index.html#custom-formats
        """
   

        images_patt = "/path/to/images/*"

        # Ex: your custom label format
        annotations = {
            "/path/to/images/000001.jpg": "dog",
            ....,
        }

        # Create samples for your data
        samples = []
        for filepath in glob.glob(images_patt):
            sample = fo.Sample(filepath=filepath)

            # Store classification in a field name of your choice
            label = annotations[filepath]
            sample["ground_truth"] = fo.Classification(label=label)

            samples.append(sample)

        # Create dataset
        dataset = fo.Dataset("my-classification-dataset")
        dataset.add_samples(samples)

                with open(coco_label_path) as f: 
                    f.write(self.bounding_box

                with open(coco_label_path) as f: 
                    f.write(self.bounding_box
                    
                    
class SyntheticDataset:
    """
    Idea here will be to combine backgrounds, with some subset of reasonable foregrounds.
    
    Rule for good places to position foreground objects need to be defined in the background class.
    At least that's the requirement of the problem I'm focusing on.
    """
    def __init__(self):
        pass
            
        
        
        
bounding_box = BoundingBox(160, 100, 190, 150, 'tin_can')
foreground = ForegroundObject("./favpng_tin-can-metal-aluminium-aluminum-can-lid.png", 150, 100)
background = Background("./conveyor_belt.jpeg")

annotated_image = AnnotatedImage(
    bounding_box, 
    foreground,
    background
)

annotated_image.display()
 
    
for x in range(0, 100):
    annotated_image.shift(1, -1)
    annotated_image.display()
