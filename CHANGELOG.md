# Changelog

All notable changes to Image Scraper will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-07

### Added
- Initial release of Image Scraper
- Bulk image downloading from any webpage
- Smart URL detection for relative and absolute URLs
- Lazy loading support for `data-src` attributes
- Optional image optimization using Pillow
- Concurrent downloads with configurable thread pool
- GUI directory selection using tkinter
- Comprehensive logging with timestamps
- Automatic filename collision handling
- Progress tracking and download statistics
- Support for multiple image formats (JPEG, PNG, GIF, BMP, WebP, TIFF)
- Robust error handling and recovery

### Features
- **Smart Image Detection**: Finds images in `<img>` tags with both `src` and `data-src` attributes
- **Concurrent Downloads**: Downloads up to 5 images simultaneously for faster performance
- **Image Optimization**: Optional JPEG compression with 85% quality to reduce file sizes
- **File Management**: Automatic filename generation and collision detection
- **Logging System**: Detailed console and file logging with multiple severity levels
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **User-Friendly**: Interactive prompts and GUI file dialogs

### Technical Details
- **Python 3.6+** compatibility
- **Dependencies**: requests, beautifulsoup4, pillow, tkinter
- **Concurrent Processing**: ThreadPoolExecutor with 5 workers
- **Error Handling**: Comprehensive exception handling for network and file operations
- **Logging**: Rotating log files with timestamps
- **Performance**: Optimized for speed and reliability

### Supported Websites
- Any website with `<img>` tags
- Lazy-loaded images using `data-src`
- Both HTTP and HTTPS protocols
- Relative and absolute image URLs

### Installation Methods
- Direct Python execution
- Virtual environment setup
- System-wide installation with symbolic links
- Requirements-based dependency management

---

## Future Releases

### Planned Features
- Command-line interface with argparse
- Batch processing from URL lists
- GUI application using tkinter
- Resume interrupted downloads
- Image filtering by size and format
- Configuration file support
- Website-specific scrapers (Instagram, Pinterest, etc.)
- Progress bars for better user experience
- Docker containerization
- PyPI package distribution

### Performance Improvements
- Adaptive concurrent worker scaling
- Bandwidth throttling options
- Memory usage optimization
- Caching mechanisms

### User Experience Enhancements
- Real-time progress bars
- Better error messages
- Configuration wizards
- Integration with popular browsers
- Cloud storage support
