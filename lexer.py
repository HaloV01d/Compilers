from ply import lex

# =========================
#       ANALIZADOR LÉXICO
# =========================

RESERVADAS_MIN = { # Palabras reservadas en minúsculas
    'inicio': 'inicio',
    'final': 'final',
    'sino': 'sino',
    'finsi': 'finsi',
}

tokens = ( # Lista de tokens
    'inicio', 'final', 'sino', 'finsi',
    'Si', 'Lee', 'Escribe',
    'Operador_Asig', 'Operadores_Binarios',
    'Num', 'Identificador',
    'Parentesis', 'Punto_Coma',
)

t_Operador_Asig   = r'=' # Operador de asignación
t_Operadores_Binarios = r'<=|>=|==|<>|\+|-|\*|/|%|<|>' # Operadores binarios
t_Parentesis = r'\(|\)' # Paréntesis
t_Punto_Coma      = r';' # Punto y coma

def t_Num(t): # Número entero
    r'\d+'
    t.value = int(t.value)
    return t

def t_Si(t): # Si
    r'Si'
    return t

def t_Lee(t): # Lee
    r'Lee'
    return t

def t_Escribe(t): # Escribe
    r'Escribe'
    return t

def t_Identificador(t): # Identificador
    r'[a-z][a-z0-9]+'
    if t.value in RESERVADAS_MIN: # Verificar si es palabra reservada
        t.type = RESERVADAS_MIN[t.value]
    return t

t_ignore = ' \t' # Ignorar espacios y tabulaciones

def t_newline(t): # Manejar saltos de línea
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t): # Manejar errores léxicos
    ch = t.value[0] # Carácter ilegal
    if ch.isalpha(): # Si empieza con letra, es un identificador inválido
        posible = ch
        i = 1
        while i < len(t.value) and t.value[i].isalnum(): # Continuar hasta que no sea alfanumérico
            posible += t.value[i]
            i += 1
        if len(posible) < 2: # Identificador inválido (menos de 2 caracteres)
            print(f"\033[91mIdentificador inválido: '{posible}' en línea {t.lineno} (mínimo 2 caracteres)\033[0m")
            t.lexer.skip(len(posible))
            return
    print(f"\033[91mCarácter ilegal: '{ch}' en línea {t.lineno}\033[0m") # Mensaje de error
    t.lexer.skip(1)

lexer = lex.lex() # Construir el analizador léxico

# =========================
#     PRUEBA RÁPIDA
# =========================
if __name__ == '__main__':
    data = '''
inicio
primer = 3
segundo = 5
Si (primer < segundo)
Escribe(primer);
Sino
Escribe(segundo);
finsi
final

    '''
    print("=== TOKENS ===")
    lexer.input(data) # Proveer datos al analizador léxico
    for tok in lexer:
        # Detecta si es palabra reservada
        if tok.type in ('inicio', 'final', 'sino', 'finsi', 'Si', 'Lee', 'Escribe'): # Palabra reservada
            print(f"Palabra reservada: '{tok.value}' (línea {tok.lineno})")
        else:
            print(f"{tok.type:20} '{tok.value}' (línea {tok.lineno})")
