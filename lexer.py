from ply import lex

# List of token names.
tokens = ('Palabras_Reservadas', 'Operador_Asig','Operadores_Binarios', 'Letra', 'Digito', 'Num','Identificador', 'Parentesis', 'Punto_Coma')

# Regular expression rules for simple tokens
# Note: The order of these definitions matters for correct tokenization.
t_Palabras_Reservadas = r'\b(inicio|final|Si|sino|finsi|Lee|Escribe)\b'
t_Operador_Asig = r'='
t_Operadores_Binarios = r'\+|-|\*|/|%|<=|>=|<>|==|<|>'
t_Letra = r'[a-z]'
t_Digito = r'[0-9]'
t_Num = r'\d+'
t_Identificador = r'[a-z][a-z0-9]+'
t_Parentesis = r'\(|\)'
t_Punto_Coma = r';'

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
    x = 10;
    Si (x > 5) Escribe(x);
    finsi
    final
    '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize and print the tokens
    for tok in lexer:
        print(tok)
        