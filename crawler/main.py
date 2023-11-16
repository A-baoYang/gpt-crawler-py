import asyncio
from playwright.async_api import async_playwright
import json
import fnmatch
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
                with open(config.output_file_name, 'w') as f:
                    json.dump(results, f, indent=2)

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
    results = await crawl(config)
    with open(config.output_file_name, 'w') as f:
        json.dump(results, f, indent=2)


# Running the main function
if __name__ == "__main__":
    config = Config(
        url="https://www.laplace-ai.com/vision",
        match="https://www.laplace-ai.com/intro/vision/**",
        selector="#SITE_PAGES",
        max_pages_to_crawl=10,
        output_file_name="output.json"
    )
    asyncio.run(main(config))
