# Regras do jogo

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

# def calcular_pontuacao(p: Pergunta, j: Jogador):

# def historico_ranking(j: Jogador):


