#versão dicionário python

import ply.yacc as yacc
import json
import re
from tomllex import tokens




jsonn= {}

def p_toml(p):
    'toml : titles sections '
    p[0] ='{\n'+ p[1] + "\n"+ p[2] + '\n}'


def p_titles(p):
    '''titles : title
              | titles title'''

    if len(p) == 2:
        p[0] = p[1]
    
    if len(p) == 3:
        p[0] = p[1] + p[2]
    

def p_title(p):
    '''title : KEY DELIMITER VALUE'''
    jsonn[p[1]] = p[3]
    p[0]= '"'+p[1]+'"'+':'+p[3] 
       


def p_tabletitle(p):
    'tabletitle : APAR KEY FPAR'
    p[0] = p[2] 
   




    
    
    

def p_sections(p):
    '''sections : sections section
                | section'''
   
    if (len(p)==2) :
        p[0] = p[1]

    if (len(p)==3):
        p[0] = p[1] + ',' + p[2]
   #print(p[0])
     

    

def p_section(p):
    '''section : tabletitle conteudo
               | tabletitle'''
    
    split = re.split(r'\.', p[1])
    current_dict = jsonn
    for pal in split[:-1]:
        if pal not in current_dict:
            current_dict[pal] = {}
        current_dict = current_dict[pal]
    current_dict[split[-1]] = {}
    current_dict = current_dict[split[-1]]
        ####################
    if len(p) == 3:    
        pares = re.split(r';;;;', p[2])
        for par in pares:
            kv = re.split(r'::::', par)
            fmatch = re.fullmatch(r'([^\."]+)\.(.+)', kv[0])
            if fmatch:
                dic = fmatch.group(1)
                key = fmatch.group(2)
                if dic not in current_dict:
                    current_dict[dic] = {}
                current_dict[dic][key] = kv[1]
            else:
                current_dict[kv[0]] = kv[1]
    
        
    p[0] = p[1]
   # print(p[0])



 
def p_conteudo(p):
    '''conteudo : conteudo KEY DELIMITER VALUE 
                | KEY DELIMITER VALUE '''
     
    if len(p) == 4 :
        p[0] = p[1] + '::::' + p[3]
    if len(p) == 5 :
        p[0] = p[1] + ';;;;' + p[2] + '::::' + p[4]
   # print(p[0])


def p_error(p):
    print("Erro sintático!")

parser = yacc.yacc()


with open('tabela.toml', 'r') as arquivo: 
    conteudo = arquivo.read()


#dados = tomllib.loads(conteudo)

data = parser.parse(conteudo)
print(jsonn)
#print(data)
with open("tabela.json", "w") as f:
    json.dump(jsonn,f,indent=6)
    
