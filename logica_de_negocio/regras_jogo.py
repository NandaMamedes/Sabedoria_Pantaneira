# # Regras do jogo

# import os
# import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from banco_sqlite.banco_de_dados import conectar

# def obter_ultimo_apelido():
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute("SELECT jogador FROM ranking_local ORDER BY id DESC LIMIT 1")
#         apelido = cur.fetchone()
#         return apelido[0] if apelido else ""

# def apelido_existe(apelido: str) -> bool:
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute("SELECT 1 FROM ranking_local WHERE jogador = ?", (apelido,))
#         return cur.fetchone() is not None
    
# def obter_pergunta_aleatoria_por_dificuldade(dificuldade):
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute("""
#             SELECT pergunta 
#             FROM Perguntas 
#             WHERE dificuldade = ?
#             ORDER BY RANDOM() 
#             LIMIT 1
#         """, (dificuldade,))
#         pergunta = cur.fetchone()
#         print(f"🔍 Pergunta encontrada para '{dificuldade}': {pergunta}")
#         return pergunta[0] if pergunta else None

# def obter_opcoes(pergunta):
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute('SELECT A, B, C, D FROM Perguntas WHERE pergunta = ?', (pergunta,))
#         opcoes = cur.fetchone()
#         return opcoes if opcoes else (None, None, None, None)
    
# def obter_resposta(pergunta):
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute('SELECT resposta FROM Perguntas WHERE pergunta = ?', (pergunta,))
#         resposta = cur.fetchone()
#         return resposta[0] if resposta else None
    
# def obter_dificuldade(pergunta):
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute('SELECT dificuldade FROM Perguntas WHERE pergunta = ?', (pergunta,))
#         nivel_pergunta = cur.fetchone()
#         return nivel_pergunta[0] if nivel_pergunta else None

# def obter_categoria(pergunta):
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute('SELECT categoria FROM Perguntas WHERE pergunta = ?', (pergunta,))
#         categoria = cur.fetchone()
#         return categoria[0] if categoria else None
    
# def obter_pontuacao(apelido):
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute('SELECT pontuacao FROM ranking_local WHERE jogador = ?', (apelido,))
#         pontuacao_atual = cur.fetchone()
#         return pontuacao_atual[0] if pontuacao_atual else None

# def obter_historico(apelido: str):
#     with conectar() as conn:
#         cur = conn.cursor()
#         cur.execute("""
#             SELECT jogador, pontuacao, nivel, data_hora
#             FROM historico_jogador
#             WHERE jogador = ?
#             ORDER BY pontuacao DESC
#         """, (apelido,))
#         return cur.fetchall()

# Regras do jogo

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from banco_sqlite.banco_de_dados import conectar

# ------------------------------------------------------------------
# Funções de jogador
# ------------------------------------------------------------------

def obter_ultimo_apelido() -> str:
    """Retorna o último apelido cadastrado no ranking local."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT jogador FROM ranking_local ORDER BY id DESC LIMIT 1")
        apelido = cur.fetchone()
        return apelido[0] if apelido else ""


def apelido_existe(apelido: str) -> bool:
    """Verifica se o apelido já existe no ranking local."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM ranking_local WHERE jogador = ?", (apelido,))
        return cur.fetchone() is not None

# ------------------------------------------------------------------
# Funções de perguntas
# ------------------------------------------------------------------

def obter_pergunta_aleatoria_por_dificuldade(dificuldade: str) -> str | None:
    """Retorna uma pergunta aleatória para a dificuldade especificada."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT pergunta 
            FROM Perguntas 
            WHERE dificuldade = ?
            ORDER BY RANDOM() 
            LIMIT 1
        """, (dificuldade,))
        pergunta = cur.fetchone()
        print(f"🔍 Pergunta encontrada para '{dificuldade}': {pergunta}")
        return pergunta[0] if pergunta else None


def obter_opcoes(pergunta: str) -> tuple:
    """Retorna as opções A, B, C e D de uma pergunta."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT A, B, C, D FROM Perguntas WHERE pergunta = ?", (pergunta,))
        opcoes = cur.fetchone()
        return opcoes if opcoes else (None, None, None, None)


def obter_resposta(pergunta: str) -> str | None:
    """Retorna a resposta correta de uma pergunta."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT resposta FROM Perguntas WHERE pergunta = ?", (pergunta,))
        resposta = cur.fetchone()
        return resposta[0] if resposta else None


def obter_dificuldade(pergunta: str) -> str | None:
    """Retorna a dificuldade de uma pergunta."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT dificuldade FROM Perguntas WHERE pergunta = ?", (pergunta,))
        nivel_pergunta = cur.fetchone()
        return nivel_pergunta[0] if nivel_pergunta else None


def obter_categoria(pergunta: str) -> str | None:
    """Retorna a categoria de uma pergunta."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT categoria FROM Perguntas WHERE pergunta = ?", (pergunta,))
        categoria = cur.fetchone()
        return categoria[0] if categoria else None

# ------------------------------------------------------------------
# Funções de pontuação e histórico
# ------------------------------------------------------------------

def obter_pontuacao(apelido: str) -> int | None:
    """Retorna a pontuação atual de um jogador."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT pontuacao FROM ranking_local WHERE jogador = ?", (apelido,))
        pontuacao_atual = cur.fetchone()
        return pontuacao_atual[0] if pontuacao_atual else None


def obter_historico(apelido: str) -> list[tuple]:
    """Retorna o histórico de pontuação de um jogador, ordenado do maior para o menor."""
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT jogador, pontuacao, nivel, data_hora
            FROM historico_jogador
            WHERE jogador = ?
            ORDER BY pontuacao DESC
        """, (apelido,))
        return cur.fetchall()
