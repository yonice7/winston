import os
import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv

# Loading the .env file
load_dotenv()


async def get_amounts(page):
    # Navigate to the page with the list of amounts
    await page.goto(os.getenv("ANELU_INVOICES"))
