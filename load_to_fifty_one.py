import glob
import fiftyone as fo


annotated_images = [annotated_image]

# Create samples for your data
samples = []
for annotated_image in annotated_images:
    
    sample = fo.Sample(filepath=annotated_image.path)

    # Convert detections to FiftyOne format
    detections = []
    
    bounding_box = annotated_image.bounding_box
    
    #for bounding_box in annotated_image.bounding_boxes:
    
    label = bounding_box.label

    # Bounding box coordinates should be relative values
    # in [0, 1] in the following format:
    # [top-left-x, top-left-y, width, height]
    bounding_box = bounding_box.return_fifty_one_style()

    detections.append(
        fo.Detection(label=label, bounding_box=bounding_box)
    )

    # Store detections in a field name of your choice
    sample["ground_truth"] = fo.Detections(detections=detections)

    samples.append(sample)

# Create dataset
dataset = fo.Dataset("augmented-samples")
dataset.add_samples(samples)
