#################################################################
## AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
## DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
## TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
## DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
## DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
## OU PLÁGIO.
## DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
## DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
## SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
## DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
## DIVULGADOS NA PÁGINA DA DISCIPLINA.
## ENTENDO QUE EPS SEM ESTE CABEÇALHO NÃO SERÃO CORRIGIDOS E,
## AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.
## Nome : Renzo Real Machado Filho
## NUSP : 154.869.07
## Turma: BCC 2024
## Prof.: Roberto Hirata Jr.
## Referências: 
## - O algoritmo Insertion Sort Otimizado foi baseado em
## https://www.geeksforgeeks.org/insertion-sort/


from random import random
from random import randint
from sys import platform
import time as T
from matplotlib import pyplot as plt
from math import sqrt

# imports extras do trabalho #
import scipy
from scipy.interpolate import make_interp_spline
import numpy as np

# import do complemento do EP
import ctypes
libsort = ctypes.CDLL('C:/Users/renzo/Documents/programming/libRenzo.so')

libsort.selectionC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.bubbleC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.insertionC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.insertion_optC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.countingC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

def mediaT(T,n):

    """ Função que, dado uma lista `T` de tamanho `n`, calcula a média aritmética dos elementos desse vetor.
    Note que, justamente, temos como parâmetros tal vetor `V` e seu tamanho `n`. 
    Como saída, retornamos o valor calculado dessa média. """

    somador = 0
    for i in range(n):
        somador = somador + T[i]
    media = somador/n

    return media

def varT(T,n):

    """ Função que, dado um vetor `V` de tamanho 'n', calcula o desvio padrão dos elementos desse vetor.
    Note que, justamente, temos como parâmetros tal vetor `V` e seu tamanho `n`. 
    Lembre-se, o desvio padrão é obtido atráves do cálculo da raiz quadrada da variância dos elementos.
    Como saída, retornamos o valor calculado do desvio padrão. """

    somador = 0
    media = mediaT(T,n)
    for i in range(n):
        somador = somador + (T[i] - media)**2
    var = somador/(n-1)
    desvio = sqrt(var)

    return desvio

def selection(V, n):

    """ Função que, dado uma lista `V` de tamanho `n`, ordena os elementos desse vetor segundo o método selection sort.
    Note que temos como parâmetros tal vetor `V` e seu tamanho `n`. 
    Não há valores de saída. """ 

    for i in range(n):
        # iteração que percorrerá de 0 até o tamanho do Vetor fornecido, este primeiro loop fixará o elemento
        for j in range(i+1, n): 
            # essa segunda iteração terá a função de comparar o elemento fixado com os elementos seguintes do Vetor
            if(V[i] > V[j]):  
                # Verifica se o elemento da posição atual do Vetor é menor que o próximo elemento
                # nas próximas três linhas trocaremos de posição os elementos, se a condição anterior for satisfeita
                swap = V[i]     
                V[i] = V[j] 
                V[j] = swap

def bubble(V, n):
    
    """ Função que, dado uma lista `V` de tamanho `n`, ordena os elementos desse vetor segundo o método bubble sort.
    Note que temos como parâmetros tal vetor `V` e seu tamanho `n`. 
    Não há valores de saída. """

    houveTroca = False

    for i in range(1,n): # iteração que decrescerá a necessidade de verificação do Vetor, pois na linha seguinte terá: range(n-i)
        for j in range(n-i): 
            # essa iteração irá atuar percorrendo o Vetor, mas a cada iteração terá que Vericar uma posição a menos
            if (V[j] > V[j+1]): # semelhante ao anterior e troca de posição...
                swap = V[j+1]     
                V[j+1] = V[j] 
                V[j] = swap

                houveTroca = True
            
        if(not houveTroca): # melhor caso, o array já está ordenado
            break
    
def insertion(V, n):

    """ Função que, dado uma lista `V` de tamanho `n`, ordena os elementos desse vetor segundo o método insertion sort.
    Note que temos como parâmetros tal vetor `V` e seu tamanho `n`. 
    Não há valores de saída. """

    for i in range(1,n): # percorreremos o Vetor, note que a condição está na forma V[i] < V[i-1], por isso partiremos de 1
        
        if (V[i] < V[i-1]): # se encontrarmos um elemento fora de ordem, trocamos suas posições
            swap = V[i]     
            V[i] = V[i-1] 
            V[i-1] = swap
                        
            for j in range(1,i):   # uma iteração decrescente para voltarmos posições no Vetor e fazendo a mesma comparação
                                     
                if (V[i-j] < V[i-j-1]): # essa iteração decrescente permite corrigir elementos fora de ordem nas posições anteriores
                    swap = V[i-j]     
                    V[i-j] = V[i-j-1] 
                    V[i-j-1] = swap
                else:
                    break 

def insertion_opt(V, n):

    """ Versão otimizada do método de ordenação Insertion Sort.
    Temos como parâmetros um vetor `V` de tamanho `n`. Não há valores de saída. """

    for i in range(1, n):
        key = V[i]  # guarda o elemento que será inserido na posição correta
        j = i - 1  # índice do elemento anterior a posição V

        while j >= 0 and V[j] > key:  # move os elementos maiores para a direita
            V[j + 1] = V[j]
            j = j - 1

        # insere o elemento na posição correta
        V[j + 1] = key

def counting(V, n):
    
    """ Função que, dado uma lista `V` de tamanho `n`, ordena os elementos desse vetor segundo o método counting sort.
    !!! Estamos tratando apenas com números positivos !!!
    Note que temos como parâmetros tal vetor `V` e seu tamanho `n`. 
    Não há valores de saída. """
    
    max = V[0]   # esse primeiro loop busca o maior valor dentro do vetor fornecido
    for i in range(n-1): 
        if (max < V[i+1]):
            max = V[i+1]

    assistant = [0 for i in range(max+1)] # cria um vetor auxiliar/assistente 

    for j in range(n): # nesse terceiro loop, contamos as ocorrências dos valores de V e adicionamos no vetor auxiliar
        assistant[V[j]] = assistant[V[j]] + 1 
    
    V.clear() # limpamos o vetor original para ordená-lo a seguir

    for k in range(max+1): # nesses quarto e quinto loops, acessaremos o vetor auxiliar que, por sua vez, mostrará as ocorrências
        for l in range(assistant[k]): # dos elementos. Assim, adicionaremos no vetor original tais elementos de forma ordenada.
            V.append(k) 

def sortPY(V, n):
    
    """ Função que, dado uma lista `V` de tamanho `n`, ordena os elementos desse vetor utilizando o método nativo do PYTHON.
    Note que padronizamos seus parâmetros conforme as funções anteriores, com um vetor `V` e seu tamanho `n`. 
    Não há valores de saída. """ 

    V.sort()

### FUNÇÕES IMPORTADAS DO C ###

def selectionC(V,n):

    """ Função que importa o selection sort implementado em C. Note que temos como parâmetros uma lista `V` de tamanho `n`. Não há valores de saída. """

    pV = (ctypes.c_int *n)(*V)
    libsort.selectionC(pV,n)
    
    #for i in range(n):
    #    V[i] = pV[i]

def bubbleC(V,n):

    """ Função que importa o bubble sort implementado em C. Note que temos como parâmetros uma lista `V` de tamanho `n`. Não há valores de saída. """

    pV = (ctypes.c_int *n)(*V)
    libsort.bubbleC(pV,n)
    
    #for i in range(n):
    #    V[i] = pV[i]
    
def insertionC(V,n):

    """ Função que importa o insertion sort implementado em C. Note que temos como parâmetros uma lista `V` de tamanho `n`. Não há valores de saída. """

    pV = (ctypes.c_int *n)(*V)
    libsort.insertionC(pV,n)
    
    #for i in range(n):
    #    V[i] = pV[i]

def insertion_optC(V,n):

    """ Função que importa o insertion sort otimizado implementado em C. Note que temos como parâmetros uma lista `V` de tamanho `n`. Não há valores de saída. """

    pV = (ctypes.c_int *n)(*V)
    libsort.insertion_optC(pV,n)
    
    #for i in range(n):
    #    V[i] = pV[i]

def countingC(V,n):

    """ Função que importa o counting sort implementado em C. Note que temos como parâmetros uma lista `V` de tamanho `n`. Não há valores de saída. """

    pV = (ctypes.c_int *n)(*V)
    libsort.countingC(pV,n)

    #for i in range(n):
    #    V[i] = pV[i]

################################

def embaralha(V,n,p):

    """ Função que, dado uma lista `V` de tamanho `n`, embaralha p% dos elementos dessa lista.
    Note que, justamente, temos como parâmetros tal lista `V`, seu tamanho `n` e a porcentagem `p`. 
    Não há valores de saída.
    """

    changes = ((p*n))//100 # transformamos o valor `p`, dado em %, em seu representante inteiro
    
    for i in range(changes): # permutamos posições aleatórias dentro do vetor
        random_num = randint(0, n-1) # OBS: optei por fazer mais iterações, para garantir um 'embaralhamento' mais eficaz
        random_num2 = randint(0, n-1) # anteriormente estava na forma: 'for i in range(changes//2)'

        swap = V[random_num]
        V[random_num] = V[random_num2]
        V[random_num2] = swap

def timeMe(func,V,n,m,p):

    """ Função que calcula o tempo médio gasto de execução de um algoritmo de ordenação, assim como sua variância.
    Assim, temos como parâmetros uma função `func`, uma lista `V` de tamanho `n`, uma valor `p` que indica a porcentagem que tal lista `V` será embaralhada por um número `m` de vezes. 
    Como saída, retornamos uma lista contendo a média e a variância do tempo de execução da função de entrada. """

    armazena = []
    Vsorted = V.copy()

    for i in range(m): # vamos iterar a execução da função de entrada um número 'm' de vezes:

        
        embaralha(Vsorted, n, p)  # embaralha o vetor e posteriormente calcula o tempo gasto de execução da função de entrada:

        start = T.process_time()
        func(Vsorted,n)
        finish = T.process_time()
        timeSpent = finish - start

        Vsorted = V.copy()

        #with open('statistics_EP0110.txt', 'a') as st:
           # txt = 'O tempo gasto de ' + str(func) + ' foi: ' + str(timeSpent) + " --- tamanho do vetor: " + str(len(V)) + "\n"
            #st.write(txt)
            

        armazena.append(timeSpent) # armazena o tempo gasto

    media = mediaT(armazena, m) # calcula a média do tempo de execução da função de entrada 
    variancia = varT(armazena, m) # calcula a variância amostral do tempo de execução da função de entrada 

    print("A media de ",func, "foi: ", media, variancia)
    
    return media, variancia # retorna uma lista com indices 'media' e 'variancia'

def GraficaSortings(mpontos, mediaMCMPi, desvioMCMPi):

    """ Função que utiliza a biblioteca `matplotlib` para gerar um gráfico do tipo `errorbar` em que o eixo x corresponde a algum dado interpretado pelo usuário e o eixo y corresponde ao tempo médio de execução de um algoritmo de ordenação, com uma taxa de desvio em relação ao tempo médio. Assim, temos como parâmetros três listas: `mpontos`, `mediaMCMPi` e `desvioMCMPi`.
    Não há valores saída.
    """

    plt.errorbar(mpontos,mediaMCMPi,yerr=desvioMCMPi, fmt='o')
   
def GraficaSortings_opt(mpontos, mediaMCMPi):
    """ Função que utiliza a biblioteca `matplotlib` para gerar um plot padrão em que o eixo x corresponde a algum dado interpretado pelo usuário e o eixo y corresponde ao tempo médio de execução de um algoritmo de ordenação. Assim, temos como parâmetros três listas: `mpontos` e `mediaMCMPi`. 
    Não há valores saída. """
    plt.plot(mpontos, mediaMCMPi)

def GraficaSortings_opt_curve(mpontos, mediaMCMPi):
    
    """ Função que utiliza as bibliotecas `matplotlib`, `scipy` e `numpy` para aproximar um gráfico curvilíneo.
    Nesse gráfico, o eixo x corresponde a algum dado interpretado pelo usuário e o eixo y corresponde ao tempo médio de execução de um algoritmo de ordenação. Assim, temos como parâmetros três listas: `mpontos`, `mediaMCMPi` e `desvioMCMPi`.
    Não há valores saída. """


    x = np.array(mpontos)
    y = np.array(mediaMCMPi)
  
    curve = make_interp_spline(x, y)
    
    x_ = np.linspace(x.min(), x.max(), 500)
    y_ = curve(x_)
    
    plt.plot(x_, y_)

def generate_vector(n):
    
    """ Função que cria um vetor de tamanho `n`.
    Note que temos como paramêtros um inteiro `n` que indica o tamanho do vetor.
    Retornamos o vetor criado como saída. """

    V = [randint(0,9999) for i in range(n)] 
    
    return V

def generate_vector_opt(interv, n):

    """ Função que cria um vetor de tamanho `n` dentro de um intervalo fornecido pelo usuário.
    Note que temos como paramêtros dois inteiros, um `n` que indica o tamanho do vetor e outro `interv` que indica o limite superior do intervalo.
    Retornamos o vetor criado como saída. """

    V = [randint(0,interv) for i in range(n)] 
    
    return V

def isEqual(V1, V2, n): 

    """ Função que verifica se duas listas possuem elementos iguais.
    Note que temos como parâmetros duas listas, `V1` e `V2` e um inteiro `n` que indica o tamanho das listas. 
    Como saída, retornamos `True` se as listas fornecidas são iguais e `False`, caso contrário. """

    for i in range(n):
        if(V1[i] != V2[i]):
            return False
    
    return True

def main():

    """ Função principal que executa o experimento conforme as diretrizes do EP1 de MAC0110.
    Não há parâmetros e nem mesmo saída. """
    
    ###########################################################################
    ############################ P A R T E   1 ################################
    ###########################################################################

    tamanhoV = [1000, 5000, 10000, 50000, 100000]
    funcs = [selection, bubble, insertion_opt, counting, sortPY] 
    statistics = [] # Trata-se de uma lista de listas, armazenando as médias e o desvio padrão dos algoritmos 

    for i in range(len(tamanhoV)): # executa o programa de acordo com as posições pedidas: 1000, 5000, 10000, 50000, 100000
        
        V = generate_vector(tamanhoV[i]) # cria uma lista desordenado de tamanho correspondente a lista tamanhoV
        Vsorted = V.copy()
      
        for j in range(len(funcs)): # chama os quatro algoritmos de ordenação estudados: selection, bubble, insertion, counting
        
            statistics.append(timeMe(funcs[j], Vsorted, len(Vsorted), 10, 0))  
            Vsorted = V.copy()

    # A seguir iteramos a lista de listas para isolar as médias e as variâncias de cada algoritmo estudado

    mediaSelection = [statistics[i][0] for i in range(0, len(statistics), len(funcs))]
    varSelection = [statistics[i][1] for i in range(0, len(statistics), len(funcs))]

    mediaBubble = [statistics[i][0] for i in range(1, len(statistics), len(funcs))]
    varBubble = [statistics[i][1] for i in range(1, len(statistics), len(funcs))]

    mediaInsertion = [statistics[i][0] for i in range(2, len(statistics), len(funcs))]
    varInsertion = [statistics[i][1] for i in range(2, len(statistics), len(funcs))]

    mediaCounting = [statistics[i][0] for i in range(3, len(statistics), len(funcs))]
    varCounting = [statistics[i][1] for i in range(3, len(statistics), len(funcs))]

    mediaPY = [statistics[i][0] for i in range(4, len(statistics), len(funcs))]
    varPY = [statistics[i][1] for i in range(4, len(statistics), len(funcs))]

    ########################### G R Á F I C O S ###############################

    legendas = ['Selection', 'Bubble', 'Insertion Otimizado', 'Counting', 'Sort PYTHON'] #'Selection', 'Bubble', 'Insertion Otimizado',
    

    GraficaSortings(tamanhoV, mediaSelection, varSelection)
    GraficaSortings(tamanhoV, mediaBubble, varBubble)       
    GraficaSortings(tamanhoV, mediaInsertion, varInsertion)
    GraficaSortings(tamanhoV, mediaCounting, varCounting)
    GraficaSortings(tamanhoV, mediaPY, varPY)

    #plt.figure()
    plt.legend(legendas, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/parte1')
    #plt.show()

    ###########################################################################
    ############################ P A R T E   2 ################################
    ###########################################################################
    
    porcentagens = [1, 3, 5, 10, 25, 50]
    funcs2 = [bubble, insertion_opt, sortPY]
    tamanhoFixo = 100000
    statistics2 = []

    V2 = [i for i in range(tamanhoFixo)]
    
    for i in range(len(porcentagens)):
        
        for j in range(len(funcs2)):
        
            statistics2.append(timeMe(funcs2[j], V2, len(V2), 10, porcentagens[i]))

    mediaBubble2 = [statistics2[i][0] for i in range(0, len(statistics2), len(funcs2))]
    varBubble2 = [statistics2[i][1] for i in range(0, len(statistics2), len(funcs2))]

    mediaInsertion2 = [statistics2[i][0] for i in range(1, len(statistics2), len(funcs2))]
    varInsertion2 = [statistics2[i][1] for i in range(1, len(statistics2), len(funcs2))]

    mediaPY2 = [statistics2[i][0] for i in range(2, len(statistics2), len(funcs2))]
    varPY2 = [statistics2[i][1] for i in range(2, len(statistics2), len(funcs2))]

    ########################### G R Á F I C O S ###############################

    legendas2 = ['Bubble', 'Insertion Otimizado', 'Sort PYTHON'] 
    plt.clf()

    GraficaSortings(porcentagens, mediaBubble2, varBubble2)
    GraficaSortings(porcentagens, mediaInsertion2, varInsertion2)
    GraficaSortings(porcentagens, mediaPY2, varPY2)
    
    plt.legend(legendas2, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Porcentagem de desordem (%)')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/parte2')
    #plt.show()

def comparativoInsertion():

    """ Função que executa o experimento comparativo entre duas versões do algoritmo `insertion sort`.
    Não há parâmetros e nem mesmo saída. """

    ###########################################################################
    ############################ P A R T E   1 ################################
    ###########################################################################
    
    tamanhoV = [1000, 5000, 10000, 50000, 100000]
    funcs = [insertion, insertion_opt] 
    statistics = [] # Trata-se de uma lista de listas, armazenando as médias e o desvio padrão dos algoritmos 

    for i in range(len(tamanhoV)): # executa o programa de acordo com as posições pedidas: 1000, 5000, 10000, 50000, 100000
        
        V = generate_vector(tamanhoV[i]) # cria uma lista desordenado de tamanho correspondente a lista tamanhoV
        Vsorted = V.copy()

        for j in range(len(funcs)): # chama os quatro algoritmos de ordenação estudados: selection, bubble, insertion, counting
        
            statistics.append(timeMe(funcs[j], Vsorted, len(Vsorted), 10, 0))  
            Vsorted = V.copy()


    mediaInsertion = [statistics[i][0] for i in range(0, len(statistics), len(funcs))]
    varInsertion = [statistics[i][1] for i in range(0, len(statistics), len(funcs))]

    mediaOtimizado = [statistics[i][0] for i in range(1, len(statistics), len(funcs))]
    varOtimizado = [statistics[i][1] for i in range(1, len(statistics), len(funcs))]

    ########################### G R Á F I C O S ###############################

    legendas = ['Insertion', 'Insertion Otimizado'] 
     
    GraficaSortings_opt_curve(tamanhoV, mediaInsertion)
    GraficaSortings_opt_curve(tamanhoV, mediaOtimizado)   
    
    #plt.figure()
    plt.legend(legendas, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/compInsert')
    #plt.show()
    
    ###########################################################################
    ############################ P A R T E   2 ################################
    ###########################################################################

    porcentagens = [1, 3, 5, 10, 25, 50]
    funcs2 = [insertion, insertion_opt]
    tamanhoFixo = 100000
    statistics2 = []

    V2 = [i for i in range(tamanhoFixo)]
    
    for i in range(len(porcentagens)):
        
        for j in range(len(funcs2)):
        
            statistics2.append(timeMe(funcs2[j], V2, len(V2), 10, porcentagens[i]))

    mediaInsertion2 = [statistics2[i][0] for i in range(0, len(statistics2), len(funcs2))]
    varInsertion2 = [statistics2[i][1] for i in range(0, len(statistics2), len(funcs2))]

    mediaOtimizado2 = [statistics2[i][0] for i in range(1, len(statistics2), len(funcs2))]
    varOtimizado2 = [statistics2[i][1] for i in range(1, len(statistics2), len(funcs2))]

    ########################### G R Á F I C O S ###############################

    legendas2 = ['Insertion', 'Insertion Otimizado']

    plt.clf()

    GraficaSortings_opt_curve(porcentagens, mediaInsertion2)
    GraficaSortings_opt_curve(porcentagens, mediaOtimizado2)

    plt.legend(legendas2, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Porcentagem de desordem (%)')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/compInsertcurve%')
    #plt.show()

    plt.clf()

    GraficaSortings_opt(porcentagens, mediaInsertion2)
    GraficaSortings_opt(porcentagens, mediaOtimizado2)

    plt.legend(legendas2, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Porcentagem de desordem (%)')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/compInsert%')
    #plt.show()

def Counting_X_PYsort():

    """ Função principal que executa o experimento comparativo entre o Counting Sort e o Timsort.
    Não há parâmetros e nem mesmo saída. """
    
    ###########################################################################
    ############################ P A R T E   1 ################################
    ###########################################################################

    tamanhoV = [1000, 2500, 5000, 10000, 25000, 50000, 75000, 100000]
    funcs = [counting, sortPY] 
    statistics = [] # Trata-se de uma lista de listas, armazenando as médias e o desvio padrão dos algoritmos 

    for i in range(len(tamanhoV)): # executa o programa de acordo com as posições pedidas: 1000, 5000, 10000, 50000, 100000
        
        V = generate_vector(tamanhoV[i]) # cria uma lista desordenado de tamanho correspondente a lista tamanhoV
        Vsorted = V.copy()
        #NewSorted = V.copy()

        for j in range(len(funcs)): # chama os quatro algoritmos de ordenação estudados: selection, bubble, insertion, counting
        
            statistics.append(timeMe(funcs[j], Vsorted, len(Vsorted), 200, 0))  
            Vsorted = V.copy()
   

    mediaCounting = [statistics[i][0] for i in range(0, len(statistics), len(funcs))]
    varCounting = [statistics[i][1] for i in range(0, len(statistics), len(funcs))]

    mediaPY = [statistics[i][0] for i in range(1, len(statistics), len(funcs))]
    varPY = [statistics[i][1] for i in range(1, len(statistics), len(funcs))]

    ########################### G R Á F I C O S ###############################

    legendas = ['Counting', 'Sort PYTHON'] 

    GraficaSortings(tamanhoV, mediaCounting, varCounting)
    GraficaSortings(tamanhoV, mediaPY, varPY)

    plt.legend(legendas, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/CxPY')
    #plt.show()

    plt.clf()
    GraficaSortings_opt(tamanhoV, mediaCounting)
    GraficaSortings_opt(tamanhoV, mediaPY)

    plt.legend(legendas, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/CxPY_2') 
    #plt.show()

def performanceCounting():

    """ Função que executa o experimento principal, mas, dessa vez, o comparativo varia o intervalo do gerador randint.
    Espera-se analisar como o tamanho máximo do intervalo influencia o comportamento do algoritmo Counting sort.
    Não há parâmetros e nem mesmo saída. """
    
    ###########################################################################
    ############################ P A R T E   1 ################################
    ###########################################################################

    tamanhoFixo = 1000
    funcs = [selection, bubble, insertion_opt, counting, sortPY] 
    intervaloV = [9999, 55555, 99999, 200000, 300000, 350000, 400000, 500000] #, 9999999, 55555555, 99999999] #99999999
    statistics = [] # Trata-se de uma lista de listas, armazenando as médias e o desvio padrão dos algoritmos 

    for i in range(len(intervaloV)): # executa o programa de acordo com as posições pedidas: 1000, 5000, 10000, 50000, 100000
        
        V = generate_vector_opt(intervaloV[i], tamanhoFixo) # cria uma lista desordenado de tamanho correspondente a lista tamanhoV
        Vsorted = V.copy()
        #NewSorted = V.copy()

        for j in range(len(funcs)): # chama os quatro algoritmos de ordenação estudados: selection, bubble, insertion, counting
        
            statistics.append(timeMe(funcs[j], Vsorted, len(Vsorted), 50, 0))  
            Vsorted = V.copy()


    mediaSelection = [statistics[i][0] for i in range(0, len(statistics), len(funcs))]
    varSelection = [statistics[i][1] for i in range(0, len(statistics), len(funcs))]

    mediaBubble = [statistics[i][0] for i in range(1, len(statistics), len(funcs))]
    varBubble = [statistics[i][1] for i in range(1, len(statistics), len(funcs))]

    mediaInsertion = [statistics[i][0] for i in range(2, len(statistics), len(funcs))]
    varInsertion = [statistics[i][1] for i in range(2, len(statistics), len(funcs))]

    mediaCounting = [statistics[i][0] for i in range(3, len(statistics), len(funcs))]
    varCounting = [statistics[i][1] for i in range(3, len(statistics), len(funcs))]

    mediaPY = [statistics[i][0] for i in range(4, len(statistics), len(funcs))]
    varPY = [statistics[i][1] for i in range(4, len(statistics), len(funcs))]

    ########################### G R Á F I C O S ###############################

    legendas = ['Selection', 'Bubble', 'Insertion Otimizado', 'Counting', 'Sort PYTHON']
    

    GraficaSortings(intervaloV, mediaSelection, varSelection)
    GraficaSortings(intervaloV, mediaBubble, varBubble)       
    GraficaSortings(intervaloV, mediaInsertion, varInsertion)
    GraficaSortings(intervaloV, mediaCounting, varCounting)
    GraficaSortings(intervaloV, mediaPY, varPY)


    plt.legend(legendas, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Tamanho do Intervalo')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/performCount')
    #plt.show()

    plt.clf()

    GraficaSortings_opt_curve(intervaloV, mediaCounting)

    #plt.legend(a, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação - Counting Sort') 
    plt.xlabel('Tamanho do Intervalo')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/performCount2')
    #plt.show()

def performanceIndividual():
    
    """ Função que executa o experimento, mas, dessa vez, produz gráficos únicos para cada algoritmo.
    Não há parâmetros e nem mesmo saída. """
    
    ###########################################################################
    ############################ P A R T E   1 ################################
    ###########################################################################

    tamanhoV = [1000, 5000, 10000, 25000, 50000]
    funcs = [selection, bubble, insertion_opt, counting, sortPY]
    statistics = [] # Trata-se de uma lista de listas, armazenando as médias e o desvio padrão dos algoritmos 

    for i in range(len(tamanhoV)): # executa o programa de acordo com as posições pedidas: 1000, 5000, 10000, 50000, 100000
        
        V = generate_vector(tamanhoV[i]) # cria uma lista desordenado de tamanho correspondente a lista tamanhoV
        Vsorted = V.copy()

        for j in range(len(funcs)): # chama os quatro algoritmos de ordenação estudados: selection, bubble, insertion, counting
        
            statistics.append(timeMe(funcs[j], Vsorted, len(Vsorted), 15, 0))  
            Vsorted = V.copy()


    mediaSelection = [statistics[i][0] for i in range(0, len(statistics), len(funcs))]
    varSelection = [statistics[i][1] for i in range(0, len(statistics), len(funcs))]

    mediaBubble = [statistics[i][0] for i in range(1, len(statistics), len(funcs))]
    varBubble = [statistics[i][1] for i in range(1, len(statistics), len(funcs))]

    mediaInsertion = [statistics[i][0] for i in range(2, len(statistics), len(funcs))]
    varInsertion = [statistics[i][1] for i in range(2, len(statistics), len(funcs))]
    
    mediaCounting = [statistics[i][0] for i in range(3, len(statistics), len(funcs))]
    varCounting = [statistics[i][1] for i in range(3, len(statistics), len(funcs))]
    
    mediaPY = [statistics[i][0] for i in range(4, len(statistics), len(funcs))]
    varPY = [statistics[i][1] for i in range(4, len(statistics), len(funcs))]
    
    medias = [mediaSelection, mediaBubble, mediaInsertion, mediaCounting, mediaPY]
    var = [varSelection, varBubble, varInsertion, varCounting, varPY]

    ########################### G R Á F I C O S ###############################

    titulos = ['Selection', 'Bubble', 'Insertion Otimizado', 'Counting', 'Sort PYTHON']
    
    for i in range(len(medias)):

        if i > 2:
            GraficaSortings_opt(tamanhoV, medias[i])
        else:    
            GraficaSortings_opt_curve(tamanhoV, medias[i])

        plt.title('Algoritmos de Ordenação - ' + titulos[i])
        plt.xlabel('Tamanho da lista')
        plt.ylabel('Tempo médio (s)')
        plt.savefig('/Users/renzo/Documents/indiv' + titulos[i])
        #plt.show()
        plt.clf()

        GraficaSortings(tamanhoV, medias[i], var[i])
        plt.title('Algoritmos de Ordenação - ' + titulos[i])
        plt.xlabel('Tamanho da lista')
        plt.ylabel('Tempo médio (s)')
        plt.savefig('/Users/renzo/Documents/indivErrBar' + titulos[i])
        #plt.show()
        plt.clf()

def performancePYsort():

    """ Função principal que executa o experimento conforme as diretrizes do EP1 de MAC0110.
    Não há parâmetros e nem mesmo saída. """
    
    ###########################################################################
    ############################ P A R T E   1 ################################
    ###########################################################################

    tamanhoV = [500000, 1000000, 10000000, 20000000, 25000000, 40000000, 50000000]
    funcs = [sortPY] 
    statistics = [] # Trata-se de uma lista de listas, armazenando as médias e o desvio padrão dos algoritmos 

    for i in range(len(tamanhoV)): # executa o programa de acordo com as posições pedidas: 1000, 5000, 10000, 50000, 100000
        
        V = generate_vector_opt(999999,tamanhoV[i]) # cria uma lista desordenado de tamanho correspondente a lista tamanhoV
        Vsorted = V.copy()

        for j in range(len(funcs)): # chama os quatro algoritmos de ordenação estudados: selection, bubble, insertion, counting
        
            statistics.append(timeMe(funcs[j], Vsorted, len(Vsorted), 10, 0))  
            Vsorted = V.copy()


    mediaPY = [statistics[i][0] for i in range(0, len(statistics), len(funcs))]
    varPY = [statistics[i][1] for i in range(0, len(statistics), len(funcs))]

    ########################### G R Á F I C O S ###############################

    legendas = ['Sort PYTHON'] 

    GraficaSortings(tamanhoV, mediaPY, varPY)

    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/PY')
    #plt.show()

    plt.clf()

    GraficaSortings_opt(tamanhoV, mediaPY)

    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/PY_2') 
    #plt.show()

##### C O M P L E M E N T O   D O   E P #####

def complementoEP():

    """ Função principal que executa a segunda parte do experimento, ou complemento do EP.
    Não há parâmetros e nem mesmo saída. """

    tamanhoV = [1000, 5000, 10000, 50000, 100000]
    funcs = [selectionC, bubbleC, insertion_optC, countingC, counting, sortPY] 
    statistics = [] # Trata-se de uma lista de listas, armazenando as médias e o desvio padrão dos algoritmos 

    for i in range(len(tamanhoV)): # executa o programa de acordo com as posições pedidas: 1000, 5000, 10000, 50000, 100000
        
        V = generate_vector(tamanhoV[i]) # cria uma lista desordenado de tamanho correspondente a lista tamanhoV
        Vsorted = V.copy()
      
        for j in range(len(funcs)): # chama os algoritmos de ordenação estudados: selection, bubble, insertion, counting
        
            statistics.append(timeMe(funcs[j], Vsorted, len(Vsorted), 10, 0))  
            Vsorted = V.copy()

    # A seguir iteramos a lista de listas para isolar as médias e as variâncias de cada algoritmo estudado

    mediaSelectionC = [statistics[i][0] for i in range(0, len(statistics), len(funcs))]
    varSelectionC = [statistics[i][1] for i in range(0, len(statistics), len(funcs))]

    mediaBubbleC = [statistics[i][0] for i in range(1, len(statistics), len(funcs))]
    varBubbleC = [statistics[i][1] for i in range(1, len(statistics), len(funcs))]

    mediaInsertionC = [statistics[i][0] for i in range(2, len(statistics), len(funcs))]
    varInsertionC = [statistics[i][1] for i in range(2, len(statistics), len(funcs))]

    mediaCountingC = [statistics[i][0] for i in range(3, len(statistics), len(funcs))]
    varCountingC = [statistics[i][1] for i in range(3, len(statistics), len(funcs))]

    mediaCounting = [statistics[i][0] for i in range(4, len(statistics), len(funcs))]
    varCounting = [statistics[i][1] for i in range(4, len(statistics), len(funcs))]

    mediaPY = [statistics[i][0] for i in range(5, len(statistics), len(funcs))]
    varPY = [statistics[i][1] for i in range(5, len(statistics), len(funcs))]

    ########################### G R Á F I C O S ###############################

    legendas = ['SelectionC', 'BubbleC', 'Insertion Otimizado C', 'CountingC ', 'Counting', 'Sort PYTHON'] #'Selection', 'Bubble', 'Insertion Otimizado',
    

    GraficaSortings(tamanhoV, mediaSelectionC, varSelectionC)
    GraficaSortings(tamanhoV, mediaBubbleC, varBubbleC)       
    GraficaSortings(tamanhoV, mediaInsertionC, varInsertionC)
    GraficaSortings(tamanhoV, mediaCountingC, varCountingC)
    GraficaSortings(tamanhoV, mediaCounting, varCounting)
    GraficaSortings(tamanhoV, mediaPY, varPY)

    #plt.figure()
    plt.legend(legendas, loc='upper left', fontsize='7')
    plt.title('Algoritmos de Ordenação') 
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo médio (s)')
    plt.savefig('/Users/renzo/Documents/complemento')
    #plt.show()

###########################################################################
############### E X E C U Ç Ã O   D A S   F U N Ç Õ E S ###################
###########################################################################

#main()
#comparativoInsertion()
#Counting_X_PYsort()
#performanceCounting()
#performanceIndividual()
#performancePYsort()
complementoEP()

############################  F  I  M  ####################################