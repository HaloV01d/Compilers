from ply import lex

# =========================
#       ANALIZADOR LÉXICO
# =========================

RESERVADAS = { # Palabras reservadas en minúsculas
    'inicio': 'INICIO',
    'final': 'FINAL',
    'sino': 'SINO',
    'finsi': 'FINSI',
    'si': 'SI',
    'lee': 'LEE',
    'escribe': 'ESCRIBE',
}

tokens = ( # Lista de tokens
    'INICIO', 'FINAL', 'SINO', 'FINSI',
    'SI', 'LEE', 'ESCRIBE',
    'OPERADOR_ASIG', 'OPERADORES_BINARIOS',
    'MENOR_IGUAL', 'MAYOR_IGUAL', 'IGUAL_IGUAL', 'DIFERENTE',
    'NUM', 'IDENTIFICADOR',
    'LPAREN','RPAREN', 'PUNTO_COMA',
)

literals = ['+', '-', '*', '/', '%', '<', '>', '=', '(', ')', ';']

t_OPERADOR_ASIG = r'=' # Operador de asignación
t_OPERADORES_BINARIOS = r'<=|>=|==|<>' # Operadores binarios
t_LPAREN = r'\(' # Paréntesis izquierdo
t_RPAREN = r'\)' # Paréntesis derecho
t_PUNTO_COMA = r';' # Punto y coma
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_IGUAL_IGUAL = r'=='
t_DIFERENTE = r'<>'

def t_NUM(t): # Número entero
    r'\d+'
    t.value = int(t.value)
    return t

def t_SI(t): # Si
    r'Si'
    return t

def t_LEE(t): # Lee
    r'Lee'
    return t

def t_ESCRIBE(t): # Escribe
    r'Escribe'
    return t

def t_IDENTIFICADOR(t): # Identificador
    r'[a-z][a-z0-9]+'
    if t.value in RESERVADAS: # Verificar si es palabra reservada
        t.type = RESERVADAS[t.value]
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
if __name__ == '__main__':  # Prueba rápida del analizador léxico
    ruta = 'C:\\Users\\Alondra Soto\\OneDrive\\Documents\\Development\\Compilers\\Test\\Caso_Correcto1.txt'  #  Cambia esto por la ruta de tu archivo de entrada
    with open(ruta, 'r', encoding='utf-8') as archivo:
        data = archivo.read()

    print("=== TOKENS ===")
    lexer.input(data)  # Proveer datos al analizador léxico

    for tok in lexer:
        if tok.type in ('INICIO', 'FINAL', 'SINO', 'FINSI', 'SI', 'LEE', 'ESCRIBE'):
            print(f"PALABRA RESERVADA: '{tok.value}' (línea {tok.lineno})")
        else:
            print(f"{tok.type}: '{tok.value}' (línea {tok.lineno})")
