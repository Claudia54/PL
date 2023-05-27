
import ply.yacc as yacc
import json 
from tomllex import tokens



jsonn= {}

def p_toml(p):
    'toml : title sections '
    p[0] ='{\n'+ p[1] + "\n"+ p[2] + '\n}'
    


#def p_tabletitle(p):
#    'tabletitle : APAR KEY FPAR'
#    p[0]= p[2]
   
     
                  
#def p_titulo(p):
    #'''titulo : KEY
              #| titulo PONTO KEY'''
    


def p_tabletitle(p):
    'tabletitle : APAR titulosection FPAR '
    p[0] = p[2] 



count=0

def p_titulosection(p):
    '''titulosection : KEY
                    | titulosection PONTO KEY'''
   
    
    if (len==2):
        p[0] =p[1] +":{\n"
    
    if (len==4):
        p[0] =p[1] + p[2] +":{\n "
        




def p_title(p):
    'title : KEY DELIMITER VALUE'
    p[0]= '"'+p[1]+'"'+':'+p[3] 
    
    

def p_sections(p):
    '''sections : sections section
                | section'''
   
    if (len(p)==2) :
        p[0] = p[1]

    if (len(p)==3):
        p[0] = p[1] + ',' + p[2]
     

    

def p_section(p):
    '''section : tabletitle conteudo'''
    print(p[1])
    p[0]='"'+p[1]+'"'+':{\n'+p[2]



 
def p_conteudo(p):
    '''conteudo : conteudo KEY DELIMITER VALUE 
                | KEY DELIMITER VALUE
                | KEY DELIMITER LISTVALUE '''
    
    #if len(p) == 2 : 
       # p[0] = p[1]
    #if len(p) == 3 :
     #   p[0] = p[1] + p[2] 
    if len(p) == 4 :
        p[0] = '"' + p[1] + '"' + ':' + p[3] +'\n'
    if len(p) == 5 :
        p[0] = p[1] + ',' + '"' + p[2] + '"' + ':' + p[4] +'\n' 
    #print(p[0])



def p_error(p):
    print("Erro sintático!")

parser = yacc.yacc()


with open('tabela.toml', 'r') as arquivo: 
    conteudo = arquivo.read()


#dados = tomllib.loads(conteudo)

data = parser.parse(conteudo)
print(data)
with open("tabela.json", "w") as f:
    json.dump(data,f,indent=6)
    
