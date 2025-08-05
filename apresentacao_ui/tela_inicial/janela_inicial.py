# Interface da janela inicial do jogo

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QDialog
from banco_sqlite.banco_de_dados import adicionar_apelido, verificar_apelido

class TelaInicialArara(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_inicial_arara.ui", self)
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
        uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_inicial_onça.ui", self)
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
        uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_inicial_capivara.ui", self)
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
        uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_inicial_jacaré.ui", self)
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
        uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_inicial_tuiuiu.ui", self)
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
        uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_apelido.ui", self)
        self.tela_inicial = tela_inicial
        self.label_imagem.setPixmap(QPixmap("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/janela_apelido.png"))
        self.label_imagem.setScaledContents(True)
        self.label_continuar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_continuar.mousePressEvent = self.verificar_apelido

    def verificar_apelido(self, event):
        apelido = self.line_apelido.text().strip()
        if apelido:
            verificar_apelido(apelido)
            print("Apelido:", apelido)
            adicionar_apelido(apelido)
            self.close()
            self.tela_inicial.close()
        else:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Atenção", "Digite um apelido!")


class TelaPlacar(QDialog):
    def __init__(self, tela_inicial):
        super().__init__()
        uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_apelido.ui", self)
        self.tela_inicial = tela_inicial
        self.label_imagem.setPixmap(QPixmap("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/janela_apelido.png"))
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
    