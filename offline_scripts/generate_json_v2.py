import os
import json

def generate_images_json(directory):
    # Define the output file name
    output_file = 'images.json'
    
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter out image files based on naming convention (contains "_250" or "_1280")
    image_files = [f for f in files if "_250" in f or "_1280" in f]
    
    # Initialize a list to hold image data
    images_data = []
    
    # Process each image file
    for filename in image_files:
        # Extract base name and format
        base_name, extension = os.path.splitext(filename)
        image_format = extension.lstrip('.').lower()
        
        # Determine size based on the filename
        if "_250" in base_name:
            size = "250"
        elif "_1280" in base_name:
            size = "1280"
        else:
            # If the size is not in the expected format, skip this file
            continue
        
        # Remove size suffix to get the pure numeric name
        name = base_name.replace("_250", "").replace("_1280", "")
        
        # Append image data to the list
        images_data.append({"name": name, "format": image_format, "size": size})
    
    # Write the data to a JSON file
    with open(output_file, 'w') as f:
        json.dump(images_data, f, indent=2)

# Replace 'path/to/your/folder' with the path to the folder containing your images
directory_path = 'H:/Project/textinputvault.github.io/media/'
generate_images_json(directory_path)
