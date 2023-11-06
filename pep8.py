"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever código Python de forma Pythônica,

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass

def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para indentação!

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos em uma classe devem ser separados com uma única linha em branco

[5] - Imports

- Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problema em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de qualquer comentário ou docstrings
# antes de constantes, ou variáveis globais

[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não Faça:

algo (1)

# Faça:

algo(1)

# Não Faça:

dict ['chave'] = lista [índice]

# Faça:

dict['chave'] = lista[índice]

# Não Faça:

x              = 1
y              = 3
Variavel_Longa = 5

# Faça:

x = 1
y = 3
Variavel_Longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""
import this
