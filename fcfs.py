#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class FCFS:
    """Algoritmo de escalonamento First Come, First Serve (FCFS)"""

    def execute(self, cilindro_inicial, requisicoes):
        """
        Executa o algoritmo. Recebe como parametros o cilindro inicial onde
        esta o braco e as requisicoes de acesso subsequentes
        """
        # Inicializa o contador de cilindros percorridos com zero
        cilindros_percorridos = 0

        # Configura a posicao inicial do braco do disco
        posicao_atual = cilindro_inicial

        for requisicao in requisicoes:
            cilindros_percorridos += int(math.fabs(requisicao - posicao_atual))
            posicao_atual = requisicao

        return cilindros_percorridos
