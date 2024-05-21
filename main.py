import re
import asyncio
import os
# from .merc import login
from anelu.login import login_anelu
# TODO: Add the get_context function from the context module


def main():
    print('Super Mario')


if __name__ == "__main__":
    asyncio.run(login_anelu())
    # TODO: If function returns successful run the invoices
