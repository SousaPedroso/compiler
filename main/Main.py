import os
from lexer.Lexer import Lexer
from lexer.Tag import *

def main():
    tests_dir = os.path.abspath("..\\tests")

    lexer = Lexer(os.path.join(tests_dir, "ex01"))
    token = lexer.get_token()
    inputs = [[token]]
    last_line = lexer.line
    # Recover the values
    entradas = [[token.value]]