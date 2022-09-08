# ImageComposer
Package to simplify creating simple synthetic image pytorch datasets for model training. 

NB: Possible that BlenderProc offers all this in a much more powerful way. I just couldn't get it going on my laptop and wanted to start experimenting.

You specify the background and foreground objects, range of feasible positions, and the package does the rest.

A great way to deal with correlated components (my made up name for when a visual property distracts a computer vision model from what it's meant to learn). What I mean by this is metadata (like a watermark) which correlates with the true classes, but not always. 

<img width="311" alt="image" src="https://user-images.githubusercontent.com/47161914/188951951-1799e8fa-a011-4f48-9b11-ec9e3bb71282.png">

# Pasting Rules

* Define all the reasonable positions for an object to be with a function e.g. x**2 + y**2 < 3 or similar

## Resources 

https://www.youtube.com/watch?v=voRFbl-GKGY


## Valid Regions Concept

* Would be great if you could freehand / poly draw a region of an image, upon which the items can be placed, with something like label-studio.


Want to then be able to repaste the below elsewhere from the polygon label.


<img width="556" alt="image" src="https://user-images.githubusercontent.com/47161914/189086968-bfd8d6cf-dc85-4104-afad-c9ee388a9614.png">

## ML integrations

* Eventually you could integrate some Computer Vision package to try to make the images more realistic. Something like https://machinelearning.apple.com/research/gan

## Augmentations 

Just integrate imgaug or albumentations. 
* Rotate
* Add noise 
* Flip
* Resize 
* Rotate
* Change brightness


