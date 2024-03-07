import os
from PIL import Image, ImageSequence

def resize_gif(original_path, output_path, scale_factor=None):
    # Open the original GIF
    with Image.open(original_path) as img:
        # Create a list to hold the resized frames
        frames = []
        for frame in ImageSequence.Iterator(img):
            # Resize each frame
            if scale_factor is not None:
                new_size = (frame.width // scale_factor, frame.height // scale_factor)
                resized_frame = frame.resize(new_size, Image.Resampling.LANCZOS)
            else:
                resized_frame = frame.copy()
            frames.append(resized_frame)

        # Use a default duration if 'duration' is not in img.info
        duration = img.info.get('duration', 100) # 100 ms as a common default

        # Save the frames as a new GIF
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=duration, optimize=False)


def resize_and_save_image(original_path, output_path, scale_factor=None):
    # Check if the image is a GIF
    if original_path.lower().endswith('.gif'):
        resize_gif(original_path, output_path, scale_factor)
    else:
        # Process non-GIF images as before
        with Image.open(original_path) as img:
            if scale_factor is not None:
                new_size = (img.width // scale_factor, img.height // scale_factor)
                resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                resized_img.save(output_path)
            else:
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
        full_res_filename = f"{i+img_numb_offset}_highres{extension}"
        full_res_path = os.path.join(directory, full_res_filename)

        # Low resolution image path
        low_res_filename = f"{i+img_numb_offset}_lowres{extension}"
        low_res_path = os.path.join(directory, low_res_filename)

        # Save full resolution image
        resize_and_save_image(old_path, full_res_path)

        # Save low resolution image (scale_factor of 3 for example)
        resize_and_save_image(old_path, low_res_path, scale_factor=2)

        print(f"Processed {filename}: Full res -> {full_res_filename}, Low res -> {low_res_filename}")

# Replace 'directory_path' with the path to the folder containing your images
newPath = input('path: ')
# Compute image number offset i.e. count how many images already exist in the media folder to avoid overwriting them 
os.chdir("../media")
img_numb_offset = len(os.listdir())/2 + 1
directory_path = newPath
rename_and_resize_images(directory_path)
