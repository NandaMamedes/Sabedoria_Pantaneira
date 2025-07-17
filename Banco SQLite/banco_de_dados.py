# Banco de Dados

import sqlite3
from perguntas_historia import perguntas_historia
from perguntas_geografia import perguntas_geografia
from perguntas_cultura import perguntas_cultura
from perguntas_variedades import perguntas_variedades

DB_NAME = "BancoJogo.db"

def conectar():
    return sqlite3.connect(DB_NAME)

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
    conn.commit()
