class Semantic:

    identities = {"sum": 0, "sub": 0, "mul": 1, "div": 1}


    # Types for each rule
    # T: Type for a variable
    # U: Unary operator (-1)
    # AS: Assignment for a identifier
    # R: Input
    # W: print
    # EX: expression (Generate the operation to be computed)
    # SO: SumOperation
    # SUO: SUbtrationOperation
    # NI: NumeroInteiro
    # NR: NumeroReal
    # MO: MultiplicationOperation
    # DO: DivisionOperation
    # EA: ExpressionAttribution
    # ID: IDent
    # PPO: PushProductOperation
    # PAO: PushAddOperation

    # Defines how each non terminal will be updated according to the operation
    operations = {"T": lambda T, V: T.update({V: ''}), "MO": "MULT", "DO": "DIVI", "SO": "SOMA", "SUO": "SUBT"}

    # Stores the rules to generate the pseudocode
    rules = {
        8: {":": "T"},
        9: {":": "T"},
        33: {"end": "AS", ";": "AS"},
        36: {"ident": "U", "(": "U", "numero_int": "U", "numero_real": "U"},
        38: {"end": "R", ";": "R"},
        39: {"end": "W", ";": "W"},
        42: {"ident": "SO", "end": "SO", ";": "SO", "(": "SO", "+": "SO", "-": "SO", "numero_int": "SO", "numero_real": "SO"},
        43: {"ident": "SUO", "end": "SUO", ";": "SUO", "(": "SUO", "+": "SUO", "-": "SUO", "numero_int": "SUO", "numero_real": "SUO"},
        44: {"end": "NI", ";": "NI", "*": "NI", "/": "NI", "+": "NI", "-": "NI"},
        45: {"end": "NR", ";": "NR", "*": "NR", "/": "NR", "+": "NR", "-": "NR"},
        50: {"ident": "MO", "(": "MO", "numero_int": "MO", "numero_real": "MO"},
        51: {"ident": "DO", "(": "DO", "numero_int": "DO", "numero_real": "DO"},
        55: {"end": "PPO", ";": "PPO", "+": "PPO", "-": "PPO"},
        56: {"end": "PAO", ";": "PAO", ")": "PAO"},
        59: {"end": "ID", ";": "ID", "*": "ID", "/": "ID", "+": "ID", "-": "ID"}
    }

    def __init__(self):
        self.real_variables = {}
        self.int_variables = {}
        self.intermediary_code = ["INPP\n"]
    