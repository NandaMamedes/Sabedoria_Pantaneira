# Interface da janela inicial do jogo

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QCursor
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QDialog
from banco_sqlite.banco_de_dados import adicionar_apelido, obter_pergunta_aleatoria_por_dificuldade, obter_opcoes, obter_resposta

############################### foi adicionado ####################################
from dotenv import load_dotenv

## GAMBIARRA TEMPORARIA 
interface_tela_onca = "C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_inicial_onça.ui"
interface_tela_arara = "C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_inicial_arara.ui"
interface_tela_capivara = "C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_inicial_capivara.ui"
interface_tela_jacare = "C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_inicial_jacare.ui"
interface_tela_tuiuiui = "C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_inicial_tuiuiu.ui"
interface_tela_apelido = "C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_apelido.ui"
interface_tela_pergunta = "C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_pergunta.ui"
interface_tela_confirmar = "C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_confirmar.ui"



class TelaInicialArara(QDialog):
    def __init__(self):
        super().__init__()

        #uic.loadUi("C:/projeto_software/tela_inicial_onça.ui", self)
        uic.loadUi(interface_tela_arara, self) # TESTE
       
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
        #uic.loadUi("C:/projeto_software/tela_inicial_onça.ui", self)
        uic.loadUi(interface_tela_onca, self) # TESTE

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
        #uic.loadUi("C:/projeto_software/tela_inicial_capivara.ui", self)
        uic.loadUi(interface_tela_capivara, self) # TESTE
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
        #uic.loadUi("C:/projeto_software/tela_inicial_jacaré.ui", self)
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
        #uic.loadUi("C:/projeto_software/tela_inicial_tuiuiu.ui", self)
        uic.loadUi(interface_tela_tuiuiu, self) # TESTE
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
        #uic.loadUi("C:/projeto_software/tela_apelido.ui", self)
        uic.loadUi(interface_tela_apelido, self) # TESTE
        self.tela_inicial = tela_inicial
        #self.label_imagem.setPixmap(QPixmap("C:/projeto_software/janela_apelido.png"))
        #self.label_imagem.setPixmap(QPixmap("C:/Users/cyber_edux__109/Documents/GitHub/Sabedoria_Pantaneira/apresentacao_ui/tela_inicial/janelas_tela_inicial/tela_apelido.png"))
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
            self.tela_pergunta = TelaPergunta(self)
            self.tela_pergunta.show()
        else:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Atenção", "Digite um apelido!")

perguntas_faceis = []
perguntas_medias = []
perguntas_dificeis = []

class TelaPergunta(QDialog):
    def __init__(self, tela_anterior):
        super().__init__()
        #uic.loadUi("C:/projeto_software/tela_pergunta.ui", self) #####################
        uic.loadUi(interface_tela_pergunta, self) # TESTE
        self.tela_anterior = tela_anterior

        self.pergunta = obter_pergunta_aleatoria_por_dificuldade("fácil")

        if not self.pergunta:
            print("⚠ Nenhuma pergunta fácil encontrada no banco!")
            self.label_pergunta.setText("Nenhuma pergunta encontrada.")
            return

        self.opcoes = obter_opcoes(self.pergunta)
        if not self.opcoes or len(self.opcoes) < 4:
            print(f"⚠ Não foi possível carregar opções para a pergunta: {self.pergunta}")
            self.label_pergunta.setText("Erro ao carregar opções.")
            return
        
        font_pergunta = QFont("Arial", 13, QFont.Weight.Bold)
        font_opcoes = QFont("Arial", 12)

        ##################  CÓDIGO QUEBRA DE LINHA ###################################
        self.label_pergunta.setFont(font_pergunta)
        self.label_pergunta.setWordWrap(True)
        self.label_pergunta.setText(self.pergunta)
        ###########################################################################

        self.label_pergunta.setFont(font_pergunta)
        for lbl in [self.label_a, self.label_b, self.label_c, self.label_d]:
            lbl.setFont(font_opcoes)

        self.label_pergunta.setText(self.pergunta)
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
        #uic.loadUi("C:/projeto_software/tela_confirmar.ui", self)
        uic.loadUi(interface_tela_confirmar, self) #TESTE
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
            #self.pontos += nivel_pergunta
            print("ACERTOU!")
            perguntas_faceis.append(self.pergunta)
            self.close()
            self.tela_anterior.close()
            self.nova_tela = TelaPergunta(self)
            self.nova_tela.show()

        else:
            print("ERROU!")
            self.close()
            self.tela_anterior.close()
            nova_janela = random.choice([TelaInicialArara, TelaInicialOnca, TelaInicialCapivara,
                                              TelaInicialJacare, TelaInicialTuiuiu])
            novo_jogo = nova_janela()
            novo_jogo.show()

        print(f'Resposta escolhida: {self.resposta_escolhida}')
        print(f'Resposta certa: {resposta_certa}')

    def fechar_janela(self, event):
        self.close()


class TelaPlacar(QDialog):
    def __init__(self, tela_inicial):
        super().__init__()
        uic.loadUi("C:/projeto_software/tela_apelido.ui", self)
        self.tela_inicial = tela_inicial
        self.label_imagem.setPixmap(QPixmap("C:/projeto_software/janela_apelido.png"))
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
