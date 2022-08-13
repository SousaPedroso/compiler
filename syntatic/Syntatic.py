from .SyntaxError import SyntaxError
from semantic.Semantic import Semantic
from semantic.DeclarationError import DeclarationError
from lexer.Token import *

class Syntatic(Semantic):
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

    def __init__(self, inputs):
        super().__init__()
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
        self.identifiers = {} # Stores the positions for each variable
        self.current_type = "" # Stores the types for a variable
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
            # print(self.current_type)
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

                        # Allocate memory
                        if self.states[-1] == 13 or self.states[-1] == 29:
                            # Set the current type for the variables
                            if self.current_type == "real":
                                # Previously declared as integer
                                if self.int_variables.get(inputs[0].ident) != None:
                                    raise DeclarationError(f"{inputs[0].ident} was declared as integer")

                                self.operations.get("T")(self.real_variables, inputs[0].ident)

                            # int
                            else:
                                # Previously declared as real
                                if self.real_variables.get(inputs[0].ident) != None:
                                    raise DeclarationError(f"{inputs[0].ident} was declared as real")

                                self.operations.get("T")(self.int_variables, inputs[0].ident)

                            self.intermediary_code.append("ALME 1")

                        self.states.append(action[1])
                        self.symbols.append(inputs[0].value)
                        tokens.append(inputs[0])
                        last_input = self.inputs[0]
                        del(self.inputs[0])

                    # reduce
                    elif action[0] != 'acc':

                        # Get semantic rule for the state
                        rule = self.rules.get(self.states[-1])
                        if rule != None:
                            rule_type = rule.get(value)
                            if rule_type == "T":
                                self.current_type = self.symbols[-1]
                                
                            # Clear the type (expecting other type or begin of the program)
                            if rule_type == "DT":
                                self.current_type = self.operations.get("DT")
                            
                            elif rule_type == "AS":
                                self.identifiers[tokens[-3].ident] = self.operations.get("AS")(self.non_terminals["expressao"])
                                last_identifier = tokens[-3].ident
                                self.intermediary_code.append(f"ARMZ {tokens[-3].ident}")

                            elif rule_type == "SU":
                                self.operations.get("SU")(self.non_terminals["outros_termos"])

                            elif rule_type == "U":
                                self.identifiers[last_identifier] = self.operations.get("U")(self.identifiers[last_identifier])
                                self.intermediary_code.append("INVE")
                            
                            elif rule_type == "R":
                                self.identifiers[tokens[-2].ident] = float(self.operations.get("R")())
                                self.intermediary_code.append("LEIT")
                                
                            elif rule_type == "W":
                                self.operations.get("W")(self.identifiers[tokens[-2].ident])
                                self.intermediary_code.append("IMPR")

                            elif rule_type == "EX":
                                op1, op2 = self.operations.get("EX")(self.non_terminals["termo"], self.non_terminals["outros_termos"])
                                operation = self.arithmetic[-1]
                                # print(f"\n\n\nOP1: {op1}, OP2: {op2}, OPERATION: {operation}\n\n\n")
                                if operation == "sum":
                                    self.non_terminals["expressao"].append(op1+op2)
                                    self.intermediary_code.append("SOMA")
                                    
                                elif operation == "sub":
                                    self.non_terminals["expressao"].append(op1-op2)
                                    self.intermediary_code.append("SUBT")
                                    
                                elif operation == "mul":
                                    self.non_terminals["expressao"].append(op1*op2)
                                    self.intermediary_code.append("MULT")

                                else:
                                    self.non_terminals["expressao"].append(op1/op2)
                                    self.intermediary_code.append("DIVI")

                            elif rule_type == "NR":
                                self.non_terminals["fator"].append(tokens[-1].input)
                                self.intermediary_code.append(f"CRCT {tokens[-1].input}")

                            elif rule_type == "NI":
                                self.non_terminals["fator"].append(tokens[-1].input)
                                self.intermediary_code.append(f"CRCT {tokens[-1].input}")

                            elif rule_type == "TE":
                                op1, op2 = self.operations.get("TE")(self.non_terminals["fator"], self.non_terminals["mais_fatores"])
                                operation = self.arithmetic[-1]
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
                                self.non_terminals["fator"].append(self.identifiers[tokens[-1].ident])
                                self.intermediary_code.append(f"CRVL {tokens[-1].ident}")

                        # print(self.non_terminals, tokens[-1])

                        # Check state for arithmetic operation
                        if self.states[-1] == 42 or self.states[-1] == 43 or self.states[-1] == 50 or self.states[-1] == 51:
                            self.arithmetic.append(self.operations[rule_type])

                        # Remove symbols
                        for _ in range(action[2]):
                            del(self.symbols[-1])
                            del(tokens[-1])
                            del(self.states[-1])

                        # Update the last 
                        # Add the correspondent symbol
                        self.symbols.append(action[1])
                        tokens.append(action[1])
                        # Check for next Nonterminal
                        self.action = 'N'

                    # accepted sentence
                    else:
                        self.intermediary_code.append("PARA")
                        self.accepted = True
                        return True

                # Syntax error
                else:
                    raise SyntaxError(f"Unexpected {value} after {last_input.value}")
                
            # Update state
            else:
                action = self.table[self.states[-1]]
                self.states.append(action.get("N").get(self.symbols[-1]))
                self.action = 'T'