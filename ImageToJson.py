# Import Libraries
import json
from PIL import Image

# Get Image Data
image = Image.open("Image.jpg")
width, height = image.size

# Setup JSON
image_data = {
    "pixels": list(image.getdata()),

    "dimensions": {
        "width": width,
        "height": height
    }
}

# Export to JSON
with open("output.json", 'w') as output:
    json.dump(image_data, output)
