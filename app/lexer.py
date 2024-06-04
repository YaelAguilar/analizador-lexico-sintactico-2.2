import ply.lex as lex

# List of token names
tokens = [
    'FOR', 'INT', 'PRINT', 'NUM', 'ID', 'OP', 'PAREN', 'BRACE', 'STRING', 'SEMICOLON', 'PLUS', 'INCREMENT'
]

# Reserved words
reserved = {
    'for': 'FOR',
    'int': 'INT',
    'println': 'PRINT'
}

# Regular expression rules for simple tokens
t_OP = r'<=|='
t_PAREN = r'[()]'
t_BRACE = r'[{}]'
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_INCREMENT = r'\+\+'
t_NUM = r'\d+'
t_STRING = r'"[^"]*"'
t_ignore = ' \t\n'

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Error handling rule
def t_error(t):
    print(f"Token ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def tokenize(code):
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value))
    return tokens
