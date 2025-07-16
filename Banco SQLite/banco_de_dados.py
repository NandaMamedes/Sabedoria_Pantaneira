# Banco de Dados

import sqlite3

DB_NAME = "BancoJogo.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def inicializar_db():
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Perguntas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pergunta TEXT NOT NULL
            )
        """)
        conn.commit()

conectar()
inicializar_db()