import cv2
import os

# Set the target size of the images
target_size = (300, 300)

# Loop through each person's directory
for person in os.listdir('dataset'):
    # Create a new directory for the resized images
    os.makedirs(os.path.join('resized_dataset', person), exist_ok=True)

    # Loop through each image in the person's directory
    for file in os.listdir(os.path.join('dataset', person)):
        # Check if the file is an image
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".bmp"):
            # Load the image
            img = cv2.imread(os.path.join('dataset', person, file))

            # Check if the image is not None
            if img is not None:
                # Get the current size of the image
                height, width, channels = img.shape

                # Calculate the aspect ratio of the image
                aspect_ratio = width / height

                # Calculate the new size of the image while maintaining the aspect ratio
                if aspect_ratio > 1:
                    # Landscape image
                    new_width = target_size[0]
                    new_height = int(new_width / aspect_ratio)
                else:
                    # Portrait image
                    new_height = target_size[1]
                    new_width = int(new_height * aspect_ratio)

                # Resize the image
                img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

                # Add padding to the image to make it square
                top = int((target_size[1] - new_height) / 2)
                bottom = target_size[1] - new_height - top
                left = int((target_size[0] - new_width) / 2)
                right = target_size[0] - new_width - left
                img_padded = cv2.copyMakeBorder(img_resized, top, bottom, left, right, cv2.BORDER_CONSTANT)

                # Save the resized and padded image to the new directory
                cv2.imwrite(os.path.join('resized_dataset', person, file), img_padded)
            else:
                print(f"Unable to read image file: {os.path.join('dataset', person, file)}")
        else:
            print(f"Skipping non-image file: {os.path.join('dataset', person, file)}")
