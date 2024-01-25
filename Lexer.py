from sly import Lexer

class Lexer(Lexer):
    tokens = { 
        NAME, LPAREN, RPAREN, 
        DIGIT, STRING, 
        OUT, RET,
        DEF, WHILE, IF,
        EQPLUS, EQMINUS, EQMUL, EQDIV,
        PLUS, MINUS, MUL, DIV, POW,
        ISEQ, EQ, 
        AND, OR, NOT,
        LTE, LT, GTE, GT, NE,
        DOT,
        TRUE, FALSE
    } 
    
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NAME['while'] = WHILE
    NAME['if'] = IF
    
    NAME['def'] = DEF
    NAME['ret'] = RET
    NAME['out'] = OUT
    
    NAME['T'] = TRUE
    NAME['F'] = FALSE
    
    LPAREN = r'\('
    RPAREN = r'\)'
    
    DIGIT = r'(-)?\d+\.?\d*'
    STRING = r'(\".*?\"|\'.*?\')'
    
    EQPLUS = r'\+='
    EQMINUS = r'\-='
    EQMUL = r'\*='
    EQDIV = r'/='
    
    LTE = r'<='
    GTE = r'>='
    
    LT = r'<'
    GT = r'>'
    
    ISEQ = r'=='
    NE = r'!='
    
    EQ = r'='
    
    PLUS = r'\+'
    MINUS = r'-'
    MUL = r'\*'
    DIV = r'/'
    POW = r'\^'
    
    AND = r'&'
    OR = r'\|'
    NOT = r'!'
    
    ignore = ' \t'
    ignore_comment = r'%.*'
    
    DOT = r'\.'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
