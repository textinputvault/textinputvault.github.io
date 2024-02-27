import os
import uuid
from PIL import Image

def resize_and_save_image(original_path, output_path, scale_factor=None):
    # Load the original image
    with Image.open(original_path) as img:
        if scale_factor is not None:
            # Calculate new size as a tuple (new_width, new_height)
            new_size = (img.width // scale_factor, img.height // scale_factor)
            # Resize the image using the LANCZOS filter for high-quality downsampling
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
            # Save the resized image
            resized_img.save(output_path)
        else:
            # Save the original image with a new name
            img.save(output_path)

def rename_and_resize_images(directory):
    image_extensions = ['.gif', '.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp']
    files = os.listdir(directory)
    image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
    image_files.sort()

    for i, filename in enumerate(image_files, start=1):
        old_path = os.path.join(directory, filename)
        extension = os.path.splitext(filename)[1].lower()

        # Full resolution image path
        full_res_filename = f"{i}_1280{extension}"
        full_res_path = os.path.join(directory, full_res_filename)

        # Low resolution image path
        low_res_filename = f"{i}_250{extension}"
        low_res_path = os.path.join(directory, low_res_filename)

        # Save full resolution image
        resize_and_save_image(old_path, full_res_path)

        # Save low resolution image (scale_factor of 5)
        resize_and_save_image(old_path, low_res_path, scale_factor=5)

        print(f"Processed {filename}: Full res -> {full_res_filename}, Low res -> {low_res_filename}")

# Replace 'path/to/your/folder' with the path to the folder containing your images
directory_path = 'H:/Project/textinputvault.github.io/media/'
rename_and_resize_images(directory_path)
