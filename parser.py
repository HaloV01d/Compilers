from ply import yacc
from Compilers.lexer import lexer


tokens = lexer.tokens

# Define the grammar rules
def p_programa(p):
    'programa : inicio secuenciaInst final'
    p[0] = ('programa', p[2])

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right'),
)

def p_asignacion(p):
    'asignacion : Identificador Operador_Asig expresion Punto_Coma'
    p[0] = ('asignacion', p[1], p[3])

def p_instruccion_asignacion(p):
    'instruccion : asignacion'
    p[0] = p[1]

def p_secuenciaInst_multiple(p):
    'secuenciaInst : instruccion secuenciaInst'
    p[0] = ('secuenciaInst', p[1], p[2])

def p_secuenciaInst_single(p):
    'secuenciaInst : instruccion'
    p[0] = ('secuenciaInst', p[1])