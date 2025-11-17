
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) ![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg) 


#### This package is maintained version of [MuhammadAmir5670/psx-feed](https://github.com/MuhammadAmir5670/psx-feed)

# psx-feed
with psx-feed, you can scrape the data of Pakistan stock exchange. psx-feed is super easy to use and handles everything for you. Just specify which company's stock data you want and how much you want, and the rest is done for you.


## Overview 
The psx-feed was written with fast use in mind. It provides the following key features

- can scrape all historical data till current date
- can scrape data for of multiple companies in a single line of code
- returns a `Pandas DataFrame` for the scraped data
- for better download speed, It does not request the complete data in a single network request rather it makes chunks of data to be downloaded and uses threads to open requests for different chunks of data, hence results in better speed

In the following paragraphs, I am going to describe how you can get and use Scrapeasy for your own projects.


## Installation

To get psx-feed, either fork this github repo or simply use Pypi via pip.

```bash
$ pip install psx-feed
```

## Local Development Setup

If you want to contribute to the project or modify it for your own needs, follow these steps to set up a local development environment:

### Prerequisites

- Python 3.4 or higher
- pip (Python package installer)
- git (for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone git@github.com:abdur1547/psx-feed.git

cd psx-feed
```

### Step 2: Create a Virtual Environment (Recommended)

Create an isolated Python environment to avoid conflicts with other projects:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Step 3: Install in Development Mode

Install the package in development mode along with all dependencies:

```bash
# Basic installation (editable mode)
pip install -e .

# Install with development dependencies (recommended for contributors)
pip install -e .[dev]

# Install with visualization dependencies
pip install -e .[viz]

# Install everything (dev + visualization)
pip install -e .[all]

# Alternative: Install from requirements files
pip install -e . && pip install -r requirements-dev.txt
```

This installs the package in "editable" mode, meaning any changes you make to the source code will be immediately available without reinstalling.

### Step 4: Verify Installation

Test that the installation works correctly:

```python
# Run this in Python interpreter or create a test script
from psx import stocks, tickers
import datetime

# Get all available tickers
all_tickers = tickers()
print(f"Found {len(all_tickers)} tickers")

# Test downloading sample data
data = stocks("SILK", start=datetime.date(2023, 1, 1), end=datetime.date(2023, 1, 31))
print(f"Downloaded {len(data)} rows of data for SILK")
```

### Step 5: Project Structure

```
psx-feed/
├── src/
│   └── psx/
│       ├── __init__.py      # Package initialization and exports
│       ├── web.py           # Main data scraping functionality
│       └── example.py       # Example usage with plotly visualization
├── demo/
│   ├── example.py           # Plotly visualization example
│   └── simple_example.py    # Basic example without visualization
├── requirements-dev.txt     # Development dependencies
├── requirements-viz.txt     # Visualization dependencies
├── pyproject.toml          # Modern Python packaging configuration (recommended)
├── setup.py                # Legacy packaging configuration (deprecated)
├── README.md               # This file
├── LICENSE                 # MIT license
└── images/                 # Example graphs and visualizations
```

### Step 6: Making Changes

1. **Edit the source code** in the `src/psx/` directory
2. **Test your changes** by running the example or your own test scripts
3. **Create visualizations** using the example in `src/psx/example.py`

### Step 7: Dependency Management

#### Core Dependencies (automatically installed)
The package automatically installs these core dependencies:

- **pandas** - Data manipulation and analysis
- **tqdm** - Progress bars for downloads
- **beautifulsoup4** - HTML parsing for web scraping
- **requests** - HTTP library for making web requests

#### Optional Dependencies

**Visualization extras** (`[viz]`):
```bash
pip install psx-feed[viz]
# Includes: plotly, matplotlib, seaborn
```

**Development extras** (`[dev]`):
```bash
pip install psx-feed[dev]
# Includes: pytest, black, flake8, mypy, sphinx, jupyter, etc.
```

#### Requirements Files

For development, you can also use the requirements files:

- **`requirements-dev.txt`** - Development tools (testing, linting, docs)
- **`requirements-viz.txt`** - Visualization libraries

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install visualization dependencies
pip install -r requirements-viz.txt
```

#### Modern Python Packaging

This project now uses **`pyproject.toml`** (the modern standard) for package configuration instead of the legacy `setup.py`. The `pyproject.toml` file includes:

- ✅ **Modern packaging standards** (PEP 518, PEP 621)
- ✅ **Tool configurations** (black, isort, mypy, pytest)
- ✅ **Better dependency management**
- ✅ **Enhanced metadata** and project URLs
- ✅ **Improved Python version support** (3.8+)

The old `setup.py` is kept for compatibility but `pyproject.toml` is now the primary configuration.

#### Why No requirements.txt?

For **pip packages**, dependencies are properly managed through `setup.py`'s `install_requires` and `extras_require`. A `requirements.txt` file is typically used for applications, not libraries. This approach:

- ✅ Allows users to install only what they need
- ✅ Enables optional features through extras
- ✅ Follows Python packaging best practices
- ✅ Avoids dependency conflicts in user environments

### Step 8: Contributing

1. **Fork** the repository on GitHub
2. **Create a feature branch** (`git checkout -b feature/new-feature`)
3. **Make your changes** and test them thoroughly
4. **Commit your changes** (`git commit -am 'Add new feature'`)
5. **Push to the branch** (`git push origin feature/new-feature`)
6. **Create a Pull Request** on GitHub

### Troubleshooting

- **Import errors**: Make sure you've activated your virtual environment and installed in development mode
- **Network issues**: The package requires internet access to scrape PSX data
- **Missing data**: Some historical data might not be available for certain stocks

### Development Tips

- Use `python -m psx.example` to run the example visualization
- Modify `src/psx/web.py` to add new scraping functionality
- Test with different stock symbols and date ranges
- Consider adding error handling for network timeouts

### Building and Publishing

This project uses modern Python packaging with `pyproject.toml`:

```bash
# Build the package
python -m build

# Install build tools
pip install build twine

# Test the build
./build_test.sh

# Upload to PyPI (when ready)
twine upload dist/*
```

### Package Testing

```bash
# Test basic functionality
python demo/simple_example.py

# Test with visualizations (requires [viz] extras)
python demo/example.py
```

## Usage

First, import stocks and tickers from psx

```
from psx import stocks, tickers
```

to get the information of all the companies in Pakistan stock Exchange....

```
tickers = tickers()
```


to scrape the data of **Silk Bank Limited** we have pass its ticker (symbol) to the `stocks` method with proper start and end date. and it will return a DataFrame with the scraped data

```
data = stocks("SILK", start=datetime.date(2020, 1, 1), end=datetime.date.today())
```


we can also download the data of multiple companies in a single call to `stocks` method by passing a list or tuple of symbols


```
data = stocks(["SILK", "PACE"], start=datetime.date(2020, 1, 1), end=datetime.date.today())
```

and now the returned DataFrame object will have a hierarchical index on rows.

## Example Graph

<img src ="images/newplot-2.png">
<img src ="images/newplot-3.png">
<img src ="images/newplot-4.png">
<img src ="images/newplot-5.png">


## Author Info
<p align="left">
<a href="mailto:muhammmadamir5670@gmail.com"><img src="https://img.icons8.com/fluent/40/000000/gmail-new.png"/></a>
<a href = "https://www.linkedin.com/in/muhammad-amir-9826b71b5/"><img src="https://img.icons8.com/fluent/40/000000/linkedin.png"/></a>
<a href = "https://twitter.com/Daniyal60990408/"><img src="https://img.icons8.com/fluent/40/000000/twitter.png"/></a>
<a href="https://www.facebook.com/daniyal.abbasi.1610/">
<img src="https://img.icons8.com/fluent/40/000000/facebook-new.png">
</a>
<a href = "https://www.instagram.com/the_infamous_abbasi/"><img src="https://img.icons8.com/fluent/40/000000/instagram-new.png"/></a>
</p>



<!-- Security scan triggered at 2025-09-02 02:41:43 -->

<!-- Security scan triggered at 2025-09-07 01:38:06 -->

<!-- Security scan triggered at 2025-09-09 05:18:41 -->

<!-- Security scan triggered at 2025-09-28 15:21:44 -->

<!-- Security scan triggered at 2025-10-08 08:55:17 -->
