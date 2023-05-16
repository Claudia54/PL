from tabela_lex import tokens

def p_tabela (p):
    'tabela :cabeçalho linh_lixo conteudo'
    p[0] =p[1]+'\n'+p[3]

def p_cabecalho(p):
    'cabecalho:BARRA valores_cab BARRA'
    p[0] =','.join(p[2])

def p_valores_cab(p):
    '''valores_cab : valores_cab BARRA valçor_cab | valor_cab'''
    if(len(p) ==2):
        p[0]=[p[1]]
    else :
        p[0]= p[1] +[p[3]]


def p_valor_cab(p):
    'valor_cab :TEXTO'
    p[0] =p[1]


def p_linha_lixo(p):
    'linha_lixo :BARRA vals_lixo BARRA'
    pass

def p_vals_lixo (p):
    '''vals_lixo : vals_lixo BARRA TRACOS '''
    pass

def p_conteudo(p):
    '''conteudo : linha | conteudo linha'''
    if(len(p) ==2):
        p[0]=p[1]
    else :
        p[0]= p[1] +'\n'+p[2]



def p_linha(p):
    'linha: BARRA valores BARRA'
    p[0] =','.join(p[2])
   


def p_valores(p):
    '''valores: valores BARRA valor| valor '''
    if(len(p) ==2):
        p[0]=[p[1]]
    else :
        p[0] =p[1]+[p[3]]

def p_valor(p):
    '''valor: TEXTO| INT|FLOAT'''
    p[0]=p[1]


#debug=TRUE