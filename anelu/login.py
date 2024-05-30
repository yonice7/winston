import os
import asyncio


async def login_anelu(context, page):

    # going to the website and input the credentials
    await page.goto(os.getenv("ANELU_CODE"))
    await page.click("a.header-top-info__link")
    username_field = page.locator("input[name='usuario']")
    password_field = page.locator("input[name='password']")
    await username_field.fill(os.getenv("ANELU_CODE"))
    await password_field.fill(os.getenv("ANELU_PASSWORD"))
    await page.click("text=Ingresar")

    # checking if login is successful
    await asyncio.sleep(4)
    if page.url == os.getenv("ANELU_LOGGED"):
        return True
    else:
        return False
