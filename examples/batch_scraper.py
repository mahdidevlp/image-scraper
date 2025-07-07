#!/usr/bin/env python3
"""
Batch Image Scraper Example

This script demonstrates how to scrape images from multiple URLs
using the Image Scraper functionality.

Usage:
    python batch_scraper.py urls.txt output_directory
"""

import os
import sys
import argparse
from pathlib import Path

# Add parent directory to path to import image_scraper
sys.path.insert(0, str(Path(__file__).parent.parent))

from image_scraper import get_image_urls, download_image
import concurrent.futures
import logging

def setup_logging():
    """Setup logging for batch processing."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('batch_scraper.log')
        ]
    )
    return logging.getLogger(__name__)

def read_urls(file_path):
    """Read URLs from a text file."""
    urls = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                url = line.strip()
                if url and not url.startswith('#'):
                    urls.append(url)
        return urls
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def scrape_url(url, base_output_dir, optimize=False):
    """Scrape images from a single URL."""
    logger = logging.getLogger(__name__)
    logger.info(f"Processing URL: {url}")
    
    # Get images from URL
    img_urls = get_image_urls(url)
    
    if not img_urls:
        logger.warning(f"No images found at {url}")
        return 0, 0
    
    # Create subdirectory for this URL
    url_dir = url.replace('https://', '').replace('http://', '').replace('/', '_')
    output_dir = os.path.join(base_output_dir, url_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    logger.info(f"Found {len(img_urls)} images. Downloading to {output_dir}")
    
    # Download images
    success_count = 0
    failed_count = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(download_image, img_url, output_dir, i, optimize): img_url
            for i, img_url in enumerate(img_urls)
        }
        
        for future in concurrent.futures.as_completed(futures):
            success, result = future.result()
            if success:
                success_count += 1
                logger.info(f"Downloaded: {result}")
            else:
                failed_count += 1
                logger.error(f"Failed: {result}")
    
    logger.info(f"URL {url} completed: {success_count} success, {failed_count} failed")
    return success_count, failed_count

def main():
    """Main function for batch processing."""
    parser = argparse.ArgumentParser(description='Batch Image Scraper')
    parser.add_argument('urls_file', help='Text file containing URLs (one per line)')
    parser.add_argument('output_dir', help='Output directory for downloaded images')
    parser.add_argument('--optimize', action='store_true', help='Optimize downloaded images')
    parser.add_argument('--max-sites', type=int, default=None, help='Maximum number of sites to process')
    
    args = parser.parse_args()
    
    logger = setup_logging()
    
    # Read URLs
    urls = read_urls(args.urls_file)
    if not urls:
        logger.error("No valid URLs found.")
        return
    
    if args.max_sites:
        urls = urls[:args.max_sites]
    
    logger.info(f"Starting batch processing of {len(urls)} URLs")
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Process URLs
    total_success = 0
    total_failed = 0
    
    for i, url in enumerate(urls, 1):
        logger.info(f"Processing site {i}/{len(urls)}: {url}")
        try:
            success, failed = scrape_url(url, args.output_dir, args.optimize)
            total_success += success
            total_failed += failed
        except Exception as e:
            logger.error(f"Error processing {url}: {e}")
            total_failed += 1
    
    # Summary
    logger.info("="*50)
    logger.info("BATCH PROCESSING SUMMARY")
    logger.info("="*50)
    logger.info(f"Total URLs processed: {len(urls)}")
    logger.info(f"Total images downloaded: {total_success}")
    logger.info(f"Total failures: {total_failed}")
    logger.info(f"Output directory: {args.output_dir}")

if __name__ == "__main__":
    main()
