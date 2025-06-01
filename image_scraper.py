#!/usr/bin/env python3
"""
Image Scraper - Downloads images from a website with optional optimization.

Requirements:
- Python 3.6+
- requests
- beautifulsoup4
- pillow (for image optimization)
- tkinter (usually included with Python)

Install dependencies:
pip install requests beautifulsoup4 pillow
"""

import os
import sys
import re
import logging
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import concurrent.futures
from datetime import datetime
try:
    from PIL import Image
    PILLOW_AVAILABLE = True
except ImportError:
    PILLOW_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(f'image_scraper_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    ]
)
logger = logging.getLogger(__name__)

def is_valid_url(url):
    """Validate if the provided URL is well-formed."""
    try:
        result = urlparse(url)
        return all([result.scheme in ('http', 'https'), result.netloc])
    except ValueError:
        return False

def get_image_urls(url):
    """Extract all image URLs from a webpage."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        img_urls = set()  # Use set to avoid duplicates
        for img in soup.find_all('img'):
            # Check 'src' attribute
            src = img.get('src')
            if src:
                src = urljoin(url, src) if not is_valid_url(src) else src
                img_urls.add(src)
            # Check 'data-src' for lazy-loaded images
            data_src = img.get('data-src')
            if data_src:
                data_src = urljoin(url, data_src) if not is_valid_url(data_src) else data_src
                img_urls.add(data_src)
        
        return list(img_urls)
    
    except requests.RequestException as e:
        logger.error(f"Failed to fetch webpage {url}: {e}")
        return []
    except Exception as e:
        logger.error(f"Error parsing webpage {url}: {e}")
        return []

def optimize_image(image_path):
    """Optimize image using Pillow to reduce file size."""
    if not PILLOW_AVAILABLE:
        logger.warning("Pillow not installed, skipping optimization.")
        return
    
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary (e.g., for PNG with transparency)
            if img.mode in ('RGBA', 'LA'):
                img = img.convert('RGB')
            # Optimize and save with reduced quality
            img.save(image_path, optimize=True, quality=85)
            logger.info(f"Optimized image: {image_path}")
    except Exception as e:
        logger.error(f"Failed to optimize {image_path}: {e}")

def download_image(img_url, save_dir, index, optimize=False):
    """Download and optionally optimize an image."""
    try:
        filename = os.path.basename(urlparse(img_url).path)
        # Default filename if none or invalid extension
        if not filename or not re.search(r'\.(jpg|jpeg|png|gif|bmp|webp)$', filename, re.IGNORECASE):
            filename = f"image_{index:04d}.jpg"
        
        # Ensure unique filename
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(os.path.join(save_dir, filename)):
            filename = f"{base}_{counter:04d}{ext}"
            counter += 1
        
        file_path = os.path.join(save_dir, filename)
        
        # Download image
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Optimize image if requested
        if optimize and PILLOW_AVAILABLE:
            optimize_image(file_path)
        
        return True, filename
    
    except requests.RequestException as e:
        return False, f"Failed to download {img_url}: {e}"
    except Exception as e:
        return False, f"Error processing {img_url}: {e}"

def select_directory():
    """Prompt user to select a directory for saving images."""
    try:
        root = tk.Tk()
        root.withdraw()
        directory = filedialog.askdirectory(title="Select Directory to Save Images")
        root.destroy()
        return directory
    except Exception as e:
        logger.error(f"Error selecting directory: {e}")
        return None

def get_user_input():
    """Get URL and optimization preference from user."""
    url = input("Enter the webpage URL to scrape images from: ").strip()
    if not is_valid_url(url):
        logger.error("Invalid URL. Please include protocol (e.g., https://example.com).")
        return None, None
    
    optimize = False
    if PILLOW_AVAILABLE:
        while True:
            choice = input("Optimize images to reduce file size? (y/n): ").strip().lower()
            if choice in ('y', 'n'):
                optimize = choice == 'y'
                break
            logger.warning("Please enter 'y' or 'n'.")
    
    return url, optimize

def main():
    """Main function to orchestrate image scraping."""
    try:
        # Get user input
        url, optimize = get_user_input()
        if not url:
            return
        
        # Fetch image URLs
        logger.info(f"Fetching images from {url}")
        img_urls = get_image_urls(url)
        
        if not img_urls:
            logger.info("No images found on the webpage.")
            return
        
        logger.info(f"Found {len(img_urls)} images.")
        
        # Select save directory
        save_dir = select_directory()
        if not save_dir:
            logger.info("No directory selected. Exiting.")
            return
        
        # Create directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)
        
        # Download images concurrently
        logger.info(f"Downloading {len(img_urls)} images to {save_dir}")
        success_count = 0
        failed_count = 0
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = {
                executor.submit(download_image, img_url, save_dir, i, optimize): img_url
                for i, img_url in enumerate(img_urls)
            }
            
            for i, future in enumerate(concurrent.futures.as_completed(futures)):
                success, result = future.result()
                if success:
                    success_count += 1
                    logger.info(f"({i+1}/{len(img_urls)}) Downloaded: {result}")
                else:
                    failed_count += 1
                    logger.error(f"({i+1}/{len(img_urls)}) {result}")
        
        # Log summary
        logger.info("\nDownload Summary:")
        logger.info(f"Total images found: {len(img_urls)}")
        logger.info(f"Successfully downloaded: {success_count}")
        logger.info(f"Failed to download: {failed_count}")
        logger.info(f"Images saved to: {save_dir}")
    
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
