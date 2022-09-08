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


###########################################

def add_alpha_channel(img):
    """
    Sometimes a png image doesn't have an alpha channel.
    
    Most of the code you're writing needs an alpha channel
    """
    b_channel, g_channel, r_channel = cv2.split(img)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.
    img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    return img_BGRA
