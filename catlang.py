from pprint import pprint
from sys import argv

from Lexer import Lexer
from Parser import Parser

def exec(c):
    global locals
    
    if c[0] == 'EQ':
        names[c[1]] = exec(c[2])
        
    if c[0] == 'EQPLUS':
        try:
            locals[c[1]] += exec(c[2])
        except (KeyError, TypeError) as e:
            names[c[1]] += exec(c[2])
    
    if c[0] == 'EQMINUS':
        try:
            locals[c[1]] -= exec(c[2])
        except (KeyError, TypeError) as e:      
            names[c[1]] -= exec(c[2])
    
    if c[0] == 'EQMUL':
        try:
            locals[c[1]] *= exec(c[2])
        except (KeyError, TypeError) as e:
            names[c[1]] *= exec(c[2])
    
    if c[0] == 'EQDIV':
        try:
            locals[c[1]] /= exec(c[2])
        except (KeyError, TypeError) as e:
            names[c[1]] /= exec(c[2])
    
    if c[0] == 'NAME':
        try:
            return locals[c[1]]
        except (KeyError, TypeError) as e:
            return names[c[1]]
    
    if c[0] == 'DIGIT':
        return c[1]
    
    if c[0] == 'STRING':
        return c[1]
    
    if c[0] == 'LTE':
        return exec(c[1]) <= exec(c[2])
    
    if c[0] == 'LT':
        return exec(c[1]) < exec(c[2])
    
    if c[0] == 'GTE':
        return exec(c[1]) >= exec(c[2])
    
    if c[0] == 'GT':
        return exec(c[1]) > exec(c[2])
    
    if c[0] == 'NE':
        return exec(c[1]) != exec(c[2])
    
    if c[0] == 'ISEQ':
        return exec(c[1]) == exec(c[2])
    
    if c[0] == 'PLUS':
        return exec(c[1]) + exec(c[2])
    
    if c[0] == 'MINUS':
        return exec(c[1]) - exec(c[2])
    
    if c[0] == 'MUL':
        return exec(c[1]) * exec(c[2])
    
    if c[0] == 'DIV':
        return exec(c[1]) / exec(c[2])
    
    if c[0] == 'POW':
        return exec(c[1]) ** exec(c[2])
    
    if c[0] == 'AND':
        return exec(c[1]) and exec(c[2])
    
    if c[0] == 'OR':
        return exec(c[1]) or exec(c[2])
    
    if c[0] == 'NOT':
        return not exec(c[1])

    if c[0] == 'DOT':
        return '\n'
    
    if c[0] == 'TRUE':
        return True
    
    if c[0] == 'FALSE':
        return False
    
    if c[0] == 'OUT':
        for key in c[1]:
            value = exec(key)
            
            # Convert True and False to T and F
            if isinstance(value, bool):
                value = ['F', 'T'][value]
            
            print(value, end="")
        print()
        
    if c[0] == 'RET':
        return exec(c[1][0])

    if c[0] == 'IF':
        if exec(c[1]):
            for key in c[2]:
                exec(key)
                
    if c[0] == 'WHILE':
        while exec(c[1]):
            for key in c[2]:
                exec(key)
    
    if c[0] == 'DEF':
        funcs[c[1]] = (c[2], c[3])
        
    if c[0] == 'FUNC':
        locals = {}
        for i, key in enumerate(funcs[c[1]][0]):
            locals[key[1]] = exec(c[2][i])
        
        for key in funcs[c[1]][1]:
            if key[0] == 'RET':
                return exec(key)
            
            exec(key)
            
# Get code
if len(argv) > 1:
    file = argv[1]
    text = open(file).read()
else:
    print("usage: python3 catlang.py <file> [-d]")
    exit()

# Lexer
lexer = Lexer()
tokens = lexer.tokenize(text)
if '-d' in argv:  # Debug
    tokens_ = lexer.tokenize(text)
    try:
        print('TOKENS')
        print(*[token for token in tokens_], sep='\n')
    except EOFError:
        pass

# Parser
names = {}
funcs = {}
parser = Parser()
ast = parser.parse(tokens)

if '-d' in argv:  # Debug
    print('AST TREE')
    pprint(ast)

# Exec all code
for leaf in ast:
    exec(leaf)
