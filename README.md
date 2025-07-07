# Image Scraper

A powerful and user-friendly Python tool to scrape and download images from websites with optional optimization features. Perfect for bulk image downloading, research, and content collection.

## 🚀 Features

- **Bulk Image Downloading**: Download all images from any webpage
- **Smart URL Detection**: Automatically handles relative and absolute URLs
- **Lazy Loading Support**: Detects and downloads lazy-loaded images (`data-src`)
- **Image Optimization**: Optional compression to reduce file sizes
- **Concurrent Downloads**: Fast multi-threaded downloading
- **GUI Directory Selection**: Easy-to-use file dialog for choosing save location
- **Duplicate Prevention**: Automatic filename collision handling
- **Comprehensive Logging**: Detailed logs with timestamps
- **Progress Tracking**: Real-time download progress and statistics
- **Error Handling**: Robust error recovery and reporting

## 📋 Requirements

- **Python 3.6+**
- **Required packages:**
  - `requests` - HTTP library for downloading
  - `beautifulsoup4` - HTML parsing
  - `pillow` - Image processing (optional, for optimization)
  - `tkinter` - GUI components (usually included with Python)

## 📦 Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/mahdidevlp/image-scraper.git
cd image-scraper

# Install dependencies
pip install -r requirements.txt

# Run the script
python image_scraper.py
```

### Using Virtual Environment (Recommended)

```bash
# Clone and setup
git clone https://github.com/mahdidevlp/image-scraper.git
cd image-scraper

# Create virtual environment
python -m venv image_scraper_env

# Activate virtual environment
source image_scraper_env/bin/activate  # Linux/Mac
# or
image_scraper_env\\Scripts\\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the script
python image_scraper.py
```

### System-wide Installation

```bash
# Make script executable
chmod +x image_scraper.py

# Create symbolic link (optional)
sudo ln -s $(pwd)/image_scraper.py /usr/local/bin/image-scraper

# Run from anywhere
image-scraper
```

## 🎯 Usage

### Interactive Mode

Simply run the script and follow the prompts:

```bash
python image_scraper.py
```

The script will ask you for:
1. **Website URL** - The webpage to scrape images from
2. **Optimization preference** - Whether to compress images
3. **Save directory** - Where to save the downloaded images

### Example Session

```
Enter the webpage URL to scrape images from: https://example.com/gallery
Optimize images to reduce file size? (y/n): y
[GUI dialog opens for directory selection]

2025-01-07 15:30:45 [INFO] Fetching images from https://example.com/gallery
2025-01-07 15:30:46 [INFO] Found 25 images.
2025-01-07 15:30:46 [INFO] Downloading 25 images to /home/user/Downloads/images
2025-01-07 15:30:47 [INFO] (1/25) Downloaded: gallery_image_001.jpg
2025-01-07 15:30:47 [INFO] (2/25) Downloaded: photo_002.png
...
2025-01-07 15:31:15 [INFO] Download Summary:
2025-01-07 15:31:15 [INFO] Total images found: 25
2025-01-07 15:31:15 [INFO] Successfully downloaded: 23
2025-01-07 15:31:15 [INFO] Failed to download: 2
2025-01-07 15:31:15 [INFO] Images saved to: /home/user/Downloads/images
```

## ⚙️ Features in Detail

### 🔍 **Smart Image Detection**
- Finds images in `<img>` tags with `src` attributes
- Detects lazy-loaded images using `data-src` attributes
- Handles both relative and absolute URLs
- Removes duplicate URLs automatically

### 🚀 **Concurrent Downloads**
- Downloads up to 5 images simultaneously
- Significantly faster than sequential downloading
- Configurable thread pool size

### 🎨 **Image Optimization**
- Optional JPEG compression (85% quality)
- Converts RGBA/LA images to RGB
- Reduces file sizes by 20-50% typically
- Preserves image quality while saving space

### 📁 **File Management**
- Automatic filename generation for images without extensions
- Collision detection and automatic renaming
- Preserves original filenames when possible
- Creates directories automatically

### 📊 **Logging and Progress**
- Real-time progress tracking
- Detailed error reporting
- Timestamped log files
- Console and file logging

## 🛠️ Configuration

### Modifying Download Settings

You can customize the script behavior by editing these variables:

```python
# In download_image function
max_workers = 5  # Concurrent download threads
timeout = 10     # Request timeout in seconds
chunk_size = 8192  # Download chunk size

# In optimize_image function
quality = 85     # JPEG compression quality (1-100)
optimize = True  # Enable PIL optimization
```

### Adding Custom Headers

Modify the headers in `get_image_urls()` function:

```python
headers = {
    'User-Agent': 'Your Custom User Agent',
    'Referer': 'https://example.com',
    # Add more headers as needed
}
```

## 📸 Supported Image Formats

- **JPEG/JPG** - Full support with optimization
- **PNG** - Full support with RGBA conversion
- **GIF** - Download only (no optimization)
- **BMP** - Full support
- **WebP** - Full support
- **TIFF** - Download support

## 🔧 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   ```bash
   pip install requests beautifulsoup4 pillow
   ```

2. **Permission denied errors**
   ```bash
   chmod +x image_scraper.py
   ```

3. **No images found**
   - Check if the website uses JavaScript to load images
   - Try a different webpage
   - Verify the URL is accessible

4. **Download failures**
   - Some websites block automated requests
   - Images might be behind authentication
   - Check internet connection

### Debug Mode

Enable debug logging by modifying the logging level:

```python
logging.basicConfig(level=logging.DEBUG)
```

## 🚀 Advanced Usage

### Command Line Arguments (Future Enhancement)

```bash
# Planned features
python image_scraper.py --url https://example.com --output ./images --optimize --max-workers 10
```

### Batch Processing

Create a list of URLs in a text file and process them:

```python
# Create urls.txt with one URL per line
# Run batch processing script (see examples/)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Install development dependencies: `pip install -r requirements-dev.txt`
4. Make your changes and add tests
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include error handling
- Write unit tests for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Beautiful Soup** - HTML parsing library
- **Requests** - HTTP library for Python
- **Pillow** - Python Imaging Library
- **Tkinter** - GUI toolkit

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/mahdidevlp/image-scraper/issues) page
2. Create a new issue with:
   - Python version and OS
   - Error messages or logs
   - URL you're trying to scrape (if not sensitive)
   - Steps to reproduce the issue

## 🗺️ Roadmap

- [ ] Command-line interface with arguments
- [ ] Batch processing from URL lists
- [ ] GUI application using tkinter
- [ ] Website-specific scrapers (Instagram, Pinterest, etc.)
- [ ] Image filtering by size/format
- [ ] Resume interrupted downloads
- [ ] Configuration file support
- [ ] Docker container
- [ ] Progress bar for GUI mode

## 📊 Performance

**Typical Performance:**
- **Small images (< 100KB)**: 10-20 images/second
- **Medium images (100KB-1MB)**: 5-10 images/second  
- **Large images (> 1MB)**: 2-5 images/second

**Factors affecting speed:**
- Internet connection speed
- Server response time
- Image file sizes
- Number of concurrent workers

---

**Made with ❤️ for content creators and researchers**
