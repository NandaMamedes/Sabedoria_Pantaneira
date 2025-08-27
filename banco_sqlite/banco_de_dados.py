# Banco de Dados

import os
import sys
import sqlite3

# ------------------------------------------------------------------
# Configurações de caminho
# ------------------------------------------------------------------

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(BASE_DIR, 'BancoJogo.db')

# ------------------------------------------------------------------
# Importação das perguntas por categoria
# ------------------------------------------------------------------

from banco_sqlite.perguntas_jogo.perguntas_historia import perguntas_historia
from banco_sqlite.perguntas_jogo.perguntas_geografia import perguntas_geografia
from banco_sqlite.perguntas_jogo.perguntas_cultura import perguntas_cultura
from banco_sqlite.perguntas_jogo.perguntas_meio_ambiente import perguntas_meio_ambiente
from banco_sqlite.perguntas_jogo.perguntas_politica import perguntas_politica
from banco_sqlite.perguntas_jogo.perguntas_variedades import perguntas_variedades

# ------------------------------------------------------------------
# Conexão com o banco
# ------------------------------------------------------------------

def conectar() -> sqlite3.Connection:
    return sqlite3.connect(CAMINHO_BANCO)

# ------------------------------------------------------------------
# Inicialização do banco e criação de tabelas
# ------------------------------------------------------------------

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
                pontuacao TEXT NOT NULL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS historico_jogador (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jogador TEXT NOT NULL,
                pontuacao INTEGER NOT NULL,
                data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

# Inicializa o banco

inicializar_db()

# ------------------------------------------------------------------
# Inserção inicial das perguntas
# ------------------------------------------------------------------

with conectar() as conn:
    cur = conn.cursor()

    def inserir_pergunta(p: dict):
        cur.execute("SELECT 1 FROM Perguntas WHERE pergunta = ?", (p["pergunta"],))
        if cur.fetchone() is None:
            cur.execute("""
                INSERT INTO Perguntas (
                    pergunta, A, B, C, D,
                    resposta, categoria, dificuldade
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                p["pergunta"], p["A"], p["B"], p["C"], p["D"],
                p["resposta"], p["categoria"], p["dificuldade"]
            ))

    for categoria in [
        perguntas_historia, perguntas_geografia, perguntas_cultura,
        perguntas_variedades, perguntas_meio_ambiente, perguntas_politica
    ]:
        for p in categoria:
            inserir_pergunta(p)

    conn.commit()

# ------------------------------------------------------------------
# Funções de jogador e pontuação
# ------------------------------------------------------------------

def adicionar_apelido(apelido: str):
    with conectar() as conn:
        conn.execute(
            "INSERT INTO ranking_local (jogador, pontuacao) VALUES (?,?)",
            (apelido, "N/A")
        )
        conn.commit()


def registrar_progresso(apelido: str, pontuacao: int):
    with conectar() as conn:
        conn.execute("""
            UPDATE ranking_local
            SET pontuacao = ?
            WHERE jogador = ?
        """, (pontuacao, apelido))
        conn.commit()


def salvar_historico(apelido: str, pontuacao: int):
    with conectar() as conn:
        conn.execute("""
            INSERT INTO historico_jogador (jogador, pontuacao)
            VALUES (?, ?)
        """, (apelido, pontuacao))
        conn.commit()
