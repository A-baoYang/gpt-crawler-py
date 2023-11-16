# Python GPT Crawler
English | [繁體中文](README-zh.md)

<div align="center"><p>Made with 🧡 by<p><a href="https://www.laplace-ai.com/"><img src="https://i.imgur.com/8ysifyO.png" width="150px"></a></div>

![](https://i.imgur.com/ywvxH5W.gif)

Inspired by: [gpt-crawler](https://github.com/BuilderIO/gpt-crawler) by Builder.io

This repository contains a Python script for web crawling using Playwright. It's designed to automate the process of extracting information from web pages, navigating through links on these pages, and aggregating the data.

## Prerequisites

Before running the script, ensure you have the following installed:
- Python 3.6 or later
- Playwright Python package
- A suitable driver for the browser you intend to use (e.g., Chromium)

## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/A-baoYang/gpt-crawler-py
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. Navigate to the project directory:
   ```bash
   cd crawler/
   ```

## Debugging
If you encounter reminder that you have some playwright dependencies to install, you run the bash below:
```bash
sudo apt-get install libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libxkbcommon0 libatspi2.0-0 libxcomposite1 libxrandr2 libgbm1 libasound2
```

## Usage
To run the web crawler, use the following command:
```bash
python main.py
```
This script will start crawling from the URL specified in the configuration, extract data based on the defined selector, and follow links that match the specified pattern. The results will be saved in a JSON file.

![](https://i.imgur.com/4tLHFAo.png)

## Configuration
You can adjust the crawling settings in the Config class within the script. Here, you can set the initial URL, link matching pattern, CSS selector for content extraction, maximum number of pages to crawl, and the output file name.

Open [main.py](crawler/main.py) and edit the `url` and `selectors` in the `config` object.

E.g. to crawl the LaplaceAI products introduction to make a custom GPT you can use:

```python
config = Config(
   url="https://www.laplace-ai.com/vision",
   match="https://www.laplace-ai.com/intro/vision/**",
   selector="#SITE_PAGES",
   max_pages_to_crawl=10,
   output_file_name="output.json"
)
```
