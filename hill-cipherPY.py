import numpy as np
import sys
import math

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

def desencriptar(vetor_mensagem):
    matrix_invertida = np.linalg.inv(matrix_chave)
    #matrix_cifra = matrix_invertida@vetor_mensagem % 26
    for i in range(tamanho_matrix):
        for j in range(1):
            matrix_cifra[i][j] = 0
            for x in range(tamanho_matrix):
                matrix_cifra[i][j] += (matrix_invertida[i][x] * vetor_mensagem[x][j])
            matrix_cifra[i][j] = int(matrix_cifra[i][j] % 26)
            print(matrix_cifra[i][j])
    
def HillCipherEncriptar(mensagem, key):

    getmatrix_chave(key)
 
    for i in range(tamanho_matrix):
        vetor_mensagem[i][0] = ord(mensagem[i]) 
    encriptar(vetor_mensagem)
    mensagem_codificada = []
    for i in range(tamanho_matrix):
        mensagem_codificada.append(chr(matrix_cifra[i][0] + 65))
    
    print("Mensagem codificada: ", "".join(mensagem_codificada))
    return "".join(mensagem_codificada)
def HillCipherDesencriptar(mensagem, key):

    getmatrix_chave(key)
    
    for i in range(tamanho_matrix):
        vetor_mensagem[i][0] = ord(mensagem[i]) % 65
    desencriptar(vetor_mensagem)
    mensagem_codificada = []
    for i in range(tamanho_matrix):
        mensagem_codificada.append(chr(matrix_cifra[i][0] + 65))
    
    print("Mensagem codificada: ", "".join(mensagem_codificada))
    return "".join(mensagem_codificada)

if len(sys.argv) == 4:
    arquivo = sys.argv[1]
    chave = sys.argv[2]
    acao = sys.argv[3]

    if arquivo[len(arquivo) - 4:] != '.txt':
        
        print('Por favor, adicione um arquivo de texto(.txt)')
    
    elif not math.sqrt(len(chave)).is_integer() :

        print('Por favor, adicione uma matrix quadrada inversivel(Com o determinante diferente de 0)')
    
    elif acao != 'criptografar' and acao != 'descriptografar':

        print('Por favor, o ultimo parametro deve ser criptografar ou descriptografar')

    else:
        tamanho_matrix = int(math.sqrt(len(chave)))
        matrix_chave = [[0] * tamanho_matrix for i in range(tamanho_matrix)]
        vetor_mensagem = [[0] for i in range(tamanho_matrix)]
        matrix_cifra = [[0] for i in range(tamanho_matrix)]
        arquivo_texto = open(arquivo)
        mensagem = arquivo_texto.read()
        arquivo_texto.close()
        if acao == 'criptografar':
            texto_codificado = HillCipherEncriptar(mensagem,chave)
            arquivo_novo = arquivo[:len(arquivo) - 4] + '_cripto.txt'
            arquivo_codificado = open(arquivo_novo,'w+')
            arquivo_codificado.write(texto_codificado)
            arquivo_codificado.close()
        else:
            texto_codificado = HillCipherdesencriptar(mensagem,chave)
            print(texto_codificado)
else:
    print('Falta parametros na chamada do script')
    print('Sintaxe correta: $<script> <arquivo.txt> <chave> <criptografar ou descriptografar>')
    sys.exit()

 