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
#t_PONTO = r'\.(?=.*\])|\[(?=.\])(.*\.)?'
t_APAR = r'\['
t_FPAR = r'\]'
t_KEY = r'"?[a-zA-Z0-9_][a-zA-Z0-9_\.,]*"?'
t_DELIMITER = r'[=]'
t_COMMENT = r'\#[^\n]*'

def t_VALUE(t):
  r'(?<=[=]\s).+'
  return t

#def t_LISTVALUE(t):
#   r'(?<=[=]\s)\[\s*([^,\]]*)*(,[\n]?\s*([^,\]]*)*)?\]'
 #  return t



# Ignorar espaços em branco e quebras de linha
t_ignore = ' \t\n'

# Função para tratar erros
def t_error(t):
    print("Caracter não reconhecido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()

with open('tabela.toml', 'r') as arquivo: 
    conteudo = arquivo.read()

lexer.input(conteudo)

while tok := lexer.token():
    print(tok)



