Algoritmos de escalonamento do braço do disco
==

Algoritmos implementados:

* First Come, Firts Serve (FCFS)
* Shortest Seek Time First (SSTF)
* Elevador (Scan)



Formato do arquivo de entrada:

<pre>
  <code>
  199
  53
  98
  183
  37
  122
  14
  124
  65
  67
  </code>
</pre>

A entrada é composta por uma série de números inteiros, um por linha, indicando, primeiro o número do último cilindro no disco (os cilindros variam de 0 até esse número), o cilindro sobre o qual a cabeça de leitura está inicialmente posicionada e a sequência de requisições de acesso.

Formato da saída:

<pre>
  <code>
  FCFS 640
  SSTF 235
  ELEVADOR 299
  </code>
</pre>

A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade total de cilindros percorridos pela cabeça de leitura para atender todas as requisições de acesso ao disco.
