from ply import yacc
from Compilers.lexer import lexer


tokens = lexer.tokens # Import tokens from lexer

# Define the grammar rules
def p_programa(p): # Program rule
    'programa : inicio secuenciaInst final'
    p[0] = ('programa', p[2])

precedence = ( # Define operator precedence
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right'),
)

def p_asignacion(p): # Assignment rule
    'asignacion : Identificador Operador_Asig expresion Punto_Coma'
    p[0] = ('asignacion', p[1], p[3])

def p_instruccion_asignacion(p): # Instruction assignment rule
    'instruccion : asignacion'
    p[0] = p[1]

def p_secuenciaInst_multiple(p): # Multiple instruction sequence rule
    'secuenciaInst : instruccion secuenciaInst'
    p[0] = ('secuenciaInst', p[1], p[2])

def p_secuenciaInst_single(p): # Single instruction sequence rule
    'secuenciaInst : instruccion'
    p[0] = ('secuenciaInst', p[1])

def p_identificador(p): # Identifier expression rule
    'expresion : Identificador'
    p[0] = ('identificador', p[1])

def p_secuenciaInst(p): # Sequence of instructions rule
    'secuenciaInst : instruccion secuenciaInst'
    p[0] = ('secuenciaInst', p[1], p[2])

def p_expresion_num(p): # Numeric expression rule
    'expresion : Num'
    p[0] = ('num', p[1])

def p_expresion_binaria(p): # Binary expression rule
    'expresion : expresion Operadores_Binarios expresion'
    p[0] = ('binaria', p[2], p[1], p[3])

def p_error(p): # Error handling rule
    if p:
        print(f"Error de sintaxis en el token '{p.value}' en la línea {p.lineno}")
    else:
        print("Error de sintaxis al final del archivo")

parser = yacc.yacc() # Build the parser