# ImageComposer
Package to simplify creating simple synthetic image pytorch datasets for model training. 

You specify the background and foreground objects, range of feasible positions, and the package does the rest.

A great way to deal with correlated components (my made up name for when a visual property distracts a computer vision model from what it's meant to learn)


<img width="230" alt="image" src="https://user-images.githubusercontent.com/47161914/188900964-f0d1fd9d-616d-4f8b-962d-da918bb0f108.png">

<img width="390" alt="image" src="https://user-images.githubusercontent.com/47161914/188908144-03503c7a-0c94-4eb9-b6e3-a60f0227e507.png">

This package is for Object Detection and uses the COCO dataset format as described by fiftyone below: 
<img width="910" alt="image" src="https://user-images.githubusercontent.com/47161914/188914721-ee205b47-e22a-478f-b5fc-96e20516ce6b.png">


# Pasting Rules

* Define all the reasonable positions for an object to be with a function e.g. x**2 + y**2 < 3 or similar

## Resources 

https://www.youtube.com/watch?v=voRFbl-GKGY

