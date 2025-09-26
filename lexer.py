from ply import lex

# List of reserved words
Palabras_Reservadas = ('inicio', 'final', 'Si', 'sino', 'finsi', 'Lee', 'Escribe')

# List of token names.
tokens = Palabras_Reservadas + ('Operador_Asig','Operadores_Binarios', 'Letra', 'Digito', 'Num','Identificador', 'Parentesis', 'Punto_Coma')

# Regular expression rules for simple tokens
# Note: The order of these definitions matters for correct tokenization.
t_Operador_Asig = r'='
t_Operadores_Binarios = r'\+|-|\*|/|%|<=|>=|<>|==|<|>'
t_Letra = r'[a-z]'
t_Digito = r'[0-9]'
t_Parentesis = r'\(|\)'
t_Punto_Coma = r';'

# A regular expression rule with some action code
def t_Identificador(t):
    r'[a-z][a-z0-9]*'
    if t.value in Palabras_Reservadas:
        t.type = t.value
        t.reservada = True
    else:
        t.type = 'Identificador'
        t.reservada = False
    return t


def t_Si(t): # Define a rule for the 'Si' reserved word
    r'Si'
    t.reservada = True
    return t

def t_Lee(t): # Define a rule for the 'Lee' reserved word
    r'Lee'
    t.reservada = True
    return t

def t_Escribe(t): # Define a rule for the 'Escribe' reserved word
    r'Escribe'
    t.reservada = True
    return t    

# A regular expression rule with some action code
def t_Num(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule for newlines to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1) # Skip the illegal character

# Build the lexer
lexer = lex.lex()

# Test the lexer with a sample input
if __name__ == "__main__":
    data = '''
    inicio
    primer = 3
    segundo = 5;
    Si (primer < segundo) 
    Escribe(primer);
    sino
    Escribe(segundo);
    finsi
    final
    '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize and print the tokens
    for tok in lexer: # Get the next token
        if hasattr(tok, 'reservada') and tok.reservada: # Check if it's a reserved word
            print(f"Palabra reservada: '{tok.value}' en línea {tok.lineno}") # Print reserved words differently
        else: # Print other tokens normally
            print(f"{tok.type}: '{tok.value}' en línea {tok.lineno}")