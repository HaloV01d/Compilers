from ply import yacc
from lexer import lexer, tokens

# ============================
#       ANALIZADOR Sintáctico
# ============================

# Define the grammar rules
def p_programa(p): # Program rule
    'programa : INICIO secuenciaInst FINAL'
    p[0] = ('programa', p[2])

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/', '%'),
    ('nonassoc', '<', '>', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'IGUAL_IGUAL', 'DIFERENTE')
)


def p_asignacion(p): # Assignment rule
    'asignacion : IDENTIFICADOR OPERADOR_ASIG expresion'
    p[0] = ('asignacion', p[1], p[3])

def p_instruccion_asignacion(p): # Assignment instruction rule
    'instruccion : asignacion'
    p[0] = p[1]

def p_identificador(p): # Identifier expression rule
    'expresion : IDENTIFICADOR'
    p[0] = ('identificador', p[1])

def p_expresion_num(p): # Numeric expression rule
    'expresion : NUM'
    p[0] = ('num', p[1])

def p_expresion_parentesis(p): # Parentheses expression rule
    'expresion : LPAREN expresion RPAREN'
    p[0] = p[2]

def p_expresion_unaria(p): # Unary expression rule
    'expresion : OPERADORES_BINARIOS expresion'
    if p[1] == '-':
        p[0] = ('negacion', p[2])
    else:
        p[0] = ('positivo', p[2])

def p_secuenciaInst(p): # Sequence of instructions rule
    'secuenciaInst : instruccion'
    p[0] = ('secuenciaInst', p[1])

def p_secuenciaInst_multiple(p): # Multiple instructions rule
    'secuenciaInst : instruccion secuenciaInst'
    p[0] = ('secuenciaInst', p[1], p[2])

def p_instruccion_lee(p): # Read instruction rule
    'instruccion : LEE LPAREN IDENTIFICADOR RPAREN PUNTO_COMA'
    p[0] = ('lee', p[3])

def p_instruccion_escribe(p): # Write instruction rule
    'instruccion : ESCRIBE LPAREN expresion RPAREN PUNTO_COMA'
    p[0] = ('escribe', p[3])

def p_instruccion_si(p): # If instruction rule
    'instruccion : SI LPAREN expresion RPAREN secuenciaInst SINO secuenciaInst FINSI'
    p[0] = ('si', p[3], p[5], p[7])

def p_instruccion_si_con_sino(p): # If instruction with else rule
    'instruccion : SI LPAREN expresion RPAREN secuenciaInst FINSI'
    p[0] = ('si', p[3], p[5], None)

def p_operadores_binarios(p):
    '''expresion : expresion '+' expresion
                 | expresion '-' expresion
                 | expresion '*' expresion
                 | expresion '/' expresion
                 | expresion '%' expresion
                 | expresion '<' expresion
                 | expresion '>' expresion
                 | expresion MENOR_IGUAL expresion
                 | expresion MAYOR_IGUAL expresion
                 | expresion IGUAL_IGUAL expresion
                 | expresion DIFERENTE expresion'''
    op = p[2]
    if op == '+':
        p[0] = ('suma', p[1], p[3])
    elif op == '-':
        p[0] = ('resta', p[1], p[3])
    elif op == '*':
        p[0] = ('multiplicacion', p[1], p[3])
    elif op == '/':
        p[0] = ('division', p[1], p[3])
    elif op == '%':
        p[0] = ('modulo', p[1], p[3])
    elif op == '<':
        p[0] = ('menor_que', p[1], p[3])
    elif op == '>':
        p[0] = ('mayor_que', p[1], p[3])
    elif op == '<=':
        p[0] = ('menor_igual', p[1], p[3])
    elif op == '>=':
        p[0] = ('mayor_igual', p[1], p[3])
    elif op == '==':
        p[0] = ('igual_igual', p[1], p[3])
    elif op == '<>':
        p[0] = ('diferente', p[1], p[3])

def p_error(p):
    if p:
        print(f"\033[91mError de sintaxis en el token '{p.value}' en la línea {p.lineno}\033[0m")
        print(f"\033[91mToken completo:", p, "\033[0m")
    else:
        print(f"\033[91mError de sintaxis al final del archivo\033[0m")

parser = yacc.yacc() # Build the parser


# =========================
#     PRUEBA RÁPIDA
# =========================
if __name__ == '__main__': # Test the parser
    ruta = 'C:\\Users\\Alondra Soto\\OneDrive\\Documents\\Development\\Compilers\\Test\\Caso_Correcto1.txt'
    with open(ruta, 'r', encoding='Utf-8', errors='replace') as archivo:
        datos = archivo.read()
    result = parser.parse(datos) # Parse the input data
    print("=== RESULTADO DEL PARSEO ===")
    print(result) # Print the result