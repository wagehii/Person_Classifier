import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve

# Create a folder to save images
if not os.path.exists('Salah'):
    os.makedirs('Salah')

# URL of the page containing image results
url = 'https://www.google.com/search?tbm=isch&q=mohamed+salah+egypt'  # Replace this with the actual URL

# Send a GET request to load the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <img> tags to extract image URLs
image_tags = soup.find_all('img')

# Print the number of images found
print(f'Found {len(image_tags)} images.')

# Download the first 50 images
downloaded_count = 0
for i, img in enumerate(image_tags[:50]):
    img_url = img.get('src')
    
    # Skip if the URL is missing
    if not img_url:
        print(f'Skipping image {i+1}: URL is missing.')
        continue
    
    # Convert relative URLs to absolute URLs
    img_url = urljoin(url, img_url)
    
    try:
        # Download and save the image
        urlretrieve(img_url, f'Salah/salah{i+72}.jpg')
        print(f'Downloaded image {i+1}: {img_url}')
        downloaded_count += 1
    except Exception as e:
        print(f'Failed to download image {i+1}: {img_url} - {e}')

print(f'Successfully downloaded {downloaded_count} images.')