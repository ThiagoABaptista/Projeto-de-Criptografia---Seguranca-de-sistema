import numpy as np
import sys
import math

def getunicode(vetor_mensagem):
    k = 0
    mensagem_unicode = [0] * (len(vetor_mensagem))
    for i in range(len(vetor_mensagem)):
            mensagem_unicode[i] = ord(vetor_mensagem[i])
            k += 1
    return mensagem_unicode
 
# Função que encripta a mensagem
def encriptar(vetor_mensagem, chave):
    mensagem_unicode = getunicode(vetor_mensagem)
    texto_codificado = ""
    for i in range(len(mensagem_unicode)):
        print(mensagem_unicode[i])
        mensagem_unicode[i] = (mensagem_unicode[i] + int(chave))
        print(mensagem_unicode[i])
        if(mensagem_unicode[i] > 127):
           mensagem_unicode[i] = mensagem_unicode[i] % 127
        texto_codificado += chr(mensagem_unicode[i])
    return texto_codificado    

def desencriptar(vetor_mensagem, chave):
    mensagem_unicode = getunicode(vetor_mensagem)
    texto_codificado = ""
    for i in range(len(mensagem_unicode)):
        print(mensagem_unicode[i])
        mensagem_unicode[i] = mensagem_unicode[i] - int(chave)
        if(mensagem_unicode[i] < 0):
            mensagem_unicode[i] = 127 + (mensagem_unicode[i])
        texto_codificado += chr(mensagem_unicode[i])
    return texto_codificado  

# Chamada principal
if len(sys.argv) == 4:
    arquivo = sys.argv[1]
    chave = sys.argv[2]
    acao = sys.argv[3]

    # Validação dos Argumentos
    if arquivo[len(arquivo) - 4:] != '.txt':
        
        print('Por favor, adicione um arquivo de texto(.txt)')
    
    elif not float(chave).is_integer() :

        print('Por favor, adicione numero inteiro como chave')
    
    elif acao != 'criptografar' and acao != 'descriptografar':

        print('Por favor, o ultimo parametro deve ser criptografar ou descriptografar')

    else:
        # Abertura do Arquivo
        arquivo_texto = open(arquivo)
        mensagem = arquivo_texto.read()
        arquivo_texto.close()
        if acao == 'criptografar':
            texto_codificado = encriptar(mensagem,chave)
            texto_arquivo_opcao = '_cripto'
        else:
            texto_codificado = desencriptar(mensagem,chave)
            print(texto_codificado)
            texto_arquivo_opcao = '_descripto'
        arquivo_novo = arquivo[:len(arquivo) - 4] + texto_arquivo_opcao + '.txt'
        arquivo_codificado = open(arquivo_novo,'w+')
        arquivo_codificado.write(texto_codificado)
        arquivo_codificado.close()
else:
    print('Falta parametros na chamada do script')
    print('Sintaxe correta: $<script> <arquivo.txt> <chave> <criptografar ou descriptografar>')
    sys.exit()

 