import ply.yacc as yacc

from tomllex import tokens


def p_tabela(p):
    'toml : title sections '
    #p[0]= '{\n'+p[1]+ '\n'+ p[2] +'\n}'
    #print(p[0])
    

def p_title(p):
    'title : KEY DELIMITER VALUE'
    p[0]= p[1]+':'+p[3] +','
    print(p[0])
    

def p_sections(p):
    '''sections : sections section
                | section'''
    if (len==2) :
        p[0] = p[1]+p[2]
       # print(p[0])

    if (len==3):
        p[0] = p[1]+p[2]+p[3]
        #print(p[0])

    

def p_section(p):
    '''section : SECTIONTITLE conteudo'''
    p[0]=p[1]+':{\n'+p[2] +'}'
    print(p[0])
    

 
def p_conteudo(p):
    '''conteudo : conteudo section 
                | conteudo KEY DELIMITER VALUE 
                | KEY DELIMITER VALUE
                | section'''
    
    if len(p) == 2 : 
        p[0]=p[1]
    if len(p)== 3 :
        p[0]=p[1]
    if len(p) == 4 :
        p[0] = p[1]+':'+p[3] +',' +'\n'
    if len(p) ==5 :
        p[0] = p[1]+p[2]+':'+p[4] +',\n' 
    #print(p[0])

def p_error(p):
    print("Erro sintático!")

parser = yacc.yacc()

texto_input = """
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

  
"""

 
csv = parser.parse(texto_input)
with open("tabela.json", "w") as f:
    f.write(csv)
    
