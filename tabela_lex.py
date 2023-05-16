import ply.lex as lex 

tokens={
    'BARRA',
    'TRACO',
    'INT',
    'FLOAT',
    'TEXTO'
}

t_BARRA =r'\|'
t_TRACOS =r'-+'


def t_FLOAT(t):
    r'\d+'
    t.value = float(t.value)
    return t
    


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TEXTO(t):
    r'[\w\-]+(\s+[\w\-]+)*'
    return t



