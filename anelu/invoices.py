import os
import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

# get amount to pay


async def get_amounts(context, page):
    # Get the page object from the context
    page = context.new_page()

    # Navigate to the page with the list of amounts
    await page.goto("https://your-website.com/amounts")
