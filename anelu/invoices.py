import os
import asyncio


async def get_invoices(page):
    # Navigate to the page with the list of amounts
    await page.goto(os.getenv("ANELU_INVOICES"))
    # TODO: complete the logic when there's an invoice
    return "hello"


async def pay_invoices(page):
    # TODO: wait until there's a new invoice and complete the logic here
    # I think I did a bad job on getting the checkbox attributes and I'm missing something I have to revisit this when there's a new invoice
    await page.goto(os.getenv("ANELU_REGISTER"))
    return "hello"
