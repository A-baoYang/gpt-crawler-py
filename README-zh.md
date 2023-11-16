# Python GPT Crawler
[English](README-zh.md) | 繁體中文

<div align="center"><p>Made with 🧡 by<p><a href="https://www.laplace-ai.com/"><img src="https://i.imgur.com/8ysifyO.png" width="150px"></a></div>

![](https://i.imgur.com/ywvxH5W.gif)

靈感來源: [gpt-crawler](https://github.com/BuilderIO/gpt-crawler)

自動化從網頁提取資訊、遍歷這些頁面上的連結並聚合數據的過程。

## Prerequisites

在運行腳本之前，請確保您已安裝以下項目：
- Python 3.6 或更高版本
- Playwright Python 套件
- 適用於您將要使用的瀏覽器的適當驅動程序（例如 Chromium）

## Installation

要在您的本機機器上設置該項目，請按照以下步驟操作：

1. 下載到本地:
   ```bash
   git clone https://github.com/A-baoYang/gpt-crawler-py
   ```
2. 安裝相關套件:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. 進到資料夾:
   ```bash
   cd crawler/
   ```

## 安裝除錯
如果你遇到 playwright 運行錯誤，你會需要安裝以下相依:
```bash
sudo apt-get install libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libxkbcommon0 libatspi2.0-0 libxcomposite1 libxrandr2 libgbm1 libasound2
```

## 使用方式
要運行網頁爬蟲，請使用以下命令：
```bash
python main.py
```
該腳本將從配置中指定的 URL 開始爬取，根據定義的選擇器提取數據，並遵循匹配特定模式的連結。結果將保存在一個 JSON 文件中。

![](https://i.imgur.com/4tLHFAo.png)

## 配置
您可以在腳本中的 Config 類中調整爬取設置。在這裡，您可以設定初始 URL、連結匹配模式、內容提取 CSS 選擇器、要爬取的最大頁面數以及輸出文件名。

打開 [main.py](crawler/main.py) 並編輯 `config` 物件中的 `url` 和 `selectors`。

例如，要爬取 LaplaceAI 產品介紹以製作自定義的 GPT，您可以使用：


```python
config = Config(
   url="https://www.laplace-ai.com/vision",
   match="https://www.laplace-ai.com/intro/vision/**",
   selector="#SITE_PAGES",
   max_pages_to_crawl=10,
   output_file_name="output.json"
)
```
