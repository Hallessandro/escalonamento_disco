#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fcfs import *
from sstf import *
from elevador import *
import copy

# funcao principal
def main():
    arquivo = open("entrada.txt")
    conteudo = []
    for line in arquivo:
        conteudo.append(int(line))
    # Le o numero do ultimo cilindro do disco
    ultimo_cilindro = int(conteudo[0])

    # Le a posicao inicial do braco do disco
    cilindro_inicial = int(conteudo[1])

    # Le as requisicoes de acesso
    requisicoes = conteudo[2:]

    # Instancia um objeto da class FCFS
    fcfs = FCFS()
    # Executa o algoritmo de escalonamento FCFS
    deslocamento_fcfs = fcfs.execute(cilindro_inicial, requisicoes)

    # Instancia um objeto da class SSTF
    sstf = SSTF()
    # Executa o algoritmo de escalonamento SSTF
    deslocamento_sstf = sstf.execute(cilindro_inicial, copy.deepcopy(requisicoes))

    # Instancia um objeto da class Elevador
    elevador = Elevador()
    # Executa o algoritmo de escalonamento Elevador
    deslocamento_elevador = elevador.execute(ultimo_cilindro, cilindro_inicial, requisicoes)

    # Exibe a saida
    print("-------------------------------------")
    print("|        Resultados obtidos         |")
    print("-------------------------------------")
    print("|   FCFS  |", deslocamento_fcfs, " setores percorridos|")
    print("-------------------------------------")
    print("|   SSTF  |", deslocamento_sstf, " setores percorridos|")
    print("-------------------------------------")
    print("| Elevador|", deslocamento_elevador, " setores percorridos|")
    print("-------------------------------------")

# Verifica se e o modulo principal e executa o codigo
if __name__ == "__main__":
    main()
