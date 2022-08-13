from hm.ModeError import ModeError
from lexer.Lexer import Lexer
from lexer.Token import Tag
from syntatic.Syntatic import Syntatic
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    "source_code",
    help="Source code to compile or interpret"
)

parser.add_argument(
    "dest_code",
    help="Destinatio file when compiling the source_code",
)

args = parser.parse_args()

class HipoMaq:
    
    def __init__(self, source_code):
        self.source_code = source_code
        self.data = None
        self.instructions = None
        self.ins_top = None
        self.data_top = None

    def interpret(self):
        self.data_top = -1
        self.ins_top = 0
        self.set_instructions = {}
        self.data = []

        with open(self.source_code, "r") as object_code:
            self.instructions = object_code.readlines()

        while self.instructions[self.ins_top] != "PARA":
            
            if self.instructions[self.ins_top] == "INPP":
                self.ins_top += 1
                continue
        
            elif self.instructions[self.ins_top] == "IMPR":
                print(self.data[self.data_top])
                self.data.pop()
                self.data_top =- 1

            elif self.instructions[self.ins_top] == "LEIT":
                
                self.data_top += 1

            # Pop the instruction after being read
            self.instructions.pop(0)



    def compile(self):
        lexer = Lexer(self.source_code)
        token = lexer.get_token()
        instructions = [token]

        while token.tag != Tag.EOS:
            token = lexer.get_token()
            instructions.append(token)

        syntatic = Syntatic(instructions)
        syntatic.evaluate_input()

        with open(args.dest_code, "w") as object_code:
            object_code.writelines(syntatic.intermediary_code)
        

hm = HipoMaq(args.source_code)
hm.compile()
hm.interpret()
