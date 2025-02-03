from PIL import Image, ImageSequence
import os 

def skip_frames_gif(input_gif_path, output_gif_path):
    # Open the input gif file
    with Image.open(input_gif_path) as img:
        # Extract every other frame from the gif
        frames = [frame.copy() for i, frame in enumerate(ImageSequence.Iterator(img)) if i % 2 == 0]
        
        # Save frames to a new gif
        frames[0].save(
            output_gif_path,
            save_all=True,
            append_images=frames[1:],
            duration=img.info['duration'] * 2, # Adjust frame display duration
            loop=0,
            optimize=True
        )

# Main 
myGifPath = input('path: ')
files = os.listdir(myGifPath)
for i, file in enumerate(files):
    if ".gif" in file:
        input_gif = file 
        output_gif = myGifPath + '/' + file + '_skip.gif'
        skip_frames_gif(myGifPath + '/' +input_gif, output_gif)
        print(str(i / len(files) * 100) + " %")