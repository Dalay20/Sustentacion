import ply.yacc as yacc
from lexico import tokens

def p_body(p):
    '''body : sentence
            | imprimir 
            | array'''

def p_asignacion(p):
    '''sentence : ID EQUALS factor SEMICOLON
                | ID EQUALS array'''

def p_array(p):
    'array : LBRACE cuerpo RBRACE'

def p_cuerpo(p):
    '''cuerpo : dato COMMA cuerpo 
              | dato'''

def p_dato(p):
    'dato : tipo COLON factor'

def p_clave(p):
    '''tipo : INTEGER
            | STR'''

def p_factor_valor(p):
    '''factor : INTEGER
            | FLOAT
            | STR'''

def p_imprimir(p):
    'imprimir : PRINT LPAREN argumentos RPAREN'

def p_argumentos(p):
    '''argumentos : factor
                  | factor COMMA argumentos'''

# Error rule for syntax errors
def p_error(p):
    print("Error de sintaxis")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('sustentación > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    if result!=None:
        print(result)

#pruebass
# x = 123;
#nombre = "Juan";
# pi = 3.14;
#  pi ={"cedula": "029292992", "edad": 23, "matrícula": "039292"} 
#comentario de 1 línea
#print("Hola mundo")