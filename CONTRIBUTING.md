# Contributing to Image Scraper

Thank you for your interest in contributing to Image Scraper! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

1. **Check existing issues** first to avoid duplicates
2. **Use the issue template** when creating new issues
3. **Provide detailed information**:
   - Python version and operating system
   - Error messages or stack traces
   - URL you're trying to scrape (if not sensitive)
   - Steps to reproduce the issue
   - Expected vs actual behavior

### Feature Requests

1. **Search existing issues** for similar requests
2. **Describe the feature** clearly and explain the use case
3. **Consider the scope** - keep features focused and relevant
4. **Be open to discussion** about implementation approaches

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Write your code** following the style guidelines below
4. **Test your changes** thoroughly
5. **Commit your changes** with clear, descriptive messages
6. **Push to your fork**: `git push origin feature/your-feature-name`
7. **Create a Pull Request** with a clear description

## 📋 Development Guidelines

### Code Style

- **Follow PEP 8** Python style guidelines
- **Use meaningful variable names** and function names
- **Add docstrings** to all functions and classes
- **Include type hints** where appropriate
- **Handle errors gracefully** with proper exception handling
- **Use consistent indentation** (4 spaces)

### Code Structure

```python
#!/usr/bin/env python3
"""
Module description.

Brief description of what this module does.
"""

import standard_library_modules
import third_party_modules
import local_modules

# Global constants
CONSTANT_NAME = "value"

def function_name(param: type) -> return_type:
    """Function description.
    
    Args:
        param: Parameter description
        
    Returns:
        Return value description
        
    Raises:
        ExceptionType: When this exception is raised
    """
    # Function implementation
    pass

class ClassName:
    """Class description."""
    
    def __init__(self, param: type) -> None:
        """Initialize the class."""
        pass

if __name__ == "__main__":
    main()
```

### Error Handling

- Always handle exceptions appropriately
- Provide meaningful error messages
- Log errors with appropriate severity levels
- Don't suppress exceptions without good reason

### Logging

Use the existing logging configuration:
```python
import logging
logger = logging.getLogger(__name__)

# Use appropriate log levels
logger.debug("Debug information")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical error")
```

## 🧪 Testing

### Manual Testing

1. **Test with different websites** to ensure compatibility
2. **Test all features** including optimization and error handling
3. **Test edge cases** like no images, invalid URLs, network issues
4. **Verify logging output** is clear and helpful

### Automated Testing

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=image_scraper

# Run type checking
mypy image_scraper.py

# Run code formatting check
black --check image_scraper.py
flake8 image_scraper.py
```

### Test Cases to Consider

- Valid and invalid URLs
- Websites with no images
- Websites with many images
- Different image formats
- Network connectivity issues
- Permission errors
- Disk space issues

## 📝 Documentation

### Code Comments

- Comment complex algorithms or business logic
- Explain non-obvious decisions
- Use TODO comments for planned improvements
- Keep comments up to date with code changes

### README Updates

- Update feature lists for new functionality
- Add new usage examples
- Update installation instructions if needed
- Keep screenshots and examples current

### Commit Messages

Follow conventional commit format:
```
type(scope): description

Examples:
feat: add batch processing support
fix: handle connection timeout errors
docs: update installation instructions
refactor: improve error handling
test: add unit tests for URL validation
perf: optimize image download speed
```

**Commit Types:**
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `perf`: Performance improvements
- `chore`: Maintenance tasks

## 🔧 Development Setup

### Prerequisites

```bash
# Python 3.6+
python --version

# Git
git --version

# Virtual environment (recommended)
python -m venv image_scraper_env
source image_scraper_env/bin/activate  # Linux/Mac
# or
image_scraper_env\Scripts\activate  # Windows
```

### Setup Development Environment

```bash
# Clone your fork
git clone https://github.com/yourusername/image-scraper.git
cd image-scraper

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks (optional)
pre-commit install
```

### Code Quality Tools

```bash
# Format code
black image_scraper.py

# Sort imports
isort image_scraper.py

# Check code style
flake8 image_scraper.py

# Type checking
mypy image_scraper.py

# Run all checks
./scripts/check_code.sh  # If available
```

## 🎯 Areas for Contribution

### High Priority

- [ ] Command-line interface with argparse
- [ ] Batch processing from URL lists
- [ ] Resume interrupted downloads
- [ ] Image filtering by size/format
- [ ] Unit tests and test coverage

### Medium Priority

- [ ] GUI application using tkinter
- [ ] Configuration file support
- [ ] Website-specific scrapers
- [ ] Progress bar for downloads
- [ ] Docker containerization

### Low Priority

- [ ] Plugin system for custom scrapers
- [ ] Image metadata extraction
- [ ] Duplicate image detection
- [ ] Image format conversion
- [ ] Integration with cloud storage

## 📞 Getting Help

### Communication Channels

1. **GitHub Issues** - For bugs and feature requests
2. **GitHub Discussions** - For questions and general discussion
3. **Pull Request Comments** - For code review and technical discussion

### Questions

If you have questions about:
- **Code structure**: Ask in the relevant pull request or issue
- **Feature decisions**: Open a GitHub discussion
- **Implementation details**: Comment on the specific code section
- **Development setup**: Check existing issues or create a new one

## 🚀 Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in a backwards compatible manner
- **PATCH**: Backwards compatible bug fixes

### Release Checklist

1. Update version number
2. Update CHANGELOG.md
3. Run full test suite
4. Update documentation
5. Create release notes
6. Tag the release
7. Update PyPI package (if applicable)

## 🏆 Recognition

Contributors will be recognized in:
- README.md acknowledgments section
- Release notes for significant contributions
- GitHub contributor statistics
- Special mentions in documentation

## 📄 License

By contributing to Image Scraper, you agree that your contributions will be licensed under the MIT License.

## 🌟 Code of Conduct

### Our Pledge

We are committed to making participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

---

Thank you for contributing to Image Scraper! 🚀
