from PIL import Image
import os

# Define the input image path and output size
input_image = r'C:\Users\Racharla Soumya\OneDrive\Pictures\image.png'
output_folder = r'C:\Users\Racharla Soumya\OneDrive\Pictures\resized pictures'
output_size = (800, 600)  # Example size

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open and resize the image
img = Image.open(input_image)
img = img.resize(output_size)

# Save the resized image to output folder
output_path = os.path.join(output_folder, os.path.basename(input_image))
img.save(output_path)

print("Image resizing completed.")