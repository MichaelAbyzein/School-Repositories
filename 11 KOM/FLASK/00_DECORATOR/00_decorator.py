
from typing import Text


def outer_function(text):
    msg = text

    def inner_fuction():
        print(msg)

    return inner_fuction()

outer_function("Hello!")