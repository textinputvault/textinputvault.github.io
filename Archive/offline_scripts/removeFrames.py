import subprocess
import os

def remove_frames_gif(folder_path):
    """
    Reduces the frames of all GIF images in the specified folder to 25% of the original frames,
    discarding the other 75%.

    Parameters:
    - folder_path: The path to the folder containing the GIF images.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".gif"):
            original_path = os.path.join(folder_path, filename)
            reduced_path = os.path.join(folder_path, filename.rsplit('.', 1)[0] + "_reduced.gif")
            
            # Get the total number of frames in the GIF
            info_command = ['gifsicle', '--info', original_path]
            info_result = subprocess.run(info_command, capture_output=True, text=True)
            
            try:
                frames_line = next((line for line in info_result.stdout.split('\n') if 'images' in line), None)
                if not frames_line:
                    print(f"Could not determine the number of frames for {filename}")
                    continue  # Skip this file
                total_frames = int(frames_line.split(' ')[2])
                frames_to_keep = total_frames // 4  # Calculate 25% of total frames, keeping only this many
                
                # If the GIF has very few frames, you might end up with 0 frames to keep, ensure at least 1
                frames_to_keep = max(1, frames_to_keep)

                # Construct the command to keep only the first 25% of frames
                command = [
                    'gifsicle',
                    original_path,
                    '#0-{}'.format(frames_to_keep - 1),
                    '-o', reduced_path,
                ]
                
                subprocess.run(command, check=True)
                print(f"Frame-reduced GIF created: {reduced_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {filename}: {e}")


# Define the path to your media folder
newPath = input('path: ')
media_folder = newPath 
remove_frames_gif(newPath)
