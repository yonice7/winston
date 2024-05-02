import os
import ast
from dotenv import load_dotenv


load_dotenv()


def sec_questions():
    return ast.literal_eval(os.getenv("SEC_Q_A"))


print(sec_questions())
