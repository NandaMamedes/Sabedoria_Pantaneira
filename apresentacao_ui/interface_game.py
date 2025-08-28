# Interface do jogo

import os
import sys
import random
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QCursor, QPixmap
from PyQt6.QtWidgets import QApplication, QDialog

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from banco_sqlite.banco_de_dados import (
    adicionar_apelido_ranking, adicionar_apelido_historico, registrar_progresso_ranking, registrar_progresso_historico, salvar_historico
)
from logica_de_negocio.regras_jogo import (
    apelido_existe, obter_ultimo_apelido, obter_pergunta_aleatoria_por_dificuldade,
    obter_opcoes, obter_resposta, obter_categoria,
    obter_pontuacao, obter_historico
)

# PASTA BASE DO PROJETO

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# PASTAS DE UI E IMAGENS

TELAS_PATH = os.path.join(BASE_DIR, "telas_game")
IMAGENS_PATH = os.path.join(BASE_DIR, "imagens_game")

# -------------------------------
# Caminhos relativos das interfaces .ui
# -------------------------------

interface_tela_jacare = os.path.join(TELAS_PATH, "tela_inicial_jacare.ui")
interface_tela_arara = os.path.join(TELAS_PATH, "tela_inicial_arara.ui")
interface_tela_capivara = os.path.join(TELAS_PATH, "tela_inicial_capivara.ui")
interface_tela_onca = os.path.join(TELAS_PATH, "tela_inicial_onca.ui")
interface_tela_tuiuiu = os.path.join(TELAS_PATH, "tela_inicial_tuiuiu.ui")
interface_tela_apelido = os.path.join(TELAS_PATH, "tela_apelido.ui")
interface_tela_historico = os.path.join(TELAS_PATH, "tela_historico.ui")
interface_tela_fim = os.path.join(TELAS_PATH, "tela_fim_jogo.ui")
interface_tela_ganhador = os.path.join(TELAS_PATH, "tela_ganhador.ui")
interface_tela_confirmar = os.path.join(TELAS_PATH, "tela_confirmar.ui")
interface_tela_placar = os.path.join(TELAS_PATH, "tela_placar.ui")

interface_tela_ambiente = os.path.join(TELAS_PATH, "tela_pergunta_ambiente.ui")
interface_tela_cultura = os.path.join(TELAS_PATH, "tela_pergunta_cultura.ui")
interface_tela_geografia = os.path.join(TELAS_PATH, "tela_pergunta_geografia.ui")
interface_tela_historia = os.path.join(TELAS_PATH, "tela_pergunta_historia.ui")
interface_tela_politica = os.path.join(TELAS_PATH, "tela_pergunta_politica.ui")
interface_tela_variedades = os.path.join(TELAS_PATH, "tela_pergunta_variedades.ui")

# -------------------------------
# Caminhos relativos das interfaces .png e .jpeg
# -------------------------------

IMAGENS_PERGUNTA = {
    "História": os.path.join(IMAGENS_PATH, "janela_pergunta_historia.png"),
    "Geografia": os.path.join(IMAGENS_PATH, "janela_pergunta_geografia.png"),
    "Cultura": os.path.join(IMAGENS_PATH, "janela_pergunta_cultura.jpeg"),
    "Variedades": os.path.join(IMAGENS_PATH, "janela_pergunta_variedades.jpeg"),
    "Meio Ambiente": os.path.join(IMAGENS_PATH, "janela_pergunta_ambiente.jpeg"),
    "Política": os.path.join(IMAGENS_PATH, "janela_pergunta_politica.jpeg")
}

# ------------------------------------------------------------------
# Classes de tela inicial para cada animal
# ------------------------------------------------------------------

class TelaInicialBase(QDialog):
    def __init__(self, ui_path):
        super().__init__()
        uic.loadUi(ui_path, self)
        imagem_apelido_path = os.path.join(IMAGENS_PATH, "imagem_apelido.png")
        self.label_imagem.setPixmap(QPixmap(imagem_apelido_path))

        self.label_jogar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_placar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_jogar.mousePressEvent = self.abrir_tela_apelido
        self.label_placar.mousePressEvent = self.abrir_tela_placar

    def abrir_tela_apelido(self, event):
        self.tela_apelido = TelaApelido(self)
        self.tela_apelido.show()

    def abrir_tela_placar(self, event):
        self.tela_placar = TelaPlacar(self)
        self.tela_placar.show()


class TelaInicialArara(TelaInicialBase):
    def __init__(self):
        super().__init__(interface_tela_arara)
        imagem_arara_path = os.path.join(IMAGENS_PATH, "imagem_arara.png")
        self.label_imagem.setPixmap(QPixmap(imagem_arara_path))


class TelaInicialOnca(TelaInicialBase):
    def __init__(self):
        super().__init__(interface_tela_onca)
        imagem_onca_path = os.path.join(IMAGENS_PATH, "imagem_onca.png")
        self.label_imagem.setPixmap(QPixmap(imagem_onca_path))


class TelaInicialCapivara(TelaInicialBase):
    def __init__(self):
        super().__init__(interface_tela_capivara)
        imagem_capivara_path = os.path.join(IMAGENS_PATH, "imagem_capivara.png")
        self.label_imagem.setPixmap(QPixmap(imagem_capivara_path))


class TelaInicialJacare(TelaInicialBase):
    def __init__(self):
        super().__init__(interface_tela_jacare)
        imagem_jacare_path = os.path.join(IMAGENS_PATH, "imagem_jacare.png")
        self.label_imagem.setPixmap(QPixmap(imagem_jacare_path))


class TelaInicialTuiuiu(TelaInicialBase):
    def __init__(self):
        super().__init__(interface_tela_tuiuiu)
        imagem_tuiuiu_path = os.path.join(IMAGENS_PATH, "imagem_tuiuiu.png")
        self.label_imagem.setPixmap(QPixmap(imagem_tuiuiu_path))

# ------------------------------------------------------------------
# Tela de apelido
# ------------------------------------------------------------------

class TelaApelido(QDialog):
    def __init__(self, tela_inicial):
        super().__init__()
        uic.loadUi(interface_tela_apelido, self)
        imagem_apelido_path = os.path.join(IMAGENS_PATH, "imagem_apelido.png")
        self.label_imagem.setPixmap(QPixmap(imagem_apelido_path))

        self.tela_inicial = tela_inicial
        self.label_continuar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_continuar.mousePressEvent = self.verificar_apelido

        ultimo = obter_ultimo_apelido()
        if ultimo:
            self.line_apelido.setText(ultimo)

    def verificar_apelido(self, event):
        apelido = self.line_apelido.text().strip()
        if not apelido:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Atenção", "Digite um apelido!")
            return

        if not apelido_existe(apelido):
            adicionar_apelido_ranking(apelido)
            adicionar_apelido_historico(apelido)

        if apelido_existe(apelido):
            adicionar_apelido_historico(apelido)

        self.close()
        self.tela_inicial.close()
        self.tela_pergunta = TelaPergunta(self, "fácil")
        self.tela_pergunta.show()

# ------------------------------------------------------------------
# Variáveis globais do jogo
# ------------------------------------------------------------------

perguntas_feitas = []
pontuacao = 0
acertos_faceis = 0
acertos_medios = 0
acertos_dificeis = 0
dificuldade_atual = "fácil"

# ------------------------------------------------------------------
# Tela de pergunta
# ------------------------------------------------------------------

class TelaPergunta(QDialog):
    def __init__(self, tela_anterior, dificuldade):
        super().__init__()
        
        self.tela_anterior = tela_anterior
        self.dificuldade = dificuldade

        tentativas = 0

        while True:
            self.pergunta = obter_pergunta_aleatoria_por_dificuldade(self.dificuldade)
            tentativas += 1

            if not self.pergunta:
                print("⚠ Nenhuma pergunta encontrada no banco!")
                uic.loadUi(interface_tela_ambiente, self)
                self.label_pergunta.setText("Nenhuma pergunta disponível.")
                return

            if self.pergunta not in perguntas_feitas:
                perguntas_feitas.append(self.pergunta)
                break

            if tentativas > 30:
                print("⚠ Todas as perguntas já foram usadas!")
                uic.loadUi(interface_tela_ambiente, self)
                self.label_pergunta.setText("Sem perguntas disponíveis.")
                return

        self.categoria = obter_categoria(self.pergunta)

        ui_interfaces = {
            "História": interface_tela_historia,
            "Geografia": interface_tela_geografia,
            "Cultura": interface_tela_cultura,
            "Variedades": interface_tela_variedades,
            "Meio Ambiente": interface_tela_ambiente,
            "Política": interface_tela_politica
        }
        uic.loadUi(ui_interfaces.get(self.categoria, interface_tela_ambiente), self)

        imagem_path = IMAGENS_PERGUNTA.get(self.categoria)

        if hasattr(self, "label_imagem") and imagem_path:
            self.label_imagem.setPixmap(QPixmap(imagem_path))
            self.label_imagem.setScaledContents(True)

        self.opcoes = obter_opcoes(self.pergunta)
        if not self.opcoes or len(self.opcoes) < 4:
            self.label_pergunta.setText("Erro ao carregar opções.")
            return

        font_pergunta = QFont("Arial", 16, QFont.Weight.Bold if len(self.pergunta) <= 75 else 15)
        font_opcoes = QFont("Arial", 13)
        self.label_pergunta.setFont(font_pergunta)
        self.label_pergunta.setWordWrap(True)
        self.label_pergunta.setText(self.pergunta)

        for lbl, opcao in zip([self.label_a, self.label_b, self.label_c, self.label_d], self.opcoes):
            lbl.setFont(font_opcoes)
            lbl.setText(opcao)
            lbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            lbl.mousePressEvent = lambda event, opcao=opcao: self.confirmar_resposta(event, opcao)

    def confirmar_resposta(self, event, resposta_escolhida):
        self.tela_confirmar = TelaConfirmar(self, self.pergunta, resposta_escolhida)
        self.tela_confirmar.show()

# ------------------------------------------------------------------
# Tela de confirmação de resposta
# ------------------------------------------------------------------

class TelaConfirmar(QDialog):
    def __init__(self, tela_anterior, pergunta, resposta_escolhida):
        super().__init__()
        uic.loadUi(interface_tela_confirmar, self)
        imagem_confirmar_path = os.path.join(IMAGENS_PATH, "imagem_confirmar.png")
        self.label_imagem.setPixmap(QPixmap(imagem_confirmar_path))

        self.tela_anterior = tela_anterior
        self.pergunta = pergunta
        self.resposta_escolhida = resposta_escolhida

        self.label_sim.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_nao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.label_sim.mousePressEvent = self.verificar_resposta
        self.label_nao.mousePressEvent = self.fechar_janela

    def verificar_resposta(self, event):
        global pontuacao, acertos_faceis, acertos_medios, acertos_dificeis, dificuldade_atual
        
        resposta_certa = obter_resposta(self.pergunta)

        if resposta_certa == self.resposta_escolhida:
            print("✅ ACERTOU!")

            if dificuldade_atual == "fácil":
                pontuacao += 5
                print(f"Pontuação: {pontuacao}")
                acertos_faceis += 1
                print(f"Acertos fáceis: {acertos_faceis}/15")

                if acertos_faceis >= 15:
                    dificuldade_atual = "médio"
                    print("🚀 Avançou para dificuldade MÉDIA!")

            elif dificuldade_atual == "médio":
                    pontuacao += 10 
                    print(f"Pontuação: {pontuacao}")
                    acertos_medios += 1
                    print(f"Acertos médios: {acertos_medios}/10")
                    
                    if acertos_medios >= 10:
                        dificuldade_atual = "difícil"
                        print("🚀 Avançou para dificuldade DIFÍCIL!")
        
            elif dificuldade_atual == "difícil":
                pontuacao += 15
                print(f"Pontuação: {pontuacao}")
                acertos_dificeis += 1
                print(f"Acertos difíceis: {acertos_dificeis}/5")

                if acertos_dificeis == 5:
                    acertos_faceis = 0
                    acertos_medios = 0
                    acertos_dificeis = 0
                    
                    apelido = obter_ultimo_apelido()
                    pontuacao_atual = obter_pontuacao(apelido)
                    
                    if pontuacao_atual == "N/A":
                        registrar_progresso_ranking(apelido, pontuacao_atual)
                        registrar_progresso_historico(apelido, pontuacao_atual)
                    
                    else:
                        pontuacao_atual = int(pontuacao_atual) + pontuacao
                        salvar_historico(apelido, pontuacao)
                        registrar_progresso_ranking(apelido, pontuacao_atual)
                        
                    dificuldade_atual = "fácil"
                    perguntas_feitas.clear()
                    
                    self.close()
                    self.tela_anterior.close()
                    self.tela_ganhador = TelaGanhador(self, pontuacao_atual)
                    self.tela_ganhador.show()
                    pontuacao = 0
                    return

            self.close()
            self.tela_anterior.close()
            self.nova_tela = TelaPergunta(self, dificuldade_atual) 
            self.nova_tela.show()

        else:
            print("❌ ERROU!")
            acertos_faceis = 0
            acertos_medios = 0
            acertos_dificeis = 0
            
            apelido = obter_ultimo_apelido()
            pontuacao_atual = obter_pontuacao(apelido)
            
            if pontuacao_atual == "N/A":
                salvar_historico(apelido, pontuacao)
                registrar_progresso_ranking(apelido, pontuacao)
                
            else:
                pontuacao_atual = int(pontuacao_atual) + pontuacao
                salvar_historico(apelido, pontuacao)
                registrar_progresso_ranking(apelido, pontuacao_atual)
    
            dificuldade_atual = "fácil"
            perguntas_feitas.clear()
            
            self.close()
            self.tela_fim = TelaFim(self.tela_anterior, self.pergunta)
            self.tela_fim.show()
            pontuacao = 0

    def fechar_janela(self, event):
        self.close()

# ------------------------------------------------------------------
# Tela de fim de jogo
# ------------------------------------------------------------------

class TelaFim(QDialog):
    def __init__(self, tela_anterior, pergunta):
        super().__init__()
        uic.loadUi(interface_tela_fim, self)
        imagem_fim_path = os.path.join(IMAGENS_PATH, "imagem_fim_jogo.png")
        self.label_imagem.setPixmap(QPixmap(imagem_fim_path))

        self.tela_anterior = tela_anterior
        self.pergunta = pergunta

        resposta_certa = obter_resposta(self.pergunta)

        self.label_reiniciar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font_resposta = QFont("Arial", 15, QFont.Weight.Bold)
        self.label_resposta_certa.setFont(font_resposta)
        self.label_resposta_certa.setText(resposta_certa)
        self.label_resposta_certa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_reiniciar.mousePressEvent = self.reiniciar_jogo

    def reiniciar_jogo(self, event):
        self.close()
        self.tela_anterior.close()
        
        telas_iniciais = [
            TelaInicialArara,
            TelaInicialOnca,
            TelaInicialCapivara,
            TelaInicialJacare,
            TelaInicialTuiuiu
            ]
        TelaEscolhida = random.choice(telas_iniciais)
        self.janela_inicial = TelaEscolhida()  
        self.janela_inicial.show()

# ------------------------------------------------------------------
# Tela de ganhador
# ------------------------------------------------------------------

class TelaGanhador(QDialog):
    def __init__(self, tela_anterior, pontuacao_atual):
        super().__init__()
        uic.loadUi(interface_tela_ganhador, self)
        imagem_ganhador_path = os.path.join(IMAGENS_PATH, "imagem_ganhador.png")
        self.label_imagem.setPixmap(QPixmap(imagem_ganhador_path))

        self.tela_anterior = tela_anterior
        self.pontuacao_atual = str(pontuacao_atual)

        self.label_jogar_novamente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        font_pontuacao = QFont("Arial", 28, QFont.Weight.Bold)
        self.label_pontuacao.setFont(font_pontuacao)
        self.label_pontuacao.setText(self.pontuacao_atual)
        self.label_pontuacao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_jogar_novamente.mousePressEvent = self.jogar_novamente

    def jogar_novamente(self, event):
        self.close()
        self.tela_anterior.close()
        
        telas_iniciais = [
            TelaInicialArara,
            TelaInicialOnca,
            TelaInicialCapivara,
            TelaInicialJacare,
            TelaInicialTuiuiu
            ]
        TelaEscolhida = random.choice(telas_iniciais)
        self.janela_inicial = TelaEscolhida()  
        self.janela_inicial.show()

# ------------------------------------------------------------------
# Tela de placar
# ------------------------------------------------------------------

class TelaPlacar(QDialog):
    def __init__(self, tela_anterior=None):
        super().__init__()
        self.tela_anterior = tela_anterior
        uic.loadUi(interface_tela_historico, self)
        self.setStyleSheet("background-color: #FFD580;") 

        apelido = obter_ultimo_apelido()
        pontuacao_geral = obter_pontuacao(apelido)
        tabela_historico = obter_historico(apelido)

        texto = f"PONTUAÇÃO GERAL: {pontuacao_geral}\n\nHISTÓRICO DO JOGADOR:\n\n"
        for linha in tabela_historico:
            jogador, pontuacao, data_hora = linha
            if pontuacao != "N/A":
                texto += f"Jogador: {jogador}\nPontos: {pontuacao}\nData: {data_hora}\n\n"

        self.label_historico.setText(texto)
        self.label_historico.setWordWrap(True)
        self.label_historico.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.label_historico.setFont(QFont("Arial", 15, QFont.Weight.Bold))

# ------------------------------------------------------------------
# Função para iniciar o jogo
# ------------------------------------------------------------------

def iniciar_jogo():
    app = QApplication(sys.argv)
    janela_escolhida = random.choice([
        TelaInicialArara, TelaInicialOnca, TelaInicialCapivara,
        TelaInicialJacare, TelaInicialTuiuiu
    ])
    janela = janela_escolhida()
    janela.show()
    sys.exit(app.exec())
