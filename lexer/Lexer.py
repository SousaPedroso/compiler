from .Token import *
from .InvalidTokenError import InvalidTokenError

digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

class Lexer:
    # Stores the states considering the presented automata
    # 'r' is for return and 's' is for shift to another state
    # All identifications of final states of the automata can be replaced
    # by a return here, since we are not moving forward after this state
    automata = {0: {'+': ['r', SUM], '-': ['r', SUB], ',': ['r', COMMA], ';': ['r', SEMICOLON], '.': ['r', LAST_POINT],
                '(': ['r', LP], ')': ['r', RP], 'p': ['s', 2], 'b': ['s', 14], 'r': ['s', 22], 'i': ['s', 28], 'w': ['s', 40],
                '0': ['s', 48], '1': ['s', 48],'2': ['s', 48], '3': ['s', 48], '4': ['s', 48], '5': ['s', 48], '6': ['s', 48],
                '7': ['s', 48], '8': ['s', 48], '9': ['s', 48], "/": ['s', 54], ":": ['s', 58],
                '{': ['s', 60], '*': ['s', 62], '}': ['s', 64]},
                2: {'r': ['s', 4]}, 4: {'o': ['s', 6]}, 6: {'g': ['s', 8]}, 8: {'r': ['s', 10]}, 10: {'a': ['s', 12]}, 12: {'m': ['r', PROGRAM]}, # program
                14: {'e': ['s', 16]}, 16: {'g': ['s', 18]}, 18: {'i': ['s', 20]}, 20: {'n': ['r', BEGIN]}, # begin
                22: {'e': ['s', 24]}, 24: {'a': ['s', 26]}, 26: {'l': ['r', REAL_TYPE], 'd': ['r', READ]}, # Read or real
                28: {'n': ['s', 30]}, 30: {'t': ['s', 32]}, 32: {'e': ['s', 34]}, 34: {'g': ['s', 36]}, 36: {'e': ['s', 38]}, 38: {'r': ['r', INTEGER_TYPE]}, # integer
                40: {'r': ['s', 42]}, 42: {'i': ['s', 44]}, 44: {'t': ['s', 46]}, 46: {'e': ['r', WRITE]}, # write
                48: {'.': ['s', 50]}, # float number
                50: {'0': ['s', 52], '1': ['s', 52],'2': ['s', 52], '3': ['s', 52], '4': ['s', 52], '5': ['s', 52], '6': ['s', 52], '7': ['s', 52], '8': ['s', 52], '9': ['s', 52]},
                54: {'*': ['s', 56]},
                58: {'=': ['r', ASSIGN]},
                }
    
    line = 1
    stop_pos = 0
    ignore = True # Lines of commentary

    def __init__(self, source_code):
        with open(source_code, "r") as file:
            self.source_code = file.read()
            self.tam = len(self.source_code)
            self.source_code += "$"
            self.state = 0

    def get_token(self):
        state = 0
        cur_pos = 0
        for cur_pos in range(self.stop_pos, self.tam):
            
            # If last token was commentary begining, we can ignore until
            if self.source_code[cur_pos] == ' ' or self.source_code[cur_pos] == '\t':
                continue

            elif self.source_code[cur_pos] == '\n':
                self.line += 1

            else:
                break

        next_action = self.automata[state].get(self.source_code[cur_pos])
        if next_action == None:
            raise InvalidTokenError(f"Invalid token {self.state[cur_pos]} at line {self.line}")

        elif next_action[0] == 's':
            state = next_action[1]
            self.stop_pos = cur_pos + 1

            # Get next action to check possible commentary with /*
            if cur_pos+1 != self.tam: # last token
                next_action = self.automata[state].get(self.source_code[cur_pos+1])

            elif cur_pos+1 == self.tam:
                raise InvalidTokenError(f"Invalid token {self.state[cur_pos]} at line {self.line}")
            
            elif next_action[0] == 'r':
                return next_action[1]()

            # Check next state whether is a *
            next_state = next_action[1]

            # Begining of comentary
            if state == 60 or next_state == 56:
                if next_state == 56:
                    self.stop_pos += 1
                    state = 56


                # Ignore other tokens
                for cur_pos in range(self.stop_pos, self.tam):
                    if (state == 56 and self.automata[cur_pos] != '*') or (self.state == 60 and self.automata[cur_pos] != '}'):
                        continue

                    # First condition of commentary
                    elif self.state == 60 and self.automata[cur_pos] != '}':
                        break

                    # Second condition of commentary
                    elif (state == 56 and self.automata[cur_pos] == '*'):
                        if cur_pos+1 != self.tam and self.automata[cur_pos+1] == '/':
                            break

                self.stop_pos = cur_pos + 1

            elif self.stop_pos != self.tam:
                # Continue reading until a token
                pass

            else:
                return EOS()

        elif self.stop_pos != self.tam:
            self.stop_pos = cur_pos +1
            return next_action[1]()

        elif self.stop_pos == self.tam:
            return EOS()
            
