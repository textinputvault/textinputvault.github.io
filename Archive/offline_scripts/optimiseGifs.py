import subprocess
import os

def compress_and_reduce_colors_gif(folder_path, compression_level, max_colors):
    """
    Compresses and reduces colors of all GIF images in the specified folder.

    Parameters:
    - folder_path: The path to the folder containing the GIF images.
    - compression_level: Compression level (0-200), where 200 is the maximum compression.
    - max_colors: The maximum number of colors to use in the GIF (e.g., 256, 128).
    """
    # Ensure the compression level is within the allowed range
    if not (0 <= compression_level <= 200):
        print("Compression level must be between 0 and 200.")
        return

    # Ensure max_colors is a positive integer
    if max_colors <= 0:
        print("Maximum colors must be a positive integer.")
        return

    # List all GIF files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".gif"):
            original_path = os.path.join(folder_path, filename)
            compressed_path = os.path.join(folder_path, filename.rsplit('.', 1)[0] + "_col.gif")
            
            # Construct the gifsicle command with color reduction
            command = [
                'gifsicle',
                '--colors={}'.format(max_colors),
                '--lossy={}'.format(compression_level),
                '--optimize=3',
                '-o', compressed_path,
                original_path
            ]
            
            try:
                # Execute the gifsicle command
                subprocess.run(command, check=True)
                print(f"Compressed and reduced colors: {filename} -> {compressed_path.split('/')[-1]}")
            except subprocess.CalledProcessError as e:
                print(f"Error compressing and reducing colors of {filename}: {e}")

# Example usage
folder_path = "C:/Users/PC/Documents/Projects/TextinputVault_GIFs/media/"  # Change this to the path of your GIF images
compression_level = 100  # Adjust the compression level as needed
max_colors = 256  # Adjust the maximum number of colors as needed
compress_and_reduce_colors_gif(folder_path, compression_level, max_colors)
