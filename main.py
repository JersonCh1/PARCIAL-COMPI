import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = (
    'LLAVEI', 'LLAVED', 'ASIGNAR', 'ID', 'NUM', 'SUMA', 'RESTA', 'MULTI', 'DIVIDIR',
    'PARENI', 'PAREND', 'SEMICOLON'
)

# Expresiones regulares para tokens simples
t_LLAVEI = r'\{'
t_LLAVED = r'\}'
t_PARENI = r'\('
t_PAREND = r'\)'
t_ASIGNAR = r'='
t_SEMICOLON = r';'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVIDIR = r'/'
t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_NUM = r'\d+'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Definición de la estructura de datos para el árbol sintáctico
class Nodo:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    def imprimir(self, nivel=0):
        print('  ' * nivel + f'{self.tipo}: {self.valor}')
        for hijo in self.hijos:
            hijo.imprimir(nivel + 1)

    def to_dot(self, dot, node_id=0):
        label = f"{self.tipo}: {self.valor}"
        dot.append(f'  node{node_id} [label="{label}"];')
        current_id = node_id
        for child in self.hijos:
            child_id = current_id + 1
            dot.append(f'  node{current_id} -> node{child_id};')
            child_id = child.to_dot(dot, child_id)
            current_id = child_id
        return current_id

# Reglas gramaticales
def p_program(p):
    'program : block'
    p[0] = p[1]

def p_block(p):
    'block : LLAVEI statements LLAVED'
    block_node = Nodo('block', None)
    for stmt in p[2]:
        block_node.agregar_hijo(stmt)
    p[0] = block_node

def p_statements(p):
    '''statements : statement statements
                  | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_statement(p):
    '''statement : assign_statement
                 | expression_statement'''
    p[0] = p[1]

def p_assign_statement(p):
    'assign_statement : ID ASIGNAR expression SEMICOLON'
    p[0] = Nodo('assign', [Nodo('ID', p[1]), p[3]])

def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'
    p[0] = p[1]

def p_expression(p):
    '''expression : expression SUMA term
                  | expression RESTA term
                  | term'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = Nodo('suma', [p[1], p[3]])
        elif p[2] == '-':
            p[0] = Nodo('resta', [p[1], p[3]])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term MULTI factor
            | term DIVIDIR factor
            | factor'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = Nodo('multi', [p[1], p[3]])
        elif p[2] == '/':
            p[0] = Nodo('dividir', [p[1], p[3]])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUM
              | ID
              | PARENI expression PAREND'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = Nodo('num' if p[1].isdigit() else 'id', p[1])

def p_empty(p):
    'empty :'
    p[0] = []

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Construir el lexer y parser
lexer = lex.lex()
parser = yacc.yacc()

# Función principal para probar el parser con entrada de texto y exportar a Graphviz
if __name__ == "__main__":
    input_data = '{ x = 3 + 4 * (2 - 1); }'
    arbol = parser.parse(input_data, lexer=lexer)
    if arbol:
        dot_output = ["digraph syntax_tree {"]
        arbol.to_dot(dot_output)
        dot_output.append("}")
        with open("syntax_tree.dot", "w") as f:
            f.write("\n".join(dot_output))
        print("Archivo DOT creado. Cárgalo en Graphviz Online para visualizar.")
    else:
        print("No se pudo generar el árbol sintáctico.")
