from .Token import *

digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

class Lexer:
    # Stores the states considering the presented automata
    # 'r' is for return and 's' is for shift to another state
    # All identifications of final states of the automata can be replaced
    # by a return here, since we are not moving forward after this state
    automata = {0: {'{': ['r', OPEN_COMMENT], '}': ['r', CLOSE_COMMENT], '+': ['r', SUM], '-': ['r', SUB], ',': ['r', COMMA],
                ';': ['r', SEMICOLON], '.': ['r', LAST_POINT], '(': ['r', LP], ')': ['r', RP], 'p': ['s', 2], 'b': ['s', 14],
                'r': ['s', 22], 'i': ['s', 28], 'w': ['s', 40], '0': ['s', 48], '1': ['s', 48],'2': ['s', 48], '3': ['s', 48],
                '4': ['s', 48], '5': ['s', 48], '6': ['s', 48], '7': ['s', 48], '8': ['s', 48], '9': ['s', 48], ":": ['s', 54],
                '*': ['s', 58]},
                2: {'r': ['s', 4]}, 4: {'o': ['s', 6]}, 6: {'g': ['s', 8]}, 8: {'r': ['s', 10]}, 10: {'a': ['s', 12]}, 12: {'m': ['r', PROGRAM]}, # program
                14: {'e': ['s', 16]}, 16: {'g': ['s', 18]}, 18: {'i': ['s', 20]}, 20: {'n': ['r', BEGIN]}, # begin
                22: {'e': ['s', 24]}, 24: {'a': ['s', 26]}, 26: {'l': ['r', REAL_TYPE], 'd': ['r', READ]}, # Read or real
                28: {'n': ['s', 30]}, 30: {'t': ['s', 32]}, 32: {'e': ['s', 34]}, 34: {'g': ['s', 36]}, 36: {'e': ['s', 38]}, 38: {'r': ['r', INTEGER_TYPE]}, # integer
                40: {'r': ['s', 42]}, 42: {'i': ['s', 44]}, 44: {'t': ['s', 46]}, 46: {'e': ['r', WRITE]}, # write
                48: {'.': ['s', 50]}, # float number
                50: {'0': ['s', 52], '1': ['s', 52],'2': ['s', 52], '3': ['s', 52], '4': ['s', 52], '5': ['s', 52], '6': ['s', 52], '7': ['s', 52], '8': ['s', 52], '9': ['s', 52]},
                54: {'*': ['r', SLASH_OPEN_COMMENT]},
                56: {'=': ['r', ASSIGN]},
                58: {'/': ['r', SLASH_CLOSE_COMMENT]}
                }
    line = 1
    stop_pos = 0
    ignore = True # Lines of commentary

    def __init__(self, source_code):
        with open(source_code, "r") as file:
            self.source_code = file.read()
            self.state = 0
            self.tam = len(self.source_code)

    def get_token(self):
        state = 0
        cur_pos = 0
        for cur_pos in range(self.stop_pos, self.tam):
            
            # If last token was commentary begining, we can ignore until
            if self.source_code[cur_pos] == ' ' or self.source_code[cur_pos] == '\t':
                continue

            elif self.source_code[cur_pos] == '\n':
                self.line += 1

            # Check presence of commentaries
            else:
                break

        next_action = self.automata[state][self.source_code[cur_pos]]

        if next_action[0] == 's':
            state = next_action[1]
            # Since we are representing as key-value the automata,
            # some atention is needed in some states

        else:
            # check commentaries
            if next_action[1] == OPEN_COMMENT:
                self.ignore = True

            elif next_action[1] == CLOSE_COMMENT:
                self.ignore = False

            elif not(self.ignore):
                return next_action[1]

            # Check possibility for other comen
            elif self.stop_pos == self.tam:
                return EOS()
            
# Arrumar o desenho automato do léxico para ler digitos enquanto houver