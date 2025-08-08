# Regras do jogo

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from banco_sqlite.banco_de_dados import obter_dificuldade
from dataclasses import dataclass

@dataclass
class Pergunta:
    id: int = None
    pergunta: str = ""
    a: str = ""
    b: str = ""
    c: str = ""
    d: str = ""
    resposta: str = ""
    categoria: str = ""
    dificuldade: str = ""

@dataclass
class Jogador:
    id: int = None
    jogador: str = ""
    pontuacao: str = ""
    nivel: str = ""
    categoria: str = ""

def verificar_resposta():
    print ("oi")

# def proxima_pergunta(p: Pergunta, j: Jogador):

def calcular_pontuacao():
    dificuldade = obter_dificuldade()

    nivel_facil = 10 # pontos
    nivel_medio = 25 # pontos
    nivel_dificil = 40 # pontos

    if dificuldade == "fácil":
        return nivel_facil




    # fácil, médio, difícil



# def historico_ranking(j: Jogador):
