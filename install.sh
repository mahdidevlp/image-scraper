#!/bin/bash

# Image Scraper Installation Script
# Installs dependencies and sets up the image scraper

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

SCRIPT_NAME="image_scraper.py"
INSTALL_PATH="/usr/local/bin/image-scraper"
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}Image Scraper Installation Script${NC}"
echo "=================================="
echo

# Check if script exists
if [[ ! -f "$CURRENT_DIR/$SCRIPT_NAME" ]]; then
    echo -e "${RED}Error: $SCRIPT_NAME not found in current directory${NC}"
    echo "Please run this script from the project directory."
    exit 1
fi

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 is required but not installed${NC}"
    echo "Please install Python 3.6 or later"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "${GREEN}Found Python $PYTHON_VERSION${NC}"

# Check pip installation
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}pip3 is required but not installed${NC}"
    echo "Please install pip3"
    exit 1
fi

# Install dependencies
echo -e "${BLUE}Installing Python dependencies...${NC}"
if [[ -f "$CURRENT_DIR/requirements.txt" ]]; then
    pip3 install -r "$CURRENT_DIR/requirements.txt"
else
    echo -e "${YELLOW}requirements.txt not found, installing individual packages${NC}"
    pip3 install requests beautifulsoup4 pillow
fi

# Make script executable
chmod +x "$CURRENT_DIR/$SCRIPT_NAME"

# System-wide installation (optional)
if [[ $EUID -eq 0 ]]; then
    echo -e "${BLUE}Installing system-wide...${NC}"
    
    # Create backup if file already exists
    if [[ -f "$INSTALL_PATH" ]]; then
        echo -e "${YELLOW}Existing installation found. Creating backup...${NC}"
        cp "$INSTALL_PATH" "$INSTALL_PATH.backup.$(date +%Y%m%d_%H%M%S)"
        echo -e "${GREEN}Backup created${NC}"
    fi
    
    # Install the script
    cp "$CURRENT_DIR/$SCRIPT_NAME" "$INSTALL_PATH"
    
    if [[ -f "$INSTALL_PATH" && -x "$INSTALL_PATH" ]]; then
        echo -e "${GREEN}✓ System-wide installation successful!${NC}"
        echo "You can now use 'image-scraper' from anywhere"
    else
        echo -e "${RED}✗ System-wide installation failed${NC}"
    fi
else
    echo -e "${YELLOW}Run with sudo for system-wide installation${NC}"
fi

# Test installation
echo -e "${BLUE}Testing installation...${NC}"
if python3 "$CURRENT_DIR/$SCRIPT_NAME" --help > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Installation test passed${NC}"
elif python3 -c "import requests, bs4; from PIL import Image; import tkinter" > /dev/null 2>&1; then
    echo -e "${GREEN}✓ All dependencies installed successfully${NC}"
else
    echo -e "${RED}✗ Some dependencies may be missing${NC}"
    echo "Try running: pip3 install requests beautifulsoup4 pillow"
fi

echo
echo -e "${GREEN}Image Scraper installation complete!${NC}"
echo
echo -e "${BLUE}Usage:${NC}"
echo "  python3 $SCRIPT_NAME"
if [[ -f "$INSTALL_PATH" ]]; then
    echo "  image-scraper"
fi
echo
echo -e "${BLUE}Examples:${NC}"
echo "  cd examples && python3 batch_scraper.py sample_urls.txt ./output"
echo
echo -e "${YELLOW}Note: Always respect website terms of service and robots.txt${NC}"
