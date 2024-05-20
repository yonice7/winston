import os
import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from text_unidecode import unidecode
import ast

load_dotenv()


async def login_merc():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Keep browser open

        page = await browser.new_page()

        await page.goto("https://www30.mercantilbanco.com/melp/login")

        username_field = page.locator("#username")
        password_field = page.locator("#password")

        await username_field.fill(os.getenv("MER_USERNAME"))
        await password_field.fill(os.getenv("MER_PASSWORD"))
        await page.locator("text=Iniciar").click()

        # works when going to page from one to the other, if not the browser closes
        await asyncio.sleep(2)
        if page.url == "https://www30.mercantilbanco.com/melp/secure-access":
            questions = await find_questions(page)
            await answer_questions(page, await find_answers(questions))
            await page.locator("label >> text=Equipo de uso personal").click()
            await page.locator("button >> text=Continuar").click()

        await asyncio.sleep(2)
        if page.url == "https://www30.mercantilbanco.com/melp/summary":
            print("Login successful")
        else:
            print("Login failed")
        print(page.url)


async def sec_questions():
    # the .env returns a string
    # ast.literal_eval is a safe way to evaluate simple string expressions in Python. It can handle basic dictionaries with tuple keys as long as the tuples are valid
    return ast.literal_eval(os.getenv("SEC_Q_A"))


async def find_questions(page):
    questions = []

    for i in range(1, 3):
        # locator doesn't have to be awaited so I removed it
        label = page.locator(f"#question-{i}")
        # cannot add the lower method here, returns error bc of the object
        # tried using the text_content method and it didn't work, use inner_text() instead
        question_text = await label.inner_text()
        # remove the diacritics from the question text and make it lowercase
        question = unidecode(question_text.lower())
        questions.append(question)
    return questions


async def find_answers(questions):
    answers = []
    for question in questions:
        # Await sec_questions() to get the actual dictionary
        sec_q_a = await sec_questions()
        for keywords, answer in sec_q_a.items():
            # Check if all words in the keywords are present in the question
            if all(word in question for word in keywords):
                answers.append(answer)
    return answers


async def answer_questions(page, answers):
    question_field1 = page.locator("#mat-input-3")
    question_field2 = page.locator("#mat-input-4")

    await question_field1.fill(answers[0])
    try:  # there could be a misspelled or missing question and answer in the dictionary, so returning an error if that's the case
        await question_field2.fill(answers[1])
    except IndexError:
        print(f"Error: Not enough answers provided. Expected answer for question 2.")
