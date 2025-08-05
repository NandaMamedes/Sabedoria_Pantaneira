# Banco de Dados

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CAMINHO_BANCO = os.path.join(BASE_DIR, 'BancoJogo.db')

import sqlite3
from banco_sqlite.perguntas_jogo.perguntas_historia import perguntas_historia as perguntas_historia
from banco_sqlite.perguntas_jogo.perguntas_geografia import perguntas_geografia as perguntas_geografia
from banco_sqlite.perguntas_jogo.perguntas_cultura import perguntas_cultura as perguntas_cultura
from banco_sqlite.perguntas_jogo.perguntas_meio_ambiente import perguntas_meio_ambiente as perguntas_meio_ambiente
from banco_sqlite.perguntas_jogo.perguntas_politica import perguntas_politica as perguntas_politica
from banco_sqlite.perguntas_jogo.perguntas_variedades import perguntas_variedades as perguntas_variedades
from dataclasses import dataclass

@dataclass
class Jogador:
    id: int = None
    jogador: str = ""
    pontuacao: str = ""
    nivel: str = ""
    categoria: str = ""

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)

def inicializar_db():
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Perguntas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pergunta TEXT NOT NULL,
                A TEXT NOT NULL,
                B TEXT NOT NULL,
                C TEXT NOT NULL,
                D TEXT NOT NULL,
                resposta TEXT NOT NULL,
                categoria TEXT NOT NULL,    
                dificuldade TEXT NOT NULL 
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS ranking_local (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jogador TEXT NOT NULL,
                pontuacao TEXT NOT NULL,
                nivel TEXT NOT NULL,
                categoria TEXT NOT NULL
            )
        """)
        conn.commit()

inicializar_db()

with conectar() as conn:
    cur = conn.cursor()

    for p in perguntas_historia:
        cur.execute("""
            INSERT INTO Perguntas (
                pergunta, A, B, C, D,
                resposta, categoria, dificuldade
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["pergunta"], p["A"], p["B"], p["C"], p["D"],
            p["resposta"], p["categoria"], p["dificuldade"]
        ))

    for p in perguntas_geografia:
        cur.execute("""
            INSERT INTO Perguntas (
                pergunta, A, B, C, D,
                resposta, categoria, dificuldade
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["pergunta"], p["A"], p["B"], p["C"], p["D"],
            p["resposta"], p["categoria"], p["dificuldade"]
        ))

    for p in perguntas_cultura:
        cur.execute("""
            INSERT INTO Perguntas (
                pergunta, A, B, C, D,
                resposta, categoria, dificuldade
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["pergunta"], p["A"], p["B"], p["C"], p["D"],
            p["resposta"], p["categoria"], p["dificuldade"]
        ))

    for p in perguntas_variedades:
        cur.execute("""
            INSERT INTO Perguntas (
                pergunta, A, B, C, D,
                resposta, categoria, dificuldade
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["pergunta"], p["A"], p["B"], p["C"], p["D"],
            p["resposta"], p["categoria"], p["dificuldade"]
        ))

    for p in perguntas_meio_ambiente:
        cur.execute("""
            INSERT INTO Perguntas (
                pergunta, A, B, C, D,
                resposta, categoria, dificuldade
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["pergunta"], p["A"], p["B"], p["C"], p["D"],
            p["resposta"], p["categoria"], p["dificuldade"]
        ))

    for p in perguntas_politica:
        cur.execute("""
            INSERT INTO Perguntas (
                pergunta, A, B, C, D,
                resposta, categoria, dificuldade
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["pergunta"], p["A"], p["B"], p["C"], p["D"],
            p["resposta"], p["categoria"], p["dificuldade"]
        ))

    conn.commit()

def adicionar_apelido(apelido: str):
    with conectar() as conn:
        conn.execute("INSERT INTO ranking_local (jogador, pontuacao, nivel, categoria) VALUES (?,?,?,?)",
                     (apelido,"N/A", "N/A", "N/A"))
        conn.commit()