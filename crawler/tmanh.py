import asyncio
from playwright.async_api import async_playwright
import json
import fnmatch
import os
from config import Config


# Function to get page HTML
async def get_page_html(page, selector):
    await page.wait_for_selector(selector)
    element = await page.query_selector(selector)
    return await element.inner_text() if element else ""


# Crawl function
async def crawl(config):
    results = []
    queue = [config.url]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        if config.cookie:
            await page.context.add_cookies([{
                "name": config.cookie['name'], 
                "value": config.cookie['value'], "url": config.url}])

        try:
            while queue and len(results) < config.max_pages_to_crawl:
                url = queue.pop(0)
                print(f"Crawler: Crawling {url}")
                await page.goto(url)
                html = await get_page_html(page, config.selector)
                results.append({'url': url, 'html': html})

                # Extract and enqueue links
                links = await page.query_selector_all("a")
                for link in links:
                    href = await link.get_attribute("href")
                    if href and fnmatch.fnmatch(href, config.match):
                        queue.append(href)

                # Implement on_visit_page logic if needed
        finally:
            await browser.close()

    return results


# Main function
async def main(config):
    if not os.path.exists(config.output_file_name):
        origin = []
    else:
        with open(config.output_file_name, 'r', encoding="utf-8") as f:
            origin = json.load(f)

    results = await crawl(config)
    with open(config.output_file_name, 'w', encoding="utf-8") as f:
        json.dump(origin + results, f, indent=2)


# Running the main function
if __name__ == "__main__":
    # with open("urls.txt", "r") as f:
    #     urls = f.readlines()
    
    # for url in urls:
    url = "https://www.tmanh.org.tw"
    config = Config(
        url=url,
        match="https://www.tmanh.org.tw/**",
        selector="body",
        max_pages_to_crawl=100,
        output_file_name="ana_output.json"
    )
    asyncio.run(main(config))
