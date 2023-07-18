# 99187 Bruno Miguel Vaz e Campos

#-------------------------------------------------------------------------------
#                                 TAD posicao
# representacao interna: cadeia de caracteres -> o primeiro caracter eh 
# referente a coluna e o segundo caracter eh referente a linha

#    cria_posicao: str x str -> booleano
#    cria_copia_posicao: posicao -> posicao
#    obter_pos_c: posicao -> str
#    obter_pos_l: posicao -> str
#    eh_posicao: universal -> booleano
#    posicoes_iguais: posicao x posicao -> booleano
#    posicao_para_str: posicao -> str

#-------------------------------------------------------------------------------

def valida_posicao(arg1, arg2):
    # valida_posicao: str x str -> booleano
    ''' devolve True caso o arg1 seja 'a', 'b' ou 'c' e o arg2 seja '1', '2' ou
    '3' e False caso contrario '''
    return type(arg1) == str and type(arg2) == str and arg1 in ('a', 'b', 'c') \
           and arg2 in ('1', '2', '3')

#-------------------------------- Construtores ---------------------------------
def cria_posicao(c, l):
    # cria_posicao: str x str -> posicao
    ''' recebe duas cadeias de caracteres correspondentes a coluna c e a linha l
    de uma posicao e devolve a posicao correpespondente '''
    if valida_posicao(c, l):
        return c + l
    else:
        raise ValueError('cria_posicao: argumentos invalidos')

def cria_copia_posicao(p):
    # cria_copia_posicao: posicao -> posicao
    ''' recebe uma posicao e devolve uma copia da nova posicao '''
    return (p + '.')[:-1]
# temos que validar o argumento passado como parametro concreto??
    
#--------------------------------- Seletores -----------------------------------
def obter_pos_c(p):
    # obter_pos_c: posicao -> str
    ''' devolve a componente coluna c da posicao p '''
    return p[0]

def obter_pos_l(p):
    # obter_pos_l: posicao -> str
    ''' devolve a componente linha l da posicao p '''
    return p[1]

#------------------------------- Reconhecedores --------------------------------
def eh_posicao(arg):
    # eh_posicao: universal -> booleano
    ''' devolve True caso o seu argumento seja um TAD posicao e False caso
    contrario '''
    return type(arg) == str and len(arg) == 2 and valida_posicao(arg[0], arg[1])

#---------------------------------- Testes -------------------------------------
def posicoes_iguais(p1, p2):
    # posicoes_iguais: posicao x posicao -> booleano
    ''' devolve True apenas se p1 e p2 sao posicoes e sao iguais '''
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

#------------------------------- Transformadores -------------------------------
def posicao_para_str(p):
    # posicao_para_str: posicao -> str
    ''' devolve a cadeia de caracteres 'cl' que representa o seu argumento,
    sendo os valores c e l as componentes coluna e linha de p '''
    return p

#--------------------------- Funcoes de alto nivel -----------------------------
def obter_posicoes_adjacentes(p):
    # obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    ''' devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a
    ordem de leitura do tabuleiro '''
    
    c, l, pos_adjacentes = obter_pos_c(p), obter_pos_l(p), ()
    c_para_int = ord(c)
    
    for i in range(-1, 2):
        for ii in range(-1, 2):
            if i != 0 and ii != 0:
                if (c_para_int + int(l)) % 2 == 0:
                    if eh_posicao((chr(c_para_int + ii) + str(int(l) + i))) \
                       and not posicoes_iguais(p, cria_posicao\
                        (chr(c_para_int + ii), str(int(l) + i))):
                        pos_adjacentes += \
                            (posicao_para_str(cria_posicao\
                                (chr(c_para_int + ii), str(int(l) + i))),)
            else:
                if eh_posicao((chr(c_para_int + ii) + str(int(l) + i))) \
                   and not posicoes_iguais(p, cria_posicao\
                    (chr(c_para_int + ii), str(int(l) + i))):
                    pos_adjacentes += (posicao_para_str(cria_posicao\
                                (chr(c_para_int + ii), str(int(l) + i))),)                      


    return pos_adjacentes


#-------------------------------------------------------------------------------
#                                 TAD peca
# representacao interna: cadeia de caracteres, com um unico caracter
#    cria_peca: str -> peca
#    cria_copia_peca: peca -> peca
#    eh_peca: universal -> booleano
#    pecas_iguais: peca x peca -> booleano
#    peca_para_str: peca -> str
#-------------------------------------------------------------------------------
def valida_peca(arg):
    # valida_peca: str -> booleano
    ''' devolve True caso o arg seja 'X', 'O' ou ' ' e False caso contrario '''
    return type(arg) == str and arg in ('X', 'O', ' ')

#-------------------------------- Construtores ---------------------------------
def cria_peca(s):
    # cria_peca: str -> peca
    ''' recebe uma cadeia de caracteres correspondente ao identificador de um
    dos dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve a peca
    correspondete '''
    if valida_peca(s):
        return s
    else:
        raise ValueError('cria_peca: argumento invalido')

def cria_copia_peca(j):
    # cria_copia_peca: peca -> peca
    ''' recebe uma peca e devolve uma copia nova da peca '''
   
    return (j + '.')[:-1] # not sure

#------------------------------- Reconhecedores --------------------------------
def eh_peca(arg):
    # eh_peca: universal -> booleano
    ''' devolve True caso o seu argumento seja um TAD peca e False caso
    contrario '''
    return valida_peca(arg)

#---------------------------------- Testes -------------------------------------
def pecas_iguais(j1, j2):
    # pecas_iguais: peca x peca -> booleano
    ''' devolve True apenas se p1 e p2 sao pecas e sao iguais '''
    return eh_peca(j1) and eh_peca(j2) and j1 == j2

#------------------------------- Transformadores -------------------------------
def peca_para_str(j):
    # peca_para_str: peca -> str
    ''' devolve a cadeia de caracteres que representa o jogador dono da peca,
    isto e, '[X]', '[O]' ou '[ ]\''''
    return '[' + j + ']'
#--------------------------- Funcoes de alto nivel -----------------------------
def peca_para_inteiro(j):
    # peca_para_inteiro: peca -> N
    ''' devolve um inteiro valor 1, -1 ou 0, dependendo se a peca eh do jogador
    'X', 'O' ou livre, respetivamente '''
    
    if pecas_iguais(j, cria_peca('X')):
        return 1
    elif pecas_iguais(j, cria_peca('O')):
        return -1
    else:
        return 0

#-------------------------------------------------------------------------------
#                                 TAD tabuleiro
# representacao interna: lista, composta por 3 elementos. Cada um desses
# elementos eh uma lista composta por 3 elementos. Cada um desses elementos
# eh uma cadeia de caracteres, composta por um unico caracter, referente a uma
# peca

#    cria_tabuleiro: {} -> tabuleiro
#    cria_copia_tabuleiro: tabuleiro -> tabuleiro
#    obter_peca: tabuleiro x posicao -> peca
#    obter_vetor: tabuleiro x str -> tuplo de pecas
#    coloca_peca: tabuleiro x peca x posicao -> tabuleiro
#    remove_peca: tabuleiro x posicao -> tabuleiro
#    move_peca: tabuleiro x posicao x posicao -> tabuleiro
#    eh_tabuleiro: universal -> booleano
#    eh_posicao_livre: tabuleiro x posicao -> booleano
#    tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
#    tabuleiro_para_str: tabuleiro -> str
#    tuplo_para_tabuleiro: tuplo -> tabuleiro

#-------------------------------------------------------------------------------

#-------------------------------- Construtores ---------------------------------
def cria_tabuleiro():
    # cria_tabuleiro: {} -> tabuleiro
    ''' devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes ocupadas por
    pecas de jogador '''
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def cria_copia_tabuleiro(t):
    # cria_copia_tabuleiro: tabuleiro -> tabuleiro
    ''' recebe um tabuleiro e devolve uma copia nova do tabuleiro '''
    return t.copy()

#--------------------------------- Seletores -----------------------------------
def obter_peca(t, p):
    # obter_peca: tabuleiro x posicao -> peca
    ''' devolve a peca na posicao p do tabuleiro. Se a posicao nao estiver
    ocupada, devolve uma peca livre '''
    return t[int(obter_pos_l(p)) - 1][ord(obter_pos_c(p)) - 97]

def obter_vetor(t, s):
    # obter_vetor: tabuleiro x str -> tuplo de pecas
    ''' devolve todas as pecas da linha ou coluna especificada pelo seu 
    argumento s '''
    
    tup_pecas = ()
    
    if s in ('a', 'b', 'c'):
        index_c = ord(s) - 97
        for i in range(3):
            tup_pecas += (t[i][index_c],)
    else:
        index_l = int(s) - 1
        for i in range(3):
            tup_pecas += (t[index_l][i],)
       
    return tup_pecas
            
    
#------------------------------- Modificadores ---------------------------------
def coloca_peca(t, j, p):
    # coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    ''' modifica destrutivamente o tabuleiro t colocando a peca j na posicao p,
    e devolve o proprio tabuleiro '''
    t[int(obter_pos_l(p)) - 1][ord(obter_pos_c(p)) - 97] = j
    return t

def remove_peca(t, p):
    # remove_peca: tabuleiro x posicao -> tabuleiro
    ''' modifica destrutivamente o tabuleiro t removendo a peca da posicao p,
    e devolve o proprio tabuleiro '''
    t[int(obter_pos_l(p)) - 1][ord(obter_pos_c(p)) - 97] = cria_peca(' ')
    return t

def move_peca(t, p1, p2):
    # move_peca: tabuleiro x posicao x posicao -> tabuleiro
    ''' modifica destrutivamente o tabuleiro t movendo a peca que se encontra
    na posicao p1 para a posicao p2, e devolve o proprio tabuleiro '''
    
    c_p1, l_p1 = obter_pos_c(p1), int(obter_pos_l(p1))
    peca_em_p1 = cria_peca(t[l_p1 - 1][ord(c_p1) - 97])
    
    t[l_p1 - 1][ord(c_p1) - 97], \
        t[int(obter_pos_l(p2)) - 1][ord(obter_pos_c(p2)) - 97] = \
        cria_peca(' '), peca_em_p1   
    return t




#---------------------- Funcoes auxiliares do eh_tabuleiro ---------------------

def soma_pecas_jogadores(arg):
    # soma_pecas_jogadores: universal -> tuplo de inteiros
    ''' devolve um tuplo de inteiros com dois elementos, em que o primeiro
    corresponde ao numero de pecas do jogador que joga com a peca 'X' e o
    segundo elemento corresponde ao numero de pecas do jogador que joga com a
    peca 'O' '''
    
    soma_X, soma_O = 0, 0
    
    for i in range(1, 4):
        linha = obter_vetor(arg, str(i))
        for el in linha:
            if pecas_iguais(el, cria_peca('X')):
                soma_X += 1
            elif pecas_iguais(el, cria_peca('O')):
                soma_O += 1
    return (soma_X, soma_O)
            

def situacoes_vitoria(arg, fila):
    # situacoes_vitoria: universal x str -> inteiro
    ''' devolve um inteiro, relativo ao numero de situacoes de vitoria, em
    linhas ou colunas, consoante o que for especificado no argumento fila '''
    num_situacoes_vitoria = 0

    for i in range(1, 4):
        soma = 0
        
        if fila == 'linha':
            vetor = obter_vetor(arg, str(i))
        else:
            vetor = obter_vetor(arg, chr(i + 96))
        
        for el in vetor:
            soma += peca_para_inteiro(el)
           
        if abs(soma) == 3:
            num_situacoes_vitoria += 1
           
    # se existem 2 vencedores em simultaneo, retorna False   
    if num_situacoes_vitoria == 2:
        return 2
    # caso haja apenas um vencedor, retorna True e nem sequer se testam
    # as situacoes de vitoria para as colunas
    elif num_situacoes_vitoria == 1:
        return 1
    else:
        return 0
    
#-------------------------- Fim das funcoes auxiliares -------------------------

#------------------------------- Reconhecedores --------------------------------

def eh_tabuleiro(arg):
    # eh_tabuleiro: universal -> booleano
    ''' devolve True caso o seu argumento seja um TAD tabuleiro e False caso
    contrario '''
    
    if type(arg) != list or len(arg) != 3:
        return False
    else:
        for i in range(3):
            if type(arg[i]) != list or len(arg[i]) != 3:
                return False
            else:
                for ii in range(3):
                    if not eh_peca(arg[i][ii]):
                        return False
    
    numero_pecas = soma_pecas_jogadores(arg)                
    soma_X, soma_O = numero_pecas[0], numero_pecas[1]
                
    if soma_X > 3 or soma_O > 3:
        return False
    
    elif abs(soma_X - soma_O) > 1:
            return False
    else:
        if soma_X == 3 and soma_O == 3:
            
            # verificar se ha 2 situacoes de vitoria
            res_l = situacoes_vitoria(arg, 'linha')
            # caso nao haja nenhum vencedor nas linhas, verificar colunas
            if res_l == 0:
                if situacoes_vitoria(arg, 'coluna') != 2:
                    return True # caso haja 1 ou nenhuma situacao de vitoria
                else:
                    return False # caso existam 2 situacoes de vitoria
            else: # retorna True, caso haja um vencedor nas linhas ou False,
                # caso existam 2 situacoes simultaneas de vitoria
                if res_l == 1:
                    return True
                else:
                    return False         
        else:
            return True
                
            
def eh_posicao_livre(t, p):
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    ''' devolve True apenas no caso da posicao p do tabuleiro corresponder a
    uma posicao livre '''
    return t[int(obter_pos_l(p)) - 1][ord(obter_pos_c(p)) - 97] == \
           cria_peca(' ')



#---------------------------------- Testes -------------------------------------
def tabuleiros_iguais(t1, t2):
    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    ''' devolve True apenas se t1 e t2 sao tabuleiros e sao iguais '''
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2



#------------------------------- Transformadores -------------------------------
def tabuleiro_para_str(t):
    # tabuleiro_para_str: tabuleiro -> str
    ''' devolve a cadeia de caracteres que representa o tabuleiro como mostrado
    nos exemplos do enunciado do projeto '''
    res = '   a   b   c\n'
    for i in range(3):
        res += str(i + 1) + ' ' + peca_para_str(t[i][0]) + '-' + \
            peca_para_str(t[i][1]) + '-' + peca_para_str(t[i][2])
        if i == 0:
            res += '\n   | \ | / |\n'
        elif i == 1:
            res += '\n   | / | \ |\n'
    return res
        
#---------------------------------- funcao auxiliar ----------------------------
def converte_para_peca(val):
    # converte_para_peca: inteiro -> peca
    ''' recebe um inteiro (-1, 0 ou 1) e devolve a peca correspondente a esse
    valor '''
    if val == 1:
        return cria_peca('X')
    elif val == -1:
        return cria_peca('O')
    else:
        return cria_peca(' ')

#-------------------------------------------------------------------------------


def tuplo_para_tabuleiro(t):
    # tuplo_para_tabuleiro: tuplo -> tabuleiro
    ''' devolve o tabuleiro que eh representado pelo tuplo t com 3 tuplos, cada
    um deles contendo 3 valores inteiros iguais a 1, -1 ou 0, tal como no
    primeiro projeto '''
    
    lista = []
    
    for el in t:
        sub_lista = []
        for val in el:
            sub_lista.append(converte_para_peca(val))
        lista.append(sub_lista)    
        
    return lista

#--------------------------- Funcoes de alto nivel -----------------------------

def obter_ganhador(t):
    # obter_ganhador: tabuleiro -> peca
    ''' devolve uma peca do jogador que tenha as suas 3 pecas em linha na
    vertical ou na horizontal no tabuleiro. Se nao existir nenhum ganhador,
    devolve uma peca livre '''
    for i in ('1', '2', '3', 'a', 'b', 'c'):
        soma_fila = 0
        vetor = obter_vetor(t, i)
        for el in vetor:
            soma_fila += peca_para_inteiro(el)
        if soma_fila == 3:
            return cria_peca('X')
        elif soma_fila == -3:
            return cria_peca('O')
    return cria_peca(' ')
        

def obter_posicoes_livres(t):
    # obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    ''' devolve um tuplo com as posicoes nao ocupadas pelas pecas de qualquer
    um dos dois jogadores na ordem de leitura do tabuleiro '''
    pos_livres = ()
    # l -> linha ; c -> coluna
    for l in ('1', '2', '3'):
        for c in ('a', 'b', 'c'):
            if eh_posicao_livre(t, cria_posicao(c, l)):
                pos_livres += (posicao_para_str(cria_posicao(c, l)),)
    return pos_livres


def obter_posicoes_jogador(t, j):
    # obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
    ''' devolve um tuplo com as posicoes ocupadas pelas pecas j de um dos dois
    jogadores na ordem de leitura do tabuleiro '''
    pos_jogador = ()
    # l -> linha
    for l in ('1', '2', '3'):
        vetor = obter_vetor(t, l)
        for ii in range(3):
            if pecas_iguais(vetor[ii], j):
                pos_jogador += (cria_posicao(chr(ii + 97), l),)
    return pos_jogador

#---------------- funcao auxiliar da obter_movimento_manual --------------------
#------------------------------- e da minimax ----------------------------------

def esta_bloqueado(t, j):
    # tabuleiro x peca -> booleano
    ''' recebe um tabuleiro de jogo e uma peca e devolve True caso o jogador
    que joga com essa peca tenha todas as suas pecas bloqueadas, isto eh, nao
    existam possiveis, e False caso tenha jogadas possiveis '''
    
    for pos in obter_posicoes_jogador(t, j):
        pos_adjacentes = obter_posicoes_adjacentes(pos)
        for el in pos_adjacentes:
            if eh_posicao_livre(t, el):
                return False
    return True
#-------------------------------------------------------------------------------



#-------------------------- OBTER MOVIMENTO MANUAL -----------------------------

def obter_movimento_manual(t, j):
    # obter_movimento_manual: tuplo x peca -> tuplo de posicoes
    ''' funcao auxiliar que recebe um tabuleiro e uma peca de um jogador e
    devolve um tuplo com uma ou duas posicoes que representam uma posicao ou um
    movimento introduzido manualmente pelo jogador '''
    
    if len(obter_posicoes_livres(t)) > 3:
    # fase de colocacao
        pos_escolhida = input('Turno do jogador. Escolha uma posicao: ')
        
        if eh_posicao(pos_escolhida) and eh_posicao_livre(t, pos_escolhida):
            return (posicao_para_str(pos_escolhida),)
        else:
            raise ValueError('obter_movimento_manual: escolha invalida')
    else:    
        # fase de movimento
        mov_escolhido = input('Turno do jogador. Escolha um movimento: ')
        
        pos_atual, pos_nova = mov_escolhido[:2], mov_escolhido[2:]
        
        # se input tem movimento com posicoes iguais e o jogador tem as suas
        # pecas efetivamente bloqueadas, permite passar o turno fazendo um
        # movimento do tipo (p1, p2)
        if posicoes_iguais(pos_atual, pos_nova):
            if esta_bloqueado(t, j):
                return (posicao_para_str(cria_posicao(mov_escolhido[0], \
                mov_escolhido[1])), posicao_para_str( \
                    cria_posicao(mov_escolhido[2], mov_escolhido[3])))
            else:
                raise ValueError('obter_movimento_manual: escolha invalida')
            
        else:
            if eh_posicao(pos_atual) and not eh_posicao_livre(t, pos_atual) and\
               eh_posicao(pos_nova) and eh_posicao_livre(t, pos_nova) \
               and pos_nova in obter_posicoes_adjacentes(pos_atual):
                
                return (posicao_para_str(cria_posicao(mov_escolhido[0], \
                    mov_escolhido[1])), posicao_para_str( \
                        cria_posicao(mov_escolhido[2], mov_escolhido[3])))
            
        raise ValueError('obter_movimento_manual: escolha invalida')                

#-------------------------------------------------------------------------------



#-------------------------------- MINIMAX --------------------------------------

def minimax(tabuleiro, jogador, profundidade, seq_movimentos):
    # minimax: tabuleiro x peca x inteiro x tuplo -> tuplo (inteiro, tuplo)
    ''' recebe um tabuleiro de jogo, a peca relativa ao jogador com o turno
    atual, o nivel de profundidade pretendido para a funcao recursiva e um
    tuplo que guarda a sequencia de movimentos. Devolve o valor do estado do
    tabuleiro (-1, 0, 1) '''
    
    if not pecas_iguais(obter_ganhador(tabuleiro), cria_peca(' ')) or \
       profundidade == 0:
        return peca_para_inteiro((obter_ganhador(tabuleiro))), \
               seq_movimentos
    
    else:
        pos_jogador = obter_posicoes_jogador(tabuleiro, cria_peca(jogador))
        
        # se estiver bloqueado, devolve um movimento do tipo (p1, p1)
        if esta_bloqueado(tabuleiro, jogador):
            return (peca_para_inteiro(jogador), \
                    ((pos_jogador[0], pos_jogador[0])),)
        
        melhor_resultado = -1 * peca_para_inteiro(cria_peca(jogador))
    
        for el in pos_jogador:
            pos_adjacentes = obter_posicoes_adjacentes(el)
        
            for pos in pos_adjacentes:
                if eh_posicao_livre(tabuleiro, pos):
                    novo_tab = cria_copia_tabuleiro(tabuleiro)
                    move_peca(novo_tab, el, pos)
                    
                    novo_resultado, nova_seq_movimentos = \
                        minimax(novo_tab, converte_para_peca \
                        (-1 * peca_para_inteiro(cria_peca(jogador))), \
                        profundidade - 1, seq_movimentos + ((el, pos),))
                    
                    if "melhor_seq_movimentos" not in locals() or \
                       (pecas_iguais(jogador, cria_peca('X')) and \
                       novo_resultado > melhor_resultado) or \
                       (pecas_iguais(jogador, cria_peca('O')) and \
                       novo_resultado < melhor_resultado):
                        melhor_resultado, melhor_seq_movimentos = \
                            novo_resultado, nova_seq_movimentos
                      
            
        return melhor_resultado, melhor_seq_movimentos

#-------------------------------------------------------------------------------

def ganho_bloqueio(t, val):
    # ganho_bloqueio: tabuleiro x inteiro -> tuplo de posicoes
    ''' recebe um tabuleiro de jogo e um inteiro correspondente a uma peca
    1 para 'X' ou -1 para 'O', e devolve um tuplo com a posicao que permite
    fazer a jogada de vitoria ou de bloqueio de vitoria '''
    for i in ('1', '2', '3', 'a', 'b', 'c'):
        soma = 0
        vetor = obter_vetor(t, i)
        for ii in range(3):
            soma += peca_para_inteiro(vetor[ii])
        if soma == 2 * val:
            for ii in range(3):
                if pecas_iguais(vetor[ii], cria_peca(' ')):
                    if i in ('1', '2', '3'):
                        return (cria_posicao(chr(ii + 97), i),) 
                    else:
                        return (cria_posicao(i, str(ii + 1)),)


def fase_colocacao(t, j):
    # fase_colocacao: tabuleiro x peca -> tuplo de posicoes
    ''' recebe um tabuleiro de jogo e uma peca e devolve um tuplo com a posicao
    para a qual o jogador que jogar com a peca j jogara a seguir '''
    val = peca_para_inteiro(j)
    
    # verifica se ha jogada de vitoria e retorna a posicao correspondente
    # em caso afirmativo
    
    res_vit = ganho_bloqueio(t, val)
    if res_vit != None:
        return res_vit
    
    # verifica se ha jogada de vitoria do oponente e retorna a posicao 
    # de bloqueio em caso afirmativo
    
    res_bloq = ganho_bloqueio(t, -val)
    if res_bloq != None:
        return res_bloq
    
    
    # verifica se posicao central esta livre e devolve a, em caso afirmativo
    elif eh_posicao_livre(t, cria_posicao('b', '2')):
        return (cria_posicao('b', '2'),)

    # verifica se existe um canto vazio e devolve o, em caso afirmativo
    for el in (cria_posicao('a', '1'), cria_posicao('c', '1'), \
               cria_posicao('a', '3'), cria_posicao('c', '3')):
        if eh_posicao_livre(t, el):
            return (el,)
        
    # verifica se existe um lateral vazio e devolve o, em caso afirmativo
    for el in (cria_posicao('b', '1'), cria_posicao('a', '2'), \
               cria_posicao('c', '2'), cria_posicao('b', '3')):
        if eh_posicao_livre(t, el):
            return (el,)     


def modo_facil(t, j):
    # modo_facil: tabuleiro x peca -> tuplo de posicoes
    ''' recebe um tabuleiro de jogo e uma peca e devolve um tuplo de posicoes
    relativo ao movimento a efetuar por parte do jogador que joga com a peca j.
    O primeiro elemento deste tuplo eh referente a posicao da peca a deslocar e
    o segundo elemento eh referente a posicao de destino dessa peca '''
    pos_computador = obter_posicoes_jogador(t, j)
    
    for pos in pos_computador:
        pos_adjacentes = obter_posicoes_adjacentes(pos)
        
        for el in pos_adjacentes:
            if eh_posicao_livre(t, el):
                return (posicao_para_str(pos), posicao_para_str(el))    



def fase_movimento(t, j, dificuldade):
    # fase_movimento: tabuleiro x peca x str -> tuplo de posicoes
    ''' recebe um tabuleiro de jogo, uma peca e uma cadeia de caracteres
    referente ao nivel de dificuldade do jogo e devolve um tuplo de posicoes
    que indica o movimento que o jogador que joga com a peca j efetuara '''
    if dificuldade == 'facil':
        # nivel de dificuldade facil 
        res_facil = modo_facil(t, j)
        if res_facil != None:
            return res_facil
                
    elif dificuldade == 'normal':
        # nivel de dificuldade normal
        val_tab, seq_movimentos = minimax(t, j, 1, ())
        novo_tab = cria_copia_tabuleiro(t)
        move_peca(novo_tab, seq_movimentos[0][0], seq_movimentos[0][1])
        if pecas_iguais(peca_para_inteiro(obter_ganhador(novo_tab)), j):
            return seq_movimentos
        else:
            # se nao obteve resultado em normal, tenta o facil
            res_facil = modo_facil(t, j)
            if res_facil != None:
                return res_facil
        
    else:
        # nivel de dificuldade dificil
        val_tab, seq_movimentos = minimax(t, j, 5, ())  
        return seq_movimentos[0]
      
#-------------------------- OBTER MOVIMENTO AUTO -------------------------------

def obter_movimento_auto(t, j, dificuldade):
    # obter_movimento_auto: tabuleiro x peca x string -> tuplo de posicoes
    ''' funcao auxiliar que recebe um tabuleiro, uma peca de um jogador e uma
    cadeia de caracteres representando o nivel de dificuldade do jogo, e devolve
    um tuplo com uma ou duas posicoes que representam uma posicao ou um 
    movimento escolhido automaticamente '''
    
    if len(obter_posicoes_livres(t)) > 3:
        # fase de colocacao
        return fase_colocacao(t, j)
    
    else:
        # fase de movimento
        return fase_movimento(t, j, dificuldade)
    
#-------------------------------- MOINHO ---------------------------------------

def moinho(peca_humano, nivel):
    # moinho: str x str -> str 
    ''' recebe duas cadeias de caracteres e devolve a representacao externa da
    peca ganhadora ('[X]' ou '[O]') '''
    
    # validacao dos argumentos
    if nivel in ('facil', 'normal', 'dificil') and \
       eh_peca(cria_peca(peca_humano[1:-1])):
        
        print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + \
              nivel + '.')
        t = cria_tabuleiro()
        print(tabuleiro_para_str(t))
        
        peca_hum = cria_peca(peca_humano[1:-1])
        val_peca_humano = peca_para_inteiro(peca_hum)
        peca_computador = converte_para_peca \
            (peca_para_inteiro(peca_hum) * -1)
        
        peca_livre, ronda = cria_peca(' '), 1
        
            
        # variavel que controla se estamos na fase de colocacao ou movimento
        colocacao = True
    
        while colocacao:
            # codigo respetivo a fase de colocacao
            
            if ronda == val_peca_humano:
                # humano a jogar
                coloca_peca(t, peca_hum, obter_movimento_manual(t, peca_hum)[0])
            else:
                # pc a jogar
                print('Turno do computador (' + nivel + '):')
                coloca_peca(t, peca_computador, \
                            obter_movimento_auto(t, peca_computador, nivel)[0])
            
            # print do tabuleiro de jogo
            print(tabuleiro_para_str(t))
            # verifica se existe vencedor
            if not pecas_iguais(cria_peca(obter_ganhador(t)), peca_livre):
                return peca_para_str(obter_ganhador(t))                
            # muda a ronda, fazendo com que seja o outro jogador a jogar
            ronda *= -1
            # verifica se ainda estamos na fase de colocacao
            if len(obter_posicoes_livres(t)) == 3:
                colocacao = False
        
        # codigo correspondente a fase de movimento
        while True:
            if ronda == val_peca_humano:
                # humano a jogar
                jog_humano = obter_movimento_manual(t, peca_humano)
                move_peca(t, jog_humano[0], jog_humano[1])
            else:
                # pc a jogar
                print('Turno do computador (' + nivel + '):')
                jog_computador = obter_movimento_auto(t, peca_computador, nivel)
                move_peca(t, jog_computador[0], jog_computador[1])
            
            # print do tabuleiro de jogo
            print(tabuleiro_para_str(t))
            # muda a ronda, fazendo com que seja o outro jogador a jogar
            ronda *= -1
            # verifica se existe ganhador
            if not pecas_iguais(obter_ganhador(t), peca_livre):
                return peca_para_str(cria_peca(obter_ganhador(t)))
    else:
        raise ValueError('moinho: argumentos invalidos')    