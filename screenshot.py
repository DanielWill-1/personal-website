from pathlib import Path
from playwright.sync_api import sync_playwright

HTML_FILE = "index.html"
OUTPUT_FILE = "fullpage.png"

html_path = Path(HTML_FILE).resolve()

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(
        viewport={
            "width": 1920,
            "height": 1080
        }
    )

    # Open local HTML file
    page.goto(html_path.as_uri(), wait_until="networkidle")

    # Full-page screenshot
    page.screenshot(
        path=OUTPUT_FILE,
        full_page=True
    )

    browser.close()

print(f"Screenshot saved to: {OUTPUT_FILE}")