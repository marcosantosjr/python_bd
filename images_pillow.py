import requests
from PIL import Image
from io import BytesIO
import os

# List of image URLs
image_urls = [
    "https://picsum.photos/400",
    "https://picsum.photos/500",
    "https://picsum.photos/600"
]

# Create a folder to save resized images
os.makedirs("resized_images", exist_ok=True)

# Download, resize, and save images
for i, url in enumerate(image_urls):
    response = requests.get(url)

    if response.status_code == 200:
        # Open image using PIL
        img = Image.open(BytesIO(response.content))

        # Resize the image to 300x300
        resized_img = img.resize((300, 300))

        # Save the resized image
        resized_img.save(f"resized_images/image_{i + 1}.jpg")
        print(f"Image {i + 1} saved successfully.")
    else:
        print(f"Failed to download image {i + 1}.")
