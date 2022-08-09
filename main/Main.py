import os
from lexer.Lexer import Lexer
from lexer.Token import *

def main():
    tests_dir = os.path.abspath("..\\tests")

    lexer = Lexer(os.path.join(tests_dir, "ex01"))
    token = lexer.get_token()
    input = [token]
    while token.tag != Tag.EOS:
        print(token, token.value)
        token = lexer.get_token()
        input.append(token)

if __name__ == "__main__":
    main()