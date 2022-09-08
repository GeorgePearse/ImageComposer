import albumentations as A
import cv2

# Declare an augmentation pipeline
transform = A.Compose([
    A.Rotate(0.8),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
])

# Read an image with OpenCV and convert it to the RGB colorspace
image = cv2.imread("./favpng_tin-can-metal-aluminium-aluminum-can-lid.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Augment an image
transformed = transform(image=image)
transformed_image = transformed["image"]
