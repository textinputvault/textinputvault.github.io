import os
import uuid

def rename_images(directory):
    # Define a list of image file extensions to include
    image_extensions = ['.gif', '.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp']
    
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter out files that are not in the specified image file types
    image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
    
    # Sort files to maintain a consistent order
    image_files.sort()
    
    # First pass: rename all image files to a temporary name
    temp_files = []
    for filename in image_files:
        # Generate a unique temporary filename
        temp_filename = f"{uuid.uuid4()}{os.path.splitext(filename)[1].lower()}"
        
        # Construct full file paths
        old_path = os.path.join(directory, filename)
        temp_path = os.path.join(directory, temp_filename)
        
        # Rename the file to the temporary name
        os.rename(old_path, temp_path)
        temp_files.append(temp_filename)
    
    # Second pass: rename all temporary files to the final name
    for i, temp_filename in enumerate(temp_files, start=1):
        # Extract original extension
        original_extension = os.path.splitext(temp_filename)[1].lower()
        
        # Construct new filename with the original extension
        new_filename = f"{i}{original_extension}"
        
        # Construct full file paths
        temp_path = os.path.join(directory, temp_filename)
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file to its final name
        os.rename(temp_path, new_path)
        print(f"Renamed {temp_filename} to {new_filename}")

# Replace 'path/to/your/folder' with the path to the folder containing your images
directory_path = 'C:/Users/Monter/Projects/textinputvault.github.io/media/'
rename_images(directory_path)
