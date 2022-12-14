class Token:
    def __init__(self, t):
        self.tag = t

class Tag:
    SUM=1
    SUB=2
    MUL=3
    DIV=4
    COMMA=5
    SEMICOLON=6
    PROGRAM=7
    BEGIN=8
    REAL_TYPE=9
    INTEGER_TYPE=10
    READ=11
    WRITE=12
    REAL_NUMBER=13
    INTEGER_NUMBER=14
    ASSIGN=15
    LAST_POINT=16 
    LP=17
    RP=18
    END=19
    EOS=20
    IDENT=21
    COLON=22

class SUM(Token):
    def __init__(self):
        super().__init__(Tag.SUM)
        self.value = '+'

class SUB(Token):
    def __init__(self):
        super().__init__(Tag.SUB)
        self.value = '-'

class MUL(Token):
    def __init__(self):
        super().__init__(Tag.MUL)
        self.value = '*'

class DIV(Token):
    def __init__(self):
        super().__init__(Tag.DIV)
        self.value = '/'

class COMMA(Token):
    def __init__(self):
        super().__init__(Tag.COMMA)
        self.value = ','

class SEMICOLON(Token):
    def __init__(self):
        super().__init__(Tag.SEMICOLON)
        self.value = ';'

class PROGRAM(Token):
    def __init__(self):
        super().__init__(Tag.PROGRAM)
        self.value = 'program'

class BEGIN(Token):
    def __init__(self):
        super().__init__(Tag.BEGIN)
        self.value = 'begin'

class REAL_TYPE(Token):
    def __init__(self):
        super().__init__(Tag.REAL_TYPE)
        self.value = 'real'

class INTEGER_TYPE(Token):
    def __init__(self):
        super().__init__(Tag.INTEGER_TYPE)
        self.value = 'integer'

class READ(Token):
    def __init__(self):
        super().__init__(Tag.READ)
        self.value = 'read'

class WRITE(Token):
    def __init__(self):
        super().__init__(Tag.WRITE)
        self.value = 'write'

class REAL_NUMBER(Token):
    def __init__(self, inp):
        super().__init__(Tag.REAL_NUMBER)
        self.value = 'numero_real'
        self.input = inp # name of the variable

class INTEGER_NUMBER(Token):
    def __init__(self, inp):
        super().__init__(Tag.INTEGER_NUMBER)
        self.value = 'numero_int'
        self.input = inp

class ASSIGN(Token):
    def __init__(self):
        super().__init__(Tag.ASSIGN)
        self.value = ':='

class LAST_POINT(Token):
    def __init__(self):
        super().__init__(Tag.LAST_POINT)
        self.value = '.'

class LP(Token):
    def __init__(self):
        super().__init__(Tag.LP)
        self.value = '('

class RP(Token):
    def __init__(self):
        super().__init__(Tag.RP)
        self.value = ')'

class END(Token):
    def __init__(self):
        super().__init__(Tag.END)
        self.value = 'end'

class EOS(Token):
    def __init__(self):
        super().__init__(Tag.EOS)
        self.value = '$'

class IDENT(Token):
    def __init__(self, identity):
        super().__init__(Tag.IDENT)
        self.value = 'ident'
        self.ident = identity

class COLON(Token):
    def __init__(self):
        super().__init__(Tag.COLON)
        self.value = ':'