import ply.yacc as yacc
from app.lexer import tokens, lexer

def p_programa(p):
    'programa : bucle'
    p[0] = "Bucle validado"

def p_bucle(p):
    '''bucle : FOR PAREN declaracion SEMICOLON condicion SEMICOLON incremento PAREN BRACE cuerpo BRACE'''
    pass

def p_declaracion(p):
    'declaracion : INT ID OP NUM'
    pass

def p_condicion(p):
    'condicion : ID OP NUM'
    pass

def p_incremento(p):
    '''incremento : ID INCREMENT'''
    pass

def p_cuerpo(p):
    'cuerpo : PRINT PAREN STRING PLUS ID PAREN SEMICOLON'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token {p.type} en la posición {p.lexpos}")
        raise SyntaxError(f"Error de sintaxis en el token {p.type} en la posición {p.lexpos}")
    else:
        print("Error de sintaxis en EOF")
        raise SyntaxError("Error de sintaxis en EOF")

parser = yacc.yacc()

def parse(code):
    return parser.parse(code, lexer=lexer)
