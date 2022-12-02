import numpy as np
import sys
import math



tamanho_matrix = math.sqrt()

matrix_chave = [[0] * tamanho_matrix for i in range(tamanho_matrix)]
 
vetor_mensagem = [[0] for i in range(tamanho_matrix)]
 
matrix_cifra = [[0] for i in range(tamanho_matrix)]
 

def getmatrix_chave(key):
    k = 0
    for i in range(tamanho_matrix):
        for j in range(tamanho_matrix):
            matrix_chave[i][j] = ord(key[k]) % 65
            k += 1
 
# Função que encripta a mensagem
def encriptar(vetor_mensagem):
    for i in range(tamanho_matrix):
        for j in range(1):
            matrix_cifra[i][j] = 0
            for x in range(tamanho_matrix):
                matrix_cifra[i][j] += (matrix_chave[i][x] *
                                       vetor_mensagem[x][j])
            matrix_cifra[i][j] = matrix_cifra[i][j] % 26
 

def HillCipher(message, key):

    getmatrix_chave(key)
 
    for i in range(tamanho_matrix):
        vetor_mensagem[i][0] = ord(message[i]) % 65
 
    encriptar(vetor_mensagem)
 
    mensagem_codificada = []
    for i in range(tamanho_matrix):
        mensagem_codificada.append(chr(matrix_cifra[i][0] + 65))
 
    print("Mensagem codificada: ", "".join(mensagem_codificada))

if len(sys.argv) == 4:
    arquivo = sys.argv[1]
    chave = sys.argv[2]
    acao = sys.argv[3]

    if arquivo[len(arquivo) - 4] != '.txt':
        
        print('Por favor, adicione um arquivo de texto(.txt)')
    
    elif not math.sqrt(chave.len()).is_integer() :

        print('Por favor, adicione uma matrix quadrada inversivel(Com o determinante diferente de 0)')

else:

    print('Falta parametros na chamada do script')
    print('Sintaxe correta: $<script> <arquivo.txt> <chave> <CRIPTO ou DECRIPTO>')
    sys.exit()

 