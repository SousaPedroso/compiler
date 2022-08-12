from .SyntaxError import SyntaxError
from semantic.Semantic import Semantic
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
    {"T": {"begin": ["r", "dc", 0], "real": ["s", 8], "integer": ["s", 9]}, "N": {"corpo": 4, "dc": 5, "dc_v": 6, "tipo_var": 7}}, # I3
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
    {"T": {":=": ["s", 27]}}, # I18
    {"T": {"begin": ["r", "mais_dc", 2]}}, # I19
    {"T": {"begin": ["r", "dc_v", 3], ";": ["r", "dc_v", 3]}}, # I20
    {"T": {"begin": ["r", "mais_var", 0], ";": ["r", "mais_var", 0], ",": ["s", 29]}, "N": {"mais_var": 28}}, # I21
    {"T": {".": ["r", "corpo", 4]}}, # I22
    {"T": {"end": ["r", "comandos", 2]}}, # I23
    {"T": {"ident": ["s", 18], "read": ["s", 16], "write": ["s", 17]}, "N": {"comandos": 30, "comando": 15}}, # I24
    {"T": {"ident": ["s", 31]}}, # I25
    {"T": {"ident": ["s", 32]}}, # I26
    {"T": {"ident": ["r", "op_un", 0], "(": ["r", "op_un", 0], "-": ["s", 36], "numero_int": ["r", "op_un", 0], "numero_real": ["r", "op_un", 0]}, "N": {"expressao": 33, "termo": 34, "op_un": 35}}, # I27
    {"T": {"begin": ["r", "variaveis", 2], ";": ["r", "variaveis", 2]}}, # I28
    {"T": {"ident": ["s", 21]}, "N": {"variaveis": 37}}, # I29
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
    # IT: Initialize
    # T: Type for a variable
    # DT: Delete type for a variable
    # U: Unary operator (-1)
    # AS: Assignment for a identifier
    # R: Input
    # W: print
    # EX: expression (POP VALUES FROM TWO STACKS AND COMPUTES THE VALUE)
    # SO: SumOperation (the operation to be applied)
    # SUO: SUbtrationOperation
    # NI: NumeroInteiro
    # NR: NumeroReal
    # TE: Termo
    # MO: MultiplicationOperation
    # DO: DivisionOperation
    # EA: ExpressionAttribution
    # MF: MaisFatores
    # ID: IDent
    # PU: ProductUnit
    # SU: SumUnit

    identities = {"sum": 0, "sub": 0, "mul": 1, "div": 1}

    # Defines how each non terminal will be updated according to the operation
    operations = {"T": lambda T, V: T.append(V), "DT": lambda T: T.pop(), "AS": lambda N: N.pop(),
    "U": lambda V: -1*V, "R": input, "W": lambda V: print(V), "EX": lambda OP1, OP2: (OP1.pop(), OP2.pop()),
    "SO": "sum", "SUO": "sub", "NI": lambda N: N, "NR": lambda N: N, "TE": lambda FA, MF: (FA.pop(), MF.pop()),
    "MO": "mul", "DO": "div", "EA": lambda E: E.pop(), "MF": lambda FA, MF: (FA.pop(), MF.pop()),
    "OT": lambda FA, MF: (FA.pop(), MF.pop()), "ID": lambda I: I, "PU": "",
    "SU": lambda OT: OT.append(0)}

    a = []
    # Stores the rules to each state to recover the value for each operation
    rules = {
        8: {":": "T"},
        9: {":": "T"},
        20: {"begin": "DT", ";": "DT"},
        33: {"end": "AS", ";": "AS"},
        34: {"end": "SU", ";": "SU", ")": "SU"},
        36: {"ident": "U", "(": "U", "numero_int": "U", "numero_real": "U"},
        38: {"end": "R", ";": "R"},
        39: {"end": "W", ";": "W"},
        40: {"end": "EX", ";": "EX", ")": "EX"},
        42: {"ident": "SO", "end": "SO", ";": "SO", "(": "SO", "+": "SO", "-": "SO", "numero_int": "SO", "numero_real": "SO"},
        43: {"ident": "SUO", "end": "SUO", ";": "SUO", "(": "SUO", "+": "SUO", "-": "SUO", "numero_int": "SUO", "numero_real": "SUO"},
        44: {"end": "NI", ";": "NI", "*": "NI", "/": "NI", "+": "NI", "-": "NI"},
        45: {"end": "NR", ";": "NR", "*": "NR", "/": "NR", "+": "NR", "-": "NR"},
        47: {"end": "SU", ";": "SU", ")": "SU"},
        48: {"end": "TE", ";": "TE", ")": "TE", "+": "TE", "-": "TE"},
        50: {"ident": "MO", "(": "MO", "numero_int": "MO", "numero_real": "MO"},
        51: {"ident": "DO", "(": "DO", "numero_int": "DO", "numero_real": "DO"},
        53: {"end": "PU", ";": "PU", "+": "PU", "-": "PU"},
        54: {"end": "EA", ";": "EA", "*": "EA", "/": "EA", "+": "EA", "-": "EA"},
        55: {"end": "MF", ";": "MF", "+": "MF", "-": "MF"},
        56: {"end": "OT", ";": "OT", ")": "OT"},
        58: {"end": "PU", ";": "PU", "+": "PU", "-": "PU"},
        59: {"end": "ID", ";": "ID", "*": "ID", "/": "ID", "+": "ID", "-": "ID"}
    }

    def __init__(self, inputs, alert=False):
        self.alert = alert
        self.inputs = inputs
        # Stores the symbols and update the values for each operation
        # Remembering that "programa" contains the final result
        self.non_terminals = {"comandos": [], "mais_comandos": [], "comando": [], "expressao": [], "termo": [], "fator": [], "mais_fatores": [], "outros_termos": [],
        "op_ad": [], "op_mul": []}
        self.terminals = {"numero_real": 0, "numero_int": 0}
        self.states = [0]
        self.symbols = []
        self.action = "T" # Search on Terminals or NonTerminals
        self.accepted = False
        self.object = {"I": [], "D": []} # Store operations for object code
        self.identifiers = {}
        self.current_type = [] # Store the types for a variable
        self.unary = 1
        self.arithmetic = []

    def evaluate_input(self):
        # Abbreviation
        inputs = self.inputs
        tokens = []
        step = 0
        last_identifier = ""

        while not(self.accepted):
            
            # If Terminal, update the value
            value = inputs[0].value
            step += 1
            # print(f"Step {step}")
            # print(f"States {self.states}")
            # print(f"Variables: {self.identifiers}")
            # print(f"Input: {inputs}")
            # print(f"Symbols: {self.symbols}")
            # print(f"Non terminals: {self.non_terminals}")
            # print(f"Operations: {self.arithmetic}")
            if self.terminals.get(value) != None:
                self.terminals[value] = inputs[0].input

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
                        self.symbols.append(inputs[0].value)
                        tokens.append(inputs[0])
                        last_input = self.inputs[0]
                        del(self.inputs[0])

                    # reduce
                    elif action[0] != 'acc':

                        if self.alert:
                            print("Reduced ", end="")

                        # Get semantic rule for the state
                        rule = self.rules.get(self.states[-1])
                        if rule != None:
                            rule_type = rule.get(value)
                            if rule_type == "T":
                                # Set the current type for the variables
                                self.operations.get("T")(self.current_type, tokens[-1].value)
                                
                            # Clear the type (expecting other type or begin of the program)
                            elif rule_type == "DT":
                                self.operations.get("DT")(self.current_type)
                            
                            elif rule_type == "AS":
                                self.identifiers[tokens[-3].ident] = self.operations.get("AS")(self.non_terminals["expressao"])
                                last_identifier = tokens[-3].ident

                            elif rule_type == "SU":
                                self.operations.get("SU")(self.non_terminals["outros_termos"])

                            elif rule_type == "U":
                                self.identifiers[last_identifier] = self.operations.get("U")(self.identifiers[last_identifier])
                            
                            elif rule_type == "R":
                                self.identifiers[tokens[-2].ident] = float(self.operations.get("R")())
                                
                            elif rule_type == "W":
                                self.operations.get("W")(self.identifiers[tokens[-2].ident])

                            elif rule_type == "EX":
                                op1, op2 = self.operations.get("EX")(self.non_terminals["termo"], self.non_terminals["outros_termos"])
                                operation = self.arithmetic[-1]
                                # print(f"\n\n\nOP1: {op1}, OP2: {op2}, OPERATION: {operation}\n\n\n")
                                if operation == "sum":
                                    self.non_terminals["expressao"].append(op1+op2)
                                    
                                elif operation == "sub":
                                    self.non_terminals["expressao"].append(op1-op2)
                                    
                                elif operation == "mul":
                                    self.non_terminals["expressao"].append(op1*op2)

                                else:
                                    self.non_terminals["expressao"].append(op1/op2)

                            elif rule_type == "NR":
                                self.non_terminals["fator"].append(tokens[-1].input)

                            elif rule_type == "NI":
                                self.non_terminals["fator"].append(tokens[-1].input)

                            elif rule_type == "TE":
                                
                                op1, op2 = self.operations.get("TE")(self.non_terminals["fator"], self.non_terminals["mais_fatores"])
                                operation = self.arithmetic[-1]
                                # print(f"\n\n\nOP1: {op1}, OP2: {op2}\n\n\n")
                                if operation == "sum":
                                    self.non_terminals["termo"].append(op1+op2)
                                    
                                elif operation == "sub":
                                    self.non_terminals["termo"].append(op1-op2)
                                    
                                elif operation == "mul":
                                    self.non_terminals["termo"].append(op1*op2)

                                else:
                                    self.non_terminals["termo"].append(op1/op2)

                            elif rule_type == "EA":
                                self.non_terminals["fator"].append(self.operations.get("EA")(self.non_terminals["expressao"]))
                                
                            elif rule_type == "PU":
                                self.non_terminals["mais_fatores"].append(self.identities[self.arithmetic[-1]])

                            elif rule_type == "MF":
                                op1, op2 = self.operations.get("MF")(self.non_terminals["fator"], self.non_terminals["mais_fatores"])
                                operation = self.arithmetic[-1]
                                if operation == "sum":
                                    self.non_terminals["mais_fatores"].append(op1+op2)
                                    
                                elif operation == "sub":
                                    self.non_terminals["mais_fatores"].append(op1-op2)
                                    
                                elif operation == "mul":
                                    self.non_terminals["mais_fatores"].append(op1*op2)

                                else:
                                    self.non_terminals["mais_fatores"].append(op1/op2)

                            elif rule_type == "OT":
                                op1, op2 = self.operations.get("OT")(self.non_terminals["termo"], self.non_terminals["outros_termos"])
                                operation = self.arithmetic[-1]
                                if operation == "sum":
                                    self.non_terminals["outros_termos"].append(op1+op2)
                                    
                                elif operation == "sub":
                                    self.non_terminals["outros_termos"].append(op1-op2)
                                    
                                elif operation == "mul":
                                    self.non_terminals["outros_termos"].append(op1*op2)

                                else:
                                    self.non_terminals["outros_termos"].append(op1/op2)

                            elif rule_type == "ID":
                                # print(tokens[-1].ident)
                                self.non_terminals["fator"].append(self.identifiers[tokens[-1].ident])

                        # print(self.non_terminals, tokens[-1])
                        # Store the symbol position to print it
                        symbol = len(self.symbols)-action[2]

                        # Check state for arithmetic operation
                        if self.states[-1] == 42 or self.states[-1] == 43 or self.states[-1] == 50 or self.states[-1] == 51:
                            self.arithmetic.append(self.operations[rule_type])

                        # Remove symbols
                        for _ in range(action[2]):
                            if self.alert:
                                print(self.symbols[symbol], end="")
                            del(self.symbols[symbol])
                            del(tokens[symbol])
                            del(self.states[-1])

                        # Update the last 
                        # Add the correspondent symbol
                        self.symbols.append(action[1])
                        tokens.append(action[1])
                        # Check for next Nonterminal
                        self.action = 'N'
                        if self.alert:
                            print(f" to {action[1]}")

                    # accepted sentence
                    else:
                        # First value of the stack (and probably the only one)
                        self.accepted = True
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