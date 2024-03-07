# Text Input Vault for XR

Welcome to the Text Input Vault for XR, a dynamic gallery designed to enhance your extended reality (XR) experiences with a rich collection of images. This README provides instructions on how to contribute to the image gallery, ensuring that your content is properly integrated and accessible within our XR applications.

## How to Add New Images to the Gallery

Adding new images to the gallery is a straightforward process that involves running a couple of scripts from the `offline_scripts` folder. Follow these steps to ensure your images are correctly processed and added to the gallery.

### Step 1: Prepare Your Images

Before you begin, make sure your images are ready for import. It's recommended to organize them in a specific folder on your device for easier processing.

### Step 2: Number and Generate Low-Resolution Media

a. Navigate to the `offline_scripts` folder in your project directory.
b. Run the `number_and_lowres_media.py` Python script. This script performs two main functions:

- Numbers each image, accounting for the number of images already in the media folder.
- Creates a low-resolution version of each image to ensure faster loading times in the gallery.

When prompted, provide the path to the folder where you've stored the images you wish to import. The script will automatically process all images in the folder.

### Step 3: Update the Image List

After processing your images, the next step is to update the gallery's index file to include your new additions.

a. Still within the `offline_scripts` folder, run the `imageList_generator.py` Python script. This script updates the `imageList.json` file, which serves as the gallery's index, with the details of the newly added images.

b. Copy the newly generated `imageList.json` file from the `offline_scripts` folder into the root directory of this repository.

c. Copy your newly renamed and lowres images to the media folder so that they can be automatically displayed into the gallery.

In future we would like to make the `imageList.json` file more sophisticated in order to hold more information about each text input technique image for use in more interesting data analysis.

## Contributing

Your contributions are what make the Text Input Vault for XR a valuable resource for the XR community. If you encounter any issues during the process or have suggestions on how to improve the gallery, please feel free to open an issue or submit a pull request.

Thank you for contributing to the Text Input Vault for XR!
