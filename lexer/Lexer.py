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
                '{': ['s', 60], '*': ['s', 62], '}': ['s', 64], 'e': ['s', 70]},
                2: {'r': ['s', 4]}, 4: {'o': ['s', 6]}, 6: {'g': ['s', 8]}, 8: {'r': ['s', 10]}, 10: {'a': ['s', 12]}, 12: {'m': ['r', PROGRAM]}, # program
                14: {'e': ['s', 16]}, 16: {'g': ['s', 18]}, 18: {'i': ['s', 20]}, 20: {'n': ['r', BEGIN]}, # begin
                22: {'e': ['s', 24]}, 24: {'a': ['s', 26]}, 26: {'l': ['r', REAL_TYPE], 'd': ['r', READ]}, # Read or real
                28: {'n': ['s', 30]}, 30: {'t': ['s', 32]}, 32: {'e': ['s', 34]}, 34: {'g': ['s', 36]}, 36: {'e': ['s', 38]}, 38: {'r': ['r', INTEGER_TYPE]}, # integer
                40: {'r': ['s', 42]}, 42: {'i': ['s', 44]}, 44: {'t': ['s', 46]}, 46: {'e': ['r', WRITE]}, # write
                48: {'.': ['s', 50], '0': ['s', 48], '1': ['s', 48],'2': ['s', 48], '3': ['s', 48], '4': ['s', 48], '5': ['s', 48], '6': ['s', 48],
                '7': ['s', 48], '8': ['s', 48], '9': ['s', 48]}, # float number and integer number
                50: {'0': ['s', 52], '1': ['s', 52],'2': ['s', 52], '3': ['s', 52], '4': ['s', 52], '5': ['s', 52], '6': ['s', 52], '7': ['s', 52], '8': ['s', 52], '9': ['s', 52]},
                52: {'0': ['s', 52], '1': ['s', 52],'2': ['s', 52], '3': ['s', 52], '4': ['s', 52], '5': ['s', 52], '6': ['s', 52], '7': ['s', 52], '8': ['s', 52], '9': ['s', 52]},
                54: {'*': ['s', 56]},
                58: {'=': ['r', ASSIGN]}, # :=
                70: {'n': ['s', 72]},
                72: {'d': ['r', END]}
                }
    # Continuar olhando o desenho para todos os estados estarem certo
    # depois fazer condições para quando for necessário ou não ler
    
    line = 1
    stop_pos = 0
    ignore = True # Lines of commentary

    def __init__(self, source_code):
        with open(source_code, "r") as file:
            self.source_code = file.read()
            self.tam = len(self.source_code)
            self.source_code += "$"
            self.state = 0

    # Function to lead with commentaries
    # Function to lead with spaces and tabulations

    # Ignore commentaries and return the position on the file
    def ignore_spaces(self):
        cur_pos = 0
        for cur_pos in range(self.stop_pos, self.tam):
            
            # If last token was commentary begining, we can ignore until
            if self.source_code[cur_pos] == ' ' or self.source_code[cur_pos] == '\t':
                continue

            elif self.source_code[cur_pos] == '\n':
                self.line += 1

            else:
                break

        return cur_pos

    def get_token(self):
        state = 0
        cur_pos = 0
        self.stop_pos = self.ignore_spaces()

        action = self.automata[state].get(self.source_code[self.stop_pos])
        char_code = ord(self.source_code[self.stop_pos])

        # Not in the automata and not letter
        if self.stop_pos+1 != self.tam and action == None and ((char_code > 122 or char_code < 97) and (char_code > 90 or char_code < 65)):
            raise InvalidTokenError(f"Invalid token {self.source_code[self.stop_pos]} at line {self.line}")

        elif action != None and action[0] == 's':
            state = action[1]

            # Get next action to check possible commentary with /*
            if self.stop_pos +1 != self.tam: # last token
                next_action = self.automata.get(state)
                if next_action != None:
                    next_action = next_action.get(self.source_code[self.stop_pos +1])

            elif self.stop_pos+1 == self.tam:
                raise InvalidTokenError(f"Invalid token {self.source_code[self.stop_pos]} at line {self.line}")
            
            if next_action != None and next_action[0] == 'r':
                self.stop_pos += 2
                return next_action[1]()

            # Check next state whether is a *
            if next_action != None:
                next_state = next_action[1]
            else:
                next_state = -1

            # Begining of comentary
            if state == 60 or next_state == 56:
                if next_state == 56:
                    self.stop_pos += 1
                    state = 56

                # Ignore other tokens
                for cur_pos in range(self.stop_pos, self.tam):
                    if (state == 56 and self.source_code[cur_pos] != '*') or (state == 60 and self.source_code[cur_pos] != '}'):
                        continue

                    # First condition of commentary
                    elif state == 60 and self.source_code[cur_pos] == '}':
                        self.stop_pos = cur_pos+1
                        break

                    # Second condition of commentary
                    elif (state == 56 and self.source_code[cur_pos] == '*'):
                        if cur_pos+1 != self.tam and self.source_code[cur_pos+1] == '/':
                            self.stop_pos = cur_pos+2
                            break


            if self.stop_pos != self.tam:
                self.stop_pos = self.ignore_spaces()
                action = self.automata[0].get(self.source_code[self.stop_pos])
                char_code = ord(self.source_code[self.stop_pos])

                # Not in the automata and not letter
                if action == None and ((char_code > 122 or char_code < 97) and (char_code > 90 or char_code < 65)):
                    raise InvalidTokenError(f"Invalid token {self.source_code[cur_pos]} at line {self.line}")

                # Search on the table first before check string
                # r, p, digit and : allows more than one valid token, treatment for each one
                elif action != None:
                    # 'program', 'begin', 'end', 'integer' must be read until the next character
                    if action[1] == 2 or action[1] == 14 or action[1] == 22 or action[1] == 28 or action[1] == 40 or action[1] == 70:
                        buffer = ""
                        while self.stop_pos != self.tam and action != None and action[0] != 'r':
                            buffer = f"{buffer}{self.source_code[self.stop_pos]}"
                            self.stop_pos += 1
                            action = self.automata[action[1]].get(self.source_code[self.stop_pos])

                        self.stop_pos += 1
                        if action == None:
                            # Variable
                            self.stop_pos -= 1
                            return IDENT(buffer)

                        else:
                            return action[1]()

                    # Treatment for colon
                    elif action[1] == 58:
                        self.stop_pos += 1
                        return COLON()

                    # Treatment for *
                    elif action[1] == 62:
                        self.stop_pos += 1
                        return MUL()

                    # Treatment for numbers
                    elif action[1] == 48:
                        buffer = ""
                        last_state = 48
                        while self.stop_pos != self.tam and action != None and action[0] != 'r':
                            buffer = self.automata[cur_pos]
                            last_state = action[1]
                            self.stop_pos += 1
                            action = self.automata[action[1]].get(self.source_code[self.stop_pos])

                        # if None (integer)
                        if last_state == 48:
                            return INTEGER_NUMBER(buffer)

                        elif last_state == 52:
                            return REAL_NUMBER(buffer)

                        # Last state == 50, missed precision of the number
                        else:
                            raise InvalidTokenError(f"It was expected a precision after {buffer}")

                # Treatment for ident
                elif (char_code <= 122 and char_code >= 97) or (char_code <= 90 and char_code >= 65):
                    buffer = ""
                    while (char_code <= 122 and char_code >= 97) or (char_code <= 90 and char_code >= 65) or\
                        (char_code >= 48 and char_code <= 57) or char_code == 95:
                        buffer = f"{buffer}{self.source_code[self.stop_pos]}"
                        self.stop_pos += 1
                        char_code = ord(self.source_code[self.stop_pos])

                    return IDENT(buffer)

                else:
                    raise InvalidTokenError(f"Invalid token {self.source_code[cur_pos]} at line {self.line}")

            else:
                return EOS()

        # Check for return the token 
        elif self.stop_pos+1 != self.tam and action != None:
            self.stop_pos += 1
            return action[1]()

        # letter, _ or digit for ident
        elif self.stop_pos+1 != self.tam:
            # MUST start with letter, this is the goal of the if statement
            if (char_code <= 122 and char_code >= 97) or (char_code <= 90 and char_code >= 65):
                buffer = ""
                while (char_code <= 122 and char_code >= 97) or (char_code <= 90 and char_code >= 65) or\
                    (char_code >= 48 and char_code <= 57) or char_code == 95:
                    buffer = f"{buffer}{self.source_code[self.stop_pos]}"
                    self.stop_pos += 1
                    char_code = ord(self.source_code[self.stop_pos])

                return IDENT(buffer)

        else:
            return EOS()

# Checar o que estou passando batido para parênteses