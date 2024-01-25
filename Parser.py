from sly import Parser
from Lexer import Lexer

class Parser(Parser):
    tokens = Lexer.tokens
    
    precedence = (
       ('right', LPAREN, NAME, RPAREN),
    )
    
    @_('expr')
    def exprs(self, p):
        return [p.expr]
    
    @_('expr exprs')
    def exprs(self, p):
        return [p.expr] + p.exprs
        
    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr
        
    @_('LPAREN IF expr LPAREN exprs RPAREN RPAREN')
    def expr(self, p):
        return ('IF', p.expr, p.exprs)

    @_('LPAREN EQ NAME expr RPAREN')
    def expr(self, p):
        return ('EQ', p.NAME, p.expr)
    
    @_('LPAREN NOT expr RPAREN')
    def expr(self, p):
        return ('NOT', p.expr)
    
    @_('LPAREN LTE expr expr RPAREN')
    def expr(self, p):
        return ('LTE', p.expr0, p.expr1)
    
    @_('LPAREN LT expr expr RPAREN')
    def expr(self, p):
        return ('LT', p.expr0, p.expr1)
    
    @_('LPAREN GTE expr expr RPAREN')
    def expr(self, p):
        return ('GTE', p.expr0, p.expr1)
    
    @_('LPAREN GT expr expr RPAREN')
    def expr(self, p):
        return ('GT', p.expr0, p.expr1)
    
    @_('LPAREN ISEQ expr expr RPAREN')
    def expr(self, p):
        return ('ISEQ', p.expr0, p.expr1)
    
    @_('LPAREN NE expr expr RPAREN')
    def expr(self, p):
        return ('NE', p.expr0, p.expr1)
    
    @_('LPAREN PLUS expr expr RPAREN')
    def expr(self, p):
        return ('PLUS', p.expr0, p.expr1)
    
    @_('LPAREN MINUS expr expr RPAREN')
    def expr(self, p):
        return ('MINUS', p.expr0, p.expr1)
    
    @_('LPAREN MUL expr expr RPAREN')
    def expr(self, p):
        return ('MUL', p.expr0, p.expr1)
    
    @_('LPAREN DIV expr expr RPAREN')
    def expr(self, p):
        return ('DIV', p.expr0, p.expr1)
    
    @_('LPAREN POW expr expr RPAREN')
    def expr(self, p):
        return ('POW', p.expr0, p.expr1)
    
    @_('LPAREN AND expr expr RPAREN')
    def expr(self, p):
        return ('AND', p.expr0, p.expr1)
    
    @_('LPAREN OR expr expr RPAREN')
    def expr(self, p):
        return ('OR', p.expr0, p.expr1)
    
    @_('LPAREN NOT expr expr RPAREN')
    def expr(self, p):
        return ('NOT', p.expr0, p.expr1)
    
    @_('LPAREN EQPLUS NAME expr RPAREN')
    def expr(self, p):
        return ('EQPLUS', p.NAME, p.expr)
    
    @_('LPAREN EQMINUS NAME expr RPAREN')
    def expr(self, p):
        return ('EQMINUS', p.NAME, p.expr)
    
    @_('LPAREN EQMUL NAME expr RPAREN')
    def expr(self, p):
        return ('EQMUL', p.NAME, p.expr)
    
    @_('LPAREN EQDIV NAME expr RPAREN')
    def expr(self, p):
        return ('EQDIV', p.NAME, p.expr)
    
    @_('LPAREN OUT exprs RPAREN')
    def expr(self, p):
        return ('OUT', p.exprs)
    
    @_('LPAREN RET exprs RPAREN')
    def expr(self, p):
        return ('RET', p.exprs)
             
    @_('LPAREN DEF NAME LPAREN exprs RPAREN LPAREN exprs RPAREN RPAREN')
    def expr (self, p):
        return ('DEF', p.NAME, p.exprs0, p.exprs1)
    
    @_('LPAREN DEF NAME LPAREN RPAREN LPAREN exprs RPAREN RPAREN')
    def expr (self, p):
        return ('DEF', p.NAME, [], p.exprs)

    @_('LPAREN WHILE expr LPAREN exprs RPAREN RPAREN')
    def expr(self, p):
        return ('WHILE', p.expr, p.exprs)
        
    @_('LPAREN NAME exprs RPAREN')
    def expr(self, p):
        return ("FUNC", p.NAME, p.exprs)
    
    @_('LPAREN NAME RPAREN')
    def expr(self, p):
        return ("FUNC", p.NAME, [])
    
    @_('NAME')
    def expr(self, p):
        return ('NAME', p.NAME)
        
    @_('TRUE')
    def expr(self, p):
        return ('TRUE',)
    
    @_('FALSE')
    def expr(self, p):
        return ('FALSE',)
    
    @_('DIGIT')
    def expr(self, p):
        if p.DIGIT.count("."):
            return ('DIGIT', float(p.DIGIT))
        
        return ('DIGIT', int(p.DIGIT))
    
    @_('DOT')
    def expr(self, p):
        return ("DOT", '\n')
    
    @_('STRING')
    def expr(self, p):
        string = p.STRING[1:-1]
        string = string.replace('\\t', '    ')
        string = string.replace('\\n', '\n')
        return ('STRING', string)
