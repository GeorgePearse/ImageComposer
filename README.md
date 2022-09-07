# ImageComposer
Package to simplify creating simple synthetic image pytorch datasets for model training. 

You specify the background and foreground objects, range of feasible positions, and the package does the rest.

A great way to deal with correlated components (my made up name for when a visual property distracts a computer vision model from what it's meant to learn). What I mean by this is metadata (like a watermark) which correlates with the true classes, but not always. 

<img width="311" alt="image" src="https://user-images.githubusercontent.com/47161914/188951951-1799e8fa-a011-4f48-9b11-ec9e3bb71282.png">

# Pasting Rules

* Define all the reasonable positions for an object to be with a function e.g. x**2 + y**2 < 3 or similar

## Resources 

https://www.youtube.com/watch?v=voRFbl-GKGY


## Augmentations 

Just integrate imgaug or albumentations. 
* Rotate
* Add noise 
* Flip
* Resize 
* Rotate
* Change brightness


