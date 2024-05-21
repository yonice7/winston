from playwright.async_api import async_playwright


async def get_context():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = context.new_page()
        return browser, context, page
