import ply.lex as lex

# Definição dos tokens
tokens = (
    'APAR',
    'FPAR',
    'KEY',
    'VALUE',
    'DELIMITER',
    'COMMENT',
    'LISTVALUE',
    )

# Expressões regulares para os tokens
t_APAR = r'\['
t_FPAR = r'\]'
t_KEY = r'([a-zA-Z0-9_][a-zA-Z0-9_\.,]*) | "[\w\.,]*\s*[\w\.,]*"'
t_DELIMITER = r'[=]'

def t_COMMENT(t):
    r'\#[^\n]*'
    pass

def t_VALUE(t):
  r'(?<=[=]\s).+'
  return t

# Ignorar espaços em branco e quebras de linha
t_ignore = ' \t\n'

# Função para tratar erros
def t_error(t):
    print("Caracter não reconhecido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()

with open('tabelateste.toml', 'r') as arquivo: 
    conteudo = arquivo.read()

lexer.input(conteudo)

while tok := lexer.token():
    print(tok)



