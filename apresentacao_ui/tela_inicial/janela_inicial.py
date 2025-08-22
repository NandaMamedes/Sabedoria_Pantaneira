# Interface da janela inicial do jogo

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from dotenv import load_dotenv
from PyQt6.QtGui import QCursor
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QDialog
from banco_sqlite.banco_de_dados import (adicionar_apelido, obter_pergunta_aleatoria_por_dificuldade, obter_opcoes, obter_resposta, obter_categoria,
                                         obter_ultimo_apelido, apelido_existe)

load_dotenv()

interface_tela_onca = os.getenv("INTERFACE_TELA_ONCA")
interface_tela_arara =  os.getenv("INTERFACE_TELA_ARARA")
interface_tela_capivara = os.getenv("INTERFACE_TELA_CAPIVARA")
interface_tela_jacare = os.getenv("INTERFACE_TELA_JACARE")
interface_tela_tuiuiui = os.getenv("INTERFACE_TELA_TUIUIU")
interface_tela_apelido = os.getenv("INTERFACE_TELA_APELIDO")
interface_tela_pergunta = os.getenv("INTERFACE_TELA_PERGUNTA")
interface_tela_confirmar = os.getenv("INTERFACE_TELA_CONFIRMAR")
interface_tela_fim = os.getenv("INTERFACE_TELA_FIM")

interface_tela_ambiente = os.getenv("INTERFACE_TELA_AMBIENTE")
interface_tela_cultura =  os.getenv("INTERFACE_TELA_CULTURA")
interface_tela_geografia = os.getenv("INTERFACE_TELA_GEOGRAFIA")
interface_tela_historia = os.getenv("INTERFACE_TELA_HISTORIA")
interface_tela_politica = os.getenv("INTERFACE_TELA_POLITICA")
interface_tela_variedades = os.getenv("INTERFACE_TELA_VARIEDADES")


class TelaInicialArara(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface_tela_arara, self) 
       
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


class TelaInicialOnca(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface_tela_onca, self)

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


class TelaInicialCapivara(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface_tela_capivara, self)
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


class TelaInicialJacare(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface_tela_jacare, self) # TESTE
        self.label_jogar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_placar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_jogar.mousePressEvent = self.abrir_tela_apelido
        self.label_placar.mousePressEvent = self.abrir_tela_apelido

    def abrir_tela_apelido(self, event):
        self.tela_apelido = TelaApelido(self)
        self.tela_apelido.show()

    def abrir_tela_placar(self, event):
        self.tela_placar = TelaPlacar(self)
        self.tela_placar.show()


class TelaInicialTuiuiu(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface_tela_tuiuiui, self) # TESTE
        self.label_jogar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_placar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_jogar.mousePressEvent = self.abrir_tela_apelido
        self.label_placar.mousePressEvent = self.abrir_tela_apelido

    def abrir_tela_apelido(self, event):
        self.tela_apelido = TelaApelido(self)
        self.tela_apelido.show()

    def abrir_tela_placar(self, event):
        self.tela_placar = TelaPlacar(self)
        self.tela_placar.show()


class TelaApelido(QDialog):
    def __init__(self, tela_inicial):
        super().__init__()
        uic.loadUi(interface_tela_apelido, self)
        self.tela_inicial = tela_inicial
        self.label_imagem.setScaledContents(True)
        self.label_continuar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_continuar.mousePressEvent = self.verificar_apelido

        ultimo = obter_ultimo_apelido()
        if ultimo:
            self.line_apelido.setText(ultimo)

    def verificar_apelido(self, event):
        apelido = self.line_apelido.text().strip()
        if apelido:
            if apelido_existe(apelido):
                print("Apelido:", apelido)
                self.close()
                self.tela_inicial.close()
                self.tela_pergunta = TelaPergunta(self)
                self.tela_pergunta.show()
            else:
                print("Apelido:", apelido)
                adicionar_apelido(apelido)
                self.close()
                self.tela_inicial.close()
                self.tela_pergunta = TelaPergunta(self)
                self.tela_pergunta.show()
        else:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Atenção", "Digite um apelido!")


perguntas_feitas = []

class TelaPergunta(QDialog):
    def __init__(self, tela_anterior):
        super().__init__()
        self.tela_anterior = tela_anterior

        tentativas = 0

        while True:
            self.pergunta = obter_pergunta_aleatoria_por_dificuldade("fácil")
            tentativas += 1

            if not self.pergunta:
                print("⚠ Nenhuma pergunta fácil encontrada no banco!")
                uic.loadUi(interface_tela_ambiente, self) 
                self.label_pergunta.setText("Nenhuma pergunta encontrada.")
                return

            if self.pergunta not in perguntas_feitas:
                print("Pergunta nova")
                perguntas_feitas.append(self.pergunta)
                print(perguntas_feitas)
                break
            else:
                print("Pergunta repetida, buscando outra...")

            if tentativas > 30:
                print("⚠ Todas as perguntas já foram usadas!")
                uic.loadUi(interface_tela_ambiente, self) 
                self.label_pergunta.setText("Sem perguntas disponíveis.")
                return

        self.categoria = obter_categoria(self.pergunta)

        if self.categoria == "História":
            ui_path = interface_tela_historia
        elif self.categoria == "Geografia":
            ui_path = interface_tela_geografia
        elif self.categoria == "Cultura":
            ui_path = interface_tela_cultura
        elif self.categoria == "Variedades":
            ui_path = interface_tela_variedades
        elif self.categoria == "Meio Ambiente":
            ui_path = interface_tela_ambiente
        elif self.categoria == "Política":
            ui_path = interface_tela_politica
        else:
            ui_path = interface_tela_ambiente

        uic.loadUi(ui_path, self)

        self.opcoes = obter_opcoes(self.pergunta)
        if not self.opcoes or len(self.opcoes) < 4:
            print(f"⚠ Não foi possível carregar opções para a pergunta: {self.pergunta}")
            self.label_pergunta.setText("Erro ao carregar opções.")
            return
        
        if len(self.pergunta) > 75:
            font_pergunta = QFont("Arial", 10, QFont.Weight.Bold)
        else:
            font_pergunta = QFont("Arial", 11, QFont.Weight.Bold)

        font_opcoes = QFont("Arial", 10)
        self.label_pergunta.setFont(font_pergunta)
        self.label_pergunta.setWordWrap(True)
        self.label_pergunta.setText(self.pergunta)

        for lbl in [self.label_a, self.label_b, self.label_c, self.label_d]:
            lbl.setFont(font_opcoes)

        self.label_a.setText(self.opcoes[0])
        self.label_b.setText(self.opcoes[1])
        self.label_c.setText(self.opcoes[2])
        self.label_d.setText(self.opcoes[3])

        for lbl in [self.label_a, self.label_b, self.label_c, self.label_d]:
            lbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.label_a.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_a.text())
        self.label_b.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_b.text())
        self.label_c.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_c.text())
        self.label_d.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_d.text())

    def confirmar_resposta(self, event, resposta_escolhida):
        self.tela_confirmar = TelaConfirmar(self, self.pergunta, resposta_escolhida)
        self.tela_confirmar.show()


class TelaConfirmar(QDialog):
    def __init__(self, tela_anterior, pergunta, resposta_escolhida):
        super().__init__()
        uic.loadUi(interface_tela_confirmar, self)
        self.tela_anterior = tela_anterior
        self.pergunta = pergunta
        self.resposta_escolhida = resposta_escolhida
        # self.pontos = 0

        self.label_sim.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_nao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.label_sim.mousePressEvent = self.verificar_resposta
        self.label_nao.mousePressEvent = self.fechar_janela

    def verificar_resposta(self, event):
        print(f"Pergunta: {self.pergunta}")
        print(f"Resposta escolhida: {self.resposta_escolhida}")
        resposta_certa = obter_resposta(self.pergunta)
        if resposta_certa == self.resposta_escolhida:
            print("ACERTOU!")
            self.close()
            self.tela_anterior.close()
            self.nova_tela = TelaPergunta(self)
            self.nova_tela.show()

        else:
            perguntas_feitas.clear()
            self.close()
            self.tela_fim = TelaFim(self.tela_anterior, self.pergunta)
            self.tela_fim.show()

    def fechar_janela(self, event):
        self.close()
        

class TelaFim(QDialog):
    def __init__(self, tela_anterior, pergunta):
        super().__init__()
        uic.loadUi(interface_tela_fim, self)
        self.tela_anterior = tela_anterior
        self.pergunta = pergunta
        
        resposta_certa = obter_resposta(self.pergunta)
            
        self.label_resposta_certa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_reiniciar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            
        font_resposta = QFont("Arial", 11, QFont.Weight.Bold)
        self.label_resposta_certa.setFont(font_resposta)
        self.label_resposta_certa.setText(resposta_certa)
        self.label_resposta_certa.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
        self.label_reiniciar.mousePressEvent = self.reiniciar_jogo
            
    def reiniciar_jogo(self, event):
        self.close()
        self.tela_anterior.close()
        
        nova_janela = random.choice([TelaInicialArara, TelaInicialOnca, TelaInicialCapivara,
                                              TelaInicialJacare, TelaInicialTuiuiu])
        novo_jogo = nova_janela()
        novo_jogo.show()
            

class TelaPlacar(QDialog):
    def __init__(self, tela_inicial):
        super().__init__()
        self.tela_inicial = tela_inicial
        self.label_imagem.setScaledContents(True)
        self.label_continuar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_continuar.mousePressEvent = self.verificar_apelido

    def verificar_apelido(self, event):
        apelido = self.line_apelido.text().strip()
        if apelido:
            print("Apelido:", apelido)
            adicionar_apelido(apelido)
            self.close()
            self.tela_inicial.close()
        else:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Atenção", "Digite um apelido!")


def iniciar_jogo():
    app = QApplication(sys.argv)
    janela_escolhida = random.choice([
        TelaInicialArara, TelaInicialOnca, TelaInicialCapivara,
        TelaInicialJacare, TelaInicialTuiuiu
    ])
    janela = janela_escolhida()
    janela.show()
    sys.exit(app.exec())
