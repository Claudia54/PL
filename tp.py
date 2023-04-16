import ply.yacc as yacc 
import ply.lex as lex
import json 

import ply.lex as lex
import ply.yacc as yacc
import json

# Definindo os tokens
tokens = (
    'SECTION',
    'KEY',
    'VALUE',
    'STRING',
    'NUMBER',
    'TRUE',
    'FALSE',
)

# Expressões regulares para cada token
t_SECTION = r'\[.*\]'
t_KEY = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_STRING = r'"(?:[^"\\]|\\.)*"'
t_NUMBER = r'-?\d+(?:\.\d+)?'
t_TRUE = r'true'
t_FALSE = r'false'

# Ignorando espaços e quebras de linha
t_ignore = ' \n\t'

