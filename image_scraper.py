#!/usr/bin/env python3
"""
Image Scraper - A script to download all images from a website

Requirements:
- Python 3.6+
- requests
- beautifulsoup4
- tkinter (usually comes with Python)

You can install the required packages with:
pip install requests beautifulsoup4
"""

import os
import sys
import re
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import concurrent.futures
import time

def is_valid_url(url):
    """Check if the URL is valid."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def get_image_urls(url):
    """Extract all image URLs from a webpage."""
    try:
        # Send a GET request to the URL
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all img tags
        img_tags = soup.find_all('img')
        
        # Extract the 'src' attribute from each img tag
        img_urls = []
        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                # Handle relative URLs
                if not is_valid_url(img_url):
                    img_url = urljoin(url, img_url)
                img_urls.append(img_url)
            
            # Also check for 'data-src' attribute (lazy loading)
            data_src = img.get('data-src')
            if data_src:
                if not is_valid_url(data_src):
                    data_src = urljoin(url, data_src)
                img_urls.append(data_src)
        
        return img_urls
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []
    except Exception as e:
        print(f"Error parsing the webpage: {e}")
        return []

def download_image(img_url, save_dir, index):
    """Download an image and save it to the specified directory."""
    try:
        # Extract the filename from the URL
        filename = os.path.basename(urlparse(img_url).path)
        
        # If filename is empty or doesn't end with an image extension, create a default filename
        if not filename or not re.search(r'\.(jpg|jpeg|png|gif|bmp|webp|svg)$', filename, re.IGNORECASE):
            filename = f"image_{index}.jpg"
        
        # Ensure filename is unique
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(os.path.join(save_dir, filename)):
            filename = f"{base}_{counter}{ext}"
            counter += 1
        
        # Send a GET request to download the image
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        
        # Save the image to the specified directory
        with open(os.path.join(save_dir, filename), 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return True, filename
    
    except requests.exceptions.RequestException as e:
        return False, f"Failed to download {img_url}: {e}"
    except Exception as e:
        return False, f"Error saving {img_url}: {e}"

def select_directory():
    """Open a directory selection dialog and return the selected directory."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Open the directory selection dialog
    directory = filedialog.askdirectory(title="Select directory to save images")
    
    return directory

def main():
    try:
        # Get the URL from the user
        url = input("Enter the URL of the webpage to scrape images from: ").strip()
        
        # Validate the URL
        if not is_valid_url(url):
            print("Invalid URL. Please enter a valid URL including the protocol (e.g., https://example.com)")
            return
        
        # Get all image URLs from the webpage
        print(f"Fetching images from {url}...")
        img_urls = get_image_urls(url)
        
        if not img_urls:
            print("No images found on the webpage.")
            return
        
        print(f"Found {len(img_urls)} images.")
        
        # Select directory to save images
        print("Please select a directory to save the images...")
        save_dir = select_directory()
        
        if not save_dir:
            print("No directory selected. Exiting.")
            return
        
        # Download images
        print(f"Downloading {len(img_urls)} images to {save_dir}...")
        
        success_count = 0
        failed_count = 0
        
        # Use a thread pool to download images concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            # Start the download tasks
            future_to_url = {
                executor.submit(download_image, img_url, save_dir, i): img_url
                for i, img_url in enumerate(img_urls)
            }
            
            # Process the results as they complete
            for i, future in enumerate(concurrent.futures.as_completed(future_to_url)):
                success, result = future.result()
                if success:
                    success_count += 1
                    print(f"Downloaded ({i+1}/{len(img_urls)}): {result}")
                else:
                    failed_count += 1
                    print(f"Failed ({i+1}/{len(img_urls)}): {result}")
        
        # Print summary
        print("\nDownload Summary:")
        print(f"Total images found: {len(img_urls)}")
        print(f"Successfully downloaded: {success_count}")
        print(f"Failed to download: {failed_count}")
        print(f"Images saved to: {save_dir}")
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

