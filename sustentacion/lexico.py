import ply.lex as lex
reserved = { 'print':'PRINT' }
# List of token names.   This is always required
tokens = (
   'INTEGER',
   'FLOAT',
   'STR',
    'MODULE',
    'EQUALS',
    'SEMICOLON',
    'COMMA',
    'COLON',
    'ID', 
    'CONSTANT', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'NUMERAL', 'PUNTO', 'LPAREN', 'RPAREN',
) + tuple(reserved.values())


t_MODULE = r'%'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_PUNTO     = r'\.'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
# A regular expression rule with some action code

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STR(t):
    r'"[^"]*"|\'[^"]*\''
    t.value = str(t.value)
    return t

def t_ID(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') 
    return t

def t_CONSTANT(t):
    r'[A-Z][a-zA-Z_0-9]*'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_COMMENTS(t):
    r'\#.*'
    pass

# Error handling rule
def t_error(t):
    print("Léxico no válido '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

data = '''
[10, 20, True, False, "ESPOL", 3.5]
{"cedula": "029292992", "edad": 23, "matricula": "039292"} #debe permitir n elementos, la clave puede ser string o int, los valores cualquier tipo de dato.
{20, False, "LP", 3.4} #debe permitir n elementos, incluso otro set
#comentario de 1 linea
print("Hola mundo")
print(10) #cualquier tipo de dato, 1 o mas argumentos
variable = [12, 3, "hol", 4.5] #la estructura que ud haya elegido
print(variable)
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)