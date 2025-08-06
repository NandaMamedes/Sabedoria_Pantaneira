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
from banco_sqlite.banco_de_dados import adicionar_apelido, perguntas, obter_pergunta_aleatoria, obter_opcoes

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
            print("Apelido:", apelido)
            adicionar_apelido(apelido)
            self.close()
            self.tela_inicial.close()
            self.tela_pergunta = TelaPergunta(self)
            self.tela_pergunta.show()
        else:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Atenção", "Digite um apelido!")


class TelaPergunta(QDialog):
    def __init__(self, tela_pergunta):
        super().__init__()
        uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_pergunta.ui", self)
        self.tela_pergunta = tela_pergunta
        self.label_a.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_b.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_c.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_d.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # perguntas_jogo = perguntas()
        pergunta_aleatoria = obter_pergunta_aleatoria()
        if pergunta_aleatoria:
            print("Pergunta aleatória:", pergunta_aleatoria)
        else:
            print("Nenhuma pergunta encontrada.")

        pergunta = obter_pergunta_aleatoria()
        if pergunta:
            print("Pergunta:", pergunta)
            opcoes = obter_opcoes(pergunta)

        self.label_pergunta.setText(pergunta)
        self.label_a.setText(opcoes[0]) 
        self.label_b.setText(opcoes[1]) 
        self.label_c.setText(opcoes[2])  
        self.label_d.setText(opcoes[3])

        self.label_a.mousePressEvent = self.verificar_resposta
        self.label_b.mousePressEvent = self.verificar_resposta
        self.label_c.mousePressEvent = self.verificar_resposta
        self.label_d.mousePressEvent = self.verificar_resposta

    def verificar_resposta(self, event):
        resposta = self.label_a.text().strip()
        if resposta:
            print("resposta dada:", resposta)
            self.close()
            self.tela_pergunta.close()
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
    


# def get_random_question(self):
#         # Busca todas as perguntas não utilizadas
#         all_questions = self.db.get_all_questions()
#         available = [q for q in all_questions if q[0] not in self.used_questions]
        
#         if not available:
#             return None  # Todas as perguntas foram usadas
            
#         # Seleciona uma pergunta aleatória
#         import random
#         question = random.choice(available)
#         self.used_questions.add(question[0])
#         return question
    
#     def carregar_nova_pergunta(self):
#         question = self.quiz.get_random_question()
        
#         if not question:
#             QMessageBox.information(self, "Fim do Quiz", 
#                                   "Você respondeu todas as perguntas disponíveis!")
#             self.close()
#             return
        
#         self.current_question = question
        
#         # Atualiza a interface
#         self.question_label.setText(question[1])  # Texto da pergunta
#         self.label_a.setText(f"A) {question[2]}")  # Opção A
#         self.label_b.setText(f"B) {question[3]}")  # Opção B
#         self.label_c.setText(f"C) {question[4]}")  # Opção C
#         self.label_d.setText(f"D) {question[5]}")  # Opção D
        
#         # Conecta os eventos de clique
#         self.option_a.mousePressEvent = lambda e: self.check_answer("A")
#         self.option_b.mousePressEvent = lambda e: self.check_answer("B")
#         self.option_c.mousePressEvent = lambda e: self.check_answer("C")
#         self.option_d.mousePressEvent = lambda e: self.check_answer("D")

#     def check_answer(self, selected_option):
#         correct_answer = self.current_question[6]
        
#         if selected_option == correct_answer:
#             QMessageBox.information(self, "Resposta", "✅ Resposta correta!")
#         else:
#             QMessageBox.warning(self, "Resposta", 
#                               f"❌ Resposta incorreta! A correta é {correct_answer}")
        
#         self.load_new_question()