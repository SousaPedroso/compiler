class Semantic:

    identities = {"sum": 0, "sub": 0, "mul": 1, "div": 1}


    # Types for each rule
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


    # Defines how each non terminal will be updated according to the operation
    operations = {"T": lambda T, V: T.update({V: ''}), "DT": lambda T: T.pop(), "AS": lambda N: N.pop(),
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

    def __init__(self):
        self.real_variables = {}
        self.int_variables = {}
        self.intermediary_code = ["INPP"]
    