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
    OPEN_COMMENT=17
    CLOSE_COMMENT=18
    SLASH_OPEN_COMMENT=19
    SLASH_CLOSE_COMMENT=20   
    LP=21
    RP=22
    END=23

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
        self.value = 'ident'
        self.input = inp # name of the variable

class INTEGER_NUMBER(Token):
    def __init__(self, inp):
        super().__init__(Tag.INTEGER_NUMBER)
        self.value = 'ident'
        self.input = inp

class ASSIGN(Token):
    def __init__(self):
        super().__init__(Tag.ASSIGN)
        self.value = ':='

class LAST_POINT(Token):
    def __init__(self):
        super().__init__(Tag.LAST_POINT)
        self.value = '.'

class OPEN_COMMENT(Token):
    def __init__(self):
        super().__init__(Tag.OPEN_COMMENT)
        self.value = '{'

class CLOSE_COMMENT(Token):
    def __init__(self):
        super().__init__(Tag.CLOSE_COMMENT)
        self.value = '}'

class SLASH_OPEN_COMMENT(Token):
    def __init__(self):
        super().__init__(Tag.SLASH_OPEN_COMMENT)
        self.value = '/*'

class SLASH_CLOSE_COMMENT(Token):
    def __init__(self):
        super().__init__(Tag.SLASH_CLOSE_COMMENT)
        self.value = '*/'

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