#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fcfs import *
from sstf import *

# funcao principal
def main():
    # Le o numero do ultimo cilindro do disco
    ultimo_cilindro = int(sys.stdin.readline())

    # Le a posicao inicial do braco do disco
    cilindro_inicial = int(sys.stdin.readline())

    # Le as requisicoes de acesso
    requisicoes = map(int, sys.stdin.readlines())

    fcfs = FCFS()
    deslocamento_fcfs = fcfs.execute(cilindro_inicial, requisicoes)

    print("FCFS", deslocamento_fcfs)

    sstf = SSTF()
    deslocamento_sstf = sstf.execute(cilindro_inicial, requisicoes)

    print("SSTF", deslocamento_sstf)

# Verifica se e o modulo principal e executa o codigo
if __name__ == "__main__":
    main()
