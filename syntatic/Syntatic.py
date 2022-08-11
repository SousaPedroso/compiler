from .SyntaxError import SyntaxError
from lexer.Token import *

class Syntatic:
    accepted = False
    # T for terminal symbos and N for nonterminal symbols
    # s for shift and r for reduce. Reduce has one more element on the list
    # representing the token to substitue the current symbols. The last value 
    # is the number of symbols to remove before append the symbol
    # In shift and Nonterminals the number is for update the state

    table = [{"T": {"program": ["s", 2]}, "N": {"programa": 1}}, # I0
    {"T": {"$": ["acc"]}}, # I1
    {"T": {"ident": ["s", 3]}}, # I2
    {"T": {"begin": ["r", "dc", 0], "real": ["s", 8], "integer": ["s", 9], "$": ["r", "T", 1]}, "N": {"corpo": 4, "dc": 5, "dc_v": 6, "tipo_var": 7}}, # I3
    {"T": {".": ["s", 57]}}, # I4
    {"T": {"begin": ["s", 10]}}, # I5
    {"T": {"begin": ["r", "mais_dc", 0], ";": ["s", 12]}, "N": {"mais_dc": 11}}, # I6
    {"T": {":": ["s", 13]}}, # I7
    {"T": {":": ["r", "tipo_var", 1]}}, # I8
    {"T": {":": ["r", "tipo_var", 1]}}, # I9
    {"T": {"ident": ["s", 18], "read": ["s", 16], "write": ["s", 17]}, "N": {"comandos": 14, "comando": 15}}, # I10
    {"T": {"begin": ["r", "dc", 2]}}, # I11
    {"T": {"begin": ["r", "dc", 0], "real": ["s", 8], "integer": ["s", 9]}, "N": {"dc": 19, "dc_v": 6, "tipo_var": 7}}, # I12
    {"T": {"ident": ["s", 21]}, "N": {"variaveis": 20}}, # I13
    {"T": {"end": ["s", 22]}}, # I14
    {"T": {"end": ["r", "mais_comandos", 0], ";": ["s", 24]}, "N": {"mais_comandos": 23}}, # I15
    {"T": {"(": ["s", 25]}}, # I16
    {"T": {"(": ["s", 26]}}, # I17
    {"T": {":=", ["s", 27]}}, # I18
    {"T": {"begin": ["r", "mais_dc", 2]}}, # I19
    {"T": {"begin": ["r", "dc_v", 3], ";": ["r", "dc_v", 3]}}, # I20
    {"T": {"begin": ["r", "mais_var", 12], ";": ["r", "mais_var", 12], ",": ["s", 29]}, "N": {"mais_var": 28}}, # I21
    {"T": {".": ["r", "corpo", 4]}}, # I22
    {"T": {"end": ["r", "comandos", 2]}}, # I23
    {"T": {"ident": ["s", 18], "read": ["s", 16], "write": ["s", 17]}, "N": {"comandos": 30, "comando": 15}}, # I24
    {"T": {"ident": ["s", 31]}}, # I25
    {"T": {"ident": ["s", 32]}}, # I26
    {"T": {"ident": ["r", "op_un", 0], "(": ["r", "op_un", 0], "-": ["s", 36], "numero_int": ["r", "op_un", 0], "numero_real": ["r", "op_un", 0]}, "N": {"expressao": 33, "termo": 34, "op_un": 35}}, # I27
    {"T": {"begin": ["r", "variaveis", 2], ";": ["r", "variaveis", 2]}}, # I28
    {"T": {"ident": ["s", "21"]}, "N": {"variaveis": 37}}, # I29
    {"T": {"end": ["r", "mais_comandos", 2]}}, # I30
    {"T": {")": ["s", 38]}}, # I31
    {"T": {")": ["s", 39]}}, # I32
    {"T": {"end": ["r", "comando", 3], ";": ["r", "comando", 3]}}, # I33
    {"T": {"end": ["r", "outros_termos", 0], ";": ["r", "outros_termos", 0], ")": ["r", "outros_termos", 0], "+": ["s", 42], "-": ["s", 43]}, "N": {"outros_termos": 40, "op_ad": 41}}, # I34
    {"T": {"ident": ["s", 59], "(": ["s", 46], "numero_int": ["s", 44], "numero_real": ["s", 45]}, "N": {"fator": 58}}, # I35
    {"T": {"ident": ["r", "op_un", 1], "(": ["r", "op_un", 1], "numero_int": ["r", "op_un", 1], "numero_real": ["r", "op_un", 1]}}, # I36
    {"T": {"begin": ["r", "mais_var", 2], ";": ["r", "mais_var", 2]}}, # I37
    {"T": {"end": ["r", "comando", 4], ";": ["r", "comando", 4]}}, # I38
    {"T": {"end": ["r", "comando", 4], ";": ["r", "comando", 4]}}, # I39
    {"T": {"end": ["r", "expressao", 2], ";": ["r", "expressao", 2], ")": ["r", "expressao", 2]}}, # I40
    {"T": {"ident": ["r", "op_un", 0], "(": ["r", "op_un", 0], "-": ["s", 36], "numero_int": ["r", "op_un", 0], "numero_real": ["r", "op_un", 0]}, "N": {"termo": 47, "op_un": 35}}, # I41
    {"T": {"ident": ["r", "op_ad", 1], "end": ["r", "op_ad", 1], ";": ["r", "op_ad", 1], "(": ["r", "op_ad", 1], "+": ["r", "op_ad", 1], "-": ["r", "op_ad", 1], "numero_int": ["r", "op_ad", 1], "numero_real": ["r", "op_ad", 1]}}, # I42
    {"T": {"ident": ["r", "op_ad", 1], "end": ["r", "op_ad", 1], ";": ["r", "op_ad", 1], "(": ["r", "op_ad", 1], "+": ["r", "op_ad", 1], "-": ["r", "op_ad", 1], "numero_int": ["r", "op_ad", 1], "numero_real": ["r", "op_ad", 1]}}, # I43
    {"T": {"end": ["r", "fator", 1], ";": ["r", "fator", 1], "*": ["r", "fator", 1], "/": ["r", "fator", 1], "+": ["r", "fator", 1], "-": ["r", "fator", 1]}}, # I44
    {"T": {"end": ["r", "fator", 1], ";": ["r", "fator", 1], "*": ["r", "fator", 1], "/": ["r", "fator", 1], "+": ["r", "fator", 1], "-": ["r", "fator", 1]}}, # I45
    {"T": {"ident": ["r", "op_un", 0], "(": ["r", "op_un", 0], "-": ["s", 36], "numero_int": ["r", "op_un", 0], "numero_real": ["r", "op_un", 0]}, "N": {"expressao": 52, "termo": 34, "op_un": 35}}, # I46
    {"T": {"end": ["r", "outros_termos", 0], ";": ["r", "outros_termos", 0], ")": ["r", "outros_termos", 0], "+": ["s", 42], "-": ["s", 43]}, "N": {"outros_termos": 56, "op_ad": 41}}, # I47
    {"T": {"end": ["r", "termo", 3], ";": ["r", "termo", 3], ")": ["r", "termo", 3], "+": ["r", "termo", 3], "-": ["r", "termo", 3]}}, # I48
    {"T": {"ident": ["s", 59], "(": ["s", 46], "numero_int": ["s", 44], "numero_real": ["s", 46]}, "N": {"fator": 53}}, # I49
    {"T": {"ident": ["r", "op_mul", 1], "(": ["r", "op_mul", 1], "numero_int": ["r", "op_mul", 1], "numero_real": ["r", "op_mul", 1]}}, # I50
    {"T": {"ident": ["r", "op_mul", 1], "(": ["r", "op_mul", 1], "numero_int": ["r", "op_mul", 1], "numero_real": ["r", "op_mul", 1]}}, # I51
    {"T": {")": ["s", 54]}}, # I52
    {"T": {"end": ["r", "mais_fatores", 0], ";": ["r", "mais_fatores", 0], "*": ["s", 50], "/": ["s", 51], "+": ["r", "mais_fatores", 0], "-": ["r", "mais_fatores", 0]}, "N": {"mais_fatores": 55, "op_mul": 49}}, # I53
    {"T": {"end": ["r", "fator", 3], ";": ["r", "fator", 3], "*": ["r", "fator", 3], "/": ["r", "fator", 3], "+": ["r", "fator", 3], "-": ["r", "fator", 3]}}, # I54
    {"T": {"end": ["r", "mais_fatores", 3], ";": ["r", "mais_fatores", 3], "+": ["r", "mais_fatores", 3], "-": ["r", "mais_fatores", 3]}}, # I55
    {"T": {"end": ["r", "outros_termos", 3], ";": ["r", "outros_termos", 3], ")": ["r", "outros_termos", 3]}}, # I56
    {"T": {"$": ["r", "programa", 4]}}, # I57
    {"T": {"end": ["r", "mais_fatores", 0], ";": ["r", "mais_fatores", 0], "*": ["s", 50], "/": ["s", 51], "+": ["r", "mais_fatores", 0], "-": ["r", "mais_fatores", 0]}, "N": {"mais_fatores": 48, "op_mul": 49}}, # I58
    {"T": {"end": ["r", "fator", 1], ";": ["r", "fator", 1], "*": ["r", "fator", 1], "/": ["r", "fator", 1], "+": ["r", "fator", 1], "-": ["r", "fator", 1]}} # I59
    ]

    # Types for each rule
    # I: Ihnerate (for symbol only, actually it is a synthetized attribute)
    # A: Add
    # S: Sub
    # M: Mult
    # D: Div

    # Defines how each non terminal will be updated according to the operation
    operations = {"I": lambda S: S, "A": lambda E, T:  E+T, "S": lambda E, T:  E-T,
    "M": lambda T, P: T*P, "D": lambda T, P: T/P, "R": lambda E: E.pop()}

    # Stores the rules to each state to recover the value for each operation
    rules = {
        3: {},
        6: {},
        8: {},
        9: {},
        11: {},
        12: {},
        15: {},
        19: {},
        20: {},
        21: {},
        22: {},
        23: {},
        27: {},
        28: {},
        30: {},
        33: {},
        34: {},
        36: {},
        37: {},
        38: {},
        39: {},
        40: {},
        41: {},
        42: {},
        43: {},
        44: {},
        45: {},
        46: {},
        47: {},
        48: {},
        50: {},
        51: {},
        53: {},
        54: {},
        55: {},
        56: {},
        57: {},
        58: {},
        59: {}
    }

    def __init__(self, inputs, alert=False):
        self.alert = alert
        self.current = 0 # Current input
        self.inputs = inputs
        self.reset_state()
        # S indicates for which value the state must be updated
        # R has two values, 1 string for indicate which token will substitute the current(s) and
        # a integer indicating the number of tokens to remove

    def reset_state(self):
        # Stores the symbols and update the values for each operation
        # Remembering that "programa" contains the final result
        self.non_terminals = {"programa": [], "corpo": [], "dc": [], "dc_v": [], "mais_dc": [], "tipo_var": [], "variaveis": [], "mais_var": [],
        "comandos": [], "mais_comandos": [], "comando": [], "expressao": [], "termo": [], "op_un": [], "fator": [], "mais_fatores": [], "outros_termos": [],
        "op_ad": [], "op_mul": []}
        self.terminals = {"numero_real": 0, "numero_int": 0}
        self.states = [0]
        self.symbols = []
        self.action = "T" # Search on Terminals or NonTerminals
        self.accepted = False

    def evaluate_input(self):
        # Abbreviation
        inputs = self.inputs


        while not(self.accepted):
            
            # If Terminal, update the value
            value = inputs[0].value
            if self.terminals.get(value) != None:
                self.terminals[value] = inputs[0].inp

            # Action for terminals
            if self.action == "T":
                # Check if it is ok
                action = self.table[self.states[-1]].get("T").get(value)
                if action != None:
                    # Push state and symbols
                    # Check shift
                    if action[0] != 'acc' and action[0] == 's':
                        if self.alert:
                            print(f"Shift to {action[1]}")

                        self.states.append(action[1])
                        self.symbols.append(value)
                        last_input = self.inputs[0]
                        del(self.inputs[0])

                    # reduce
                    elif action[0] != 'acc':

                        if self.alert:
                            print("Reduced ", end="")

                        # Get the rule for the value
                        rule = self.rules.get(self.states[-1])
                        rule_type = rule.get(value)

                        # Store the symbol position to print it
                        symbol = len(self.symbols)-action[2]

                        # print(rule_type, self.non_terminals)

                        # Remove symbols
                        for _ in range(action[2]):
                            if self.alert:
                                print(self.symbols[symbol], end="")
                            del(self.symbols[symbol])
                            del(self.states[-1])

                        # Update the last 
                        # Add the correspondent symbol
                        self.symbols.append(action[1])
                        # Check for next Nonterminal
                        self.action = 'N'
                        if self.alert:
                            print(f" to {action[1]}")

                    # accepted sentence
                    else:
                        # First value of the stack (and probably the only one)
                        print(f"Value for the input {self.current+1}: {str(self.non_terminals['programa'][0]).replace('.', ',')}")
                        self.accepted = True
                        self.current += 1
                        self.reset_state()
                        return True

                # Syntax error
                else:
                    # Need more values
                    if value != "$":
                        raise SyntaxError(f"Unexpected {value} after {last_input.value}")

                    else:
                        raise SyntaxError(f"It was expected a sentence or value after {last_input.value}")
                
            # Update state
            else:
                action = self.table[self.states[-1]]
                self.states.append(action.get("N").get(self.symbols[-1]))
                self.action = 'T'
                if self.alert:
                    print(f"Deviation for state {self.states[-1]}")