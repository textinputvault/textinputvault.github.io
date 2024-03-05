import os
import json

# Define the path to your media folder
media_folder = 'H:/Project/textinputvault.github.io/media/'

# Define the path for the output JSON file
output_json_file = 'imageList.json'

# List all files in the media folder
files = os.listdir(media_folder)

# Filter out image files (edit or add more extensions as needed)
image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Generate JSON content
json_content = json.dumps(image_files)

# Write the JSON content to a file
with open(output_json_file, 'w') as json_file:
    json_file.write(json_content)

print(f"JSON file '{output_json_file}' has been generated with {len(image_files)} image names.")
