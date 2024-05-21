import os
import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from context import get_context

load_dotenv()


async def login_anelu(context, page):
    await page.goto("https://www.administradoranelu.com/")
    await page.click("a.header-top-info__link")
    username_field = page.locator("input[name='usuario']")
    password_field = page.locator("input[name='password']")

    await username_field.fill(os.getenv("ANELU_CODE"))
    await password_field.fill(os.getenv("ANELU_PASSWORD"))
    await page.click("text=Ingresar")

    await asyncio.sleep(4)
    if page.url == "https://www.administradoranelu.com/enlinea/":
        return "successful"
    else:
        return "failed"
