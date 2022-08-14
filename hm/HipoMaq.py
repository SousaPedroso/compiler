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
    help="Destination file when compiling the source_code",
)

args = parser.parse_args()

class HipoMaq:
    
    def __init__(self, source_code):
        self.source_code = source_code
        self.data = []
        self.instructions = None
        self.ins_top = None
        self.data_top = None
        self.rel_address =  None
        self.inv_rel_addresses = None
        self.int_variables = None

    def interpret(self):
        self.data_top = -1
        self.ins_top = 0
        self.set_instructions = {}

        with open(args.dest_code, "r") as object_code:
            self.instructions = object_code.readlines()

        while self.instructions[self.ins_top] != "PARA":
            # Remove '\n'
            instruction = self.instructions[self.ins_top]
            self.instructions[self.ins_top] = instruction[:len(instruction)-1]

            # INPP is ignored
            if self.instructions[self.ins_top] == "IMPR":
                print(self.data[self.data_top])
                self.data.pop()
                self.data_top -= 1

            elif self.instructions[self.ins_top] == "LEIT":
                inp = float(input())
                self.data_top += 1
                self.data.append(inp)

            elif self.instructions[self.ins_top] == "ALME 1":
                self.data_top += 1
                self.data.append(0)

            elif self.instructions[self.ins_top][:4] == "ARMZ":
                address =  ""
                for d in self.instructions[self.ins_top][5:]:
                    address = f"{address}{d}"

                address = int(address)
                # If variable integer, force cast
                inv_ad = self.inv_rel_addresses.get(address)
                int_var = self.int_variables.get(inv_ad)
                if int_var == None:
                    self.data[address] = self.data[self.data_top]
                else:
                    self.data[address] = int(self.data[self.data_top])
                self.data.pop()
                self.data_top -= 1

            elif self.instructions[self.ins_top] == "INVE":
                self.data[self.data_top] *= -1

            elif self.instructions[self.ins_top] == "SOMA":
                # If variable integer, force cast
                self.data[self.data_top-1] = self.data[self.data_top-1] + self.data[self.data_top]
                self.data_top -= 1
                self.data.pop()

            elif self.instructions[self.ins_top] == "SUB":
                self.data[self.data_top-1] = self.data[self.data_top-1] - self.data[self.data_top]
                self.data_top -= 1
                self.data.pop()

            elif self.instructions[self.ins_top] == "MULT":
                self.data[self.data_top-1] = self.data[self.data_top-1] * self.data[self.data_top]
                self.data_top -= 1
                self.data.pop()

            elif self.instructions[self.ins_top] == "DIVI":
                self.data[self.data_top-1] = self.data[self.data_top-1] / self.data[self.data_top]
                self.data_top -= 1
                self.data.pop()

            elif self.instructions[self.ins_top][:4] == "CRCT":
                # If find  a '.', it is a float
                buffer = ""
                buffer_type = "i"
                for char in self.instructions[self.ins_top][5:]:
                    buffer = f"{buffer}{char}"
                    if char == '.':
                        buffer_type = "f"

                if buffer_type == "i":
                    self.data.append(int(buffer))

                else:
                    self.data.append(float(buffer))

                self.data_top += 1

            elif self.instructions[self.ins_top][:4] == "CRVL":
                address =  ""
                for d in self.instructions[self.ins_top][5:]:
                    address = f"{address}{d}"

                address = int(address)
                self.data.append(self.data[address])
                self.data_top += 1

            # Next instruction
            self.ins_top += 1

    def compile(self):
        lexer = Lexer(self.source_code)
        token = lexer.get_token()
        instructions = [token]

        while token.tag != Tag.EOS:
            token = lexer.get_token()
            instructions.append(token)

        syntatic = Syntatic(instructions)
        syntatic.evaluate_input()

        self.int_variables = syntatic.int_variables
        self.rel_address = syntatic.rel_addresses
        self.inv_rel_addresses = syntatic.inv_rel_addresses

        with open(args.dest_code, "w") as object_code:
            object_code.writelines(syntatic.intermediary_code)
        

hm = HipoMaq(args.source_code)
hm.compile()
hm.interpret()
