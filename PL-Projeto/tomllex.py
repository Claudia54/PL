import ply.lex as lex

# Definição dos tokens
tokens = (
    'PONTO',
    'APAR',
    'FPAR',
    'KEY',
    'VALUE',
    'DELIMITER',
    'COMMENT',
    'LISTVALUE')

# Expressões regulares para os tokens
t_PONTO = r'\.'
t_APAR = r'\['
t_FPAR = r'\]'
t_KEY = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_DELIMITER = r'[=]'
t_COMMENT = r'\#[^\n]*'



def t_LISTVALUE(t):
   r'(?<=[=]\s)\[\s*([^,\]]*)*(,[\n]?\s*([^,\]]*)*)?\]'
   return t

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


lexer.input("""
title = "TOML Example"
[owner]
name = "Tom Preston-Werner"
date = 2010-04-23
time = 21:30:00
[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true
[servers]
[servers.alpha]
  ip = "10.0.0.1"
  dc = "eqdc10"
[servers.beta]
  ip = "10.0.0.2"
  dc = "eqdc10"
# Line breaks are OK when inside arrays
hosts = [
"alpha",
"omega" ]
""")
#while tok := lexer.token():
   # print(tok)

