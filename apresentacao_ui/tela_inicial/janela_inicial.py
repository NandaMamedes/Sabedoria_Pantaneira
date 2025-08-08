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
from banco_sqlite.banco_de_dados import adicionar_apelido, obter_pergunta_aleatoria, obter_opcoes, obter_resposta

class TelaInicialArara(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/projeto_software/tela_inicial_arara.ui", self)
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
        uic.loadUi("C:/projeto_software/tela_inicial_onça.ui", self)
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
        uic.loadUi("C:/projeto_software/tela_inicial_capivara.ui", self)
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
        uic.loadUi("C:/projeto_software/tela_inicial_jacaré.ui", self)
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
        uic.loadUi("C:/projeto_software/tela_inicial_tuiuiu.ui", self)
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
        uic.loadUi("C:/projeto_software/tela_apelido.ui", self)
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

perguntas_feitas = []

# class TelaPergunta(QDialog):
#     def __init__(self, tela_pergunta):
#         super().__init__()
#         uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_pergunta.ui", self)
#         self.tela_pergunta = tela_pergunta
#         self.label_a.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#         self.label_b.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#         self.label_c.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#         self.label_d.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
#         pergunta = obter_pergunta_aleatoria()

#         if pergunta is None:
#             print("Fim do jogo", "Você respondeu todas as perguntas!")
#             self.close()
#             return
        
#         self.label_pergunta.setText(pergunta)
#         opcoes = obter_opcoes(pergunta)

#         self.label_a.setText(opcoes[0])
#         self.label_b.setText(opcoes[1])
#         self.label_c.setText(opcoes[2])
#         self.label_d.setText(opcoes[3])

#         # self.label_a.mousePressEvent = self.confirmar_resposta_a
#         # self.label_b.mousePressEvent = self.confirmar_resposta_b
#         # self.label_c.mousePressEvent = self.confirmar_resposta_c
#         # self.label_d.mousePressEvent = self.confirmar_resposta_d

#         self.label_a.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_a.text())
#         self.label_b.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_b.text())
#         self.label_c.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_c.text())
#         self.label_d.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_d.text())


#         # opcoes = obter_opcoes(pergunta)
#         # self.label_pergunta.setText(pergunta)
#         # self.label_a.setText(opcoes[0]) 
#         # self.label_b.setText(opcoes[1]) 
#         # self.label_c.setText(opcoes[2])  
#         # self.label_d.setText(opcoes[3])

#         # self.label_a.mousePressEvent = self.confirmar_resposta
#         # self.label_b.mousePressEvent = self.confirmar_resposta
#         # self.label_c.mousePressEvent = self.confirmar_resposta
#         # self.label_d.mousePressEvent = self.confirmar_resposta

#     def confirmar_resposta_a(self, event, pergunta):
#         opcao = self.label_a.text()
#         resposta = obter_resposta(pergunta)
#         self.tela_confirmar = TelaConfirmar(self, resposta, opcao)
#         self.tela_confirmar.show()

#     # def confirmar_resposta_a(self, event, pergunta):
#     #     opcao = self.label_a.text()
#     #     resposta = obter_resposta(pergunta)
#     #     self.tela_confirmar = TelaConfirmar(self, resposta, opcao)
#     #     self.tela_confirmar.show()

#     # def confirmar_resposta_b(self, event, pergunta):
#     #     opcao = self.label_b.text()
#     #     resposta = obter_resposta(pergunta)
#     #     self.tela_confirmar = TelaConfirmar(self, resposta, opcao)
#     #     self.tela_confirmar.show()

#     # def confirmar_resposta_c(self, event, pergunta):
#     #     opcao = self.label_c.text()
#     #     resposta = obter_resposta(pergunta)
#     #     self.tela_confirmar = TelaConfirmar(self, resposta, opcao)
#     #     self.tela_confirmar.show()

#     # def confirmar_resposta_d(self, event, pergunta):
#     #     opcao = self.label_d.text()
#     #     resposta = obter_resposta(pergunta)
#     #     self.tela_confirmar = TelaConfirmar(self, resposta, opcao)
#     #     self.tela_confirmar.show()


# class TelaConfirmar(QDialog):
#     # def __init__(self, tela_confirmar):
#     #     super().__init__()
#     #     uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_confirmar.ui", self)
#     #     self.tela_confirmar = tela_confirmar
#     #     self.label_sim.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#     #     self.label_nao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

#     #     self.label_sim.mousePressEvent = self.verificar_resposta
#     #     self.label_nao.mousePressEvent = self.fechar_janela


#     def __init__(self, tela_confirmar, resposta, opcao):
#         super().__init__()
#         uic.loadUi("C:/Users/Família Anjos/Downloads/testes do projeto de jogo/tela_confirmar.ui", self)

#         self.tela_confirmar = tela_confirmar
#         self.resposta = resposta
#         self.opcao = opcao

#         self.label_sim.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#         self.label_nao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

#         self.label_sim.mousePressEvent = self.verificar_resposta
#         self.label_nao.mousePressEvent = self.fechar_janela

#     def verificar_resposta(self, event):
#         if self.resposta == self.opcao:
#             print("Resposta Correta", "Você acertou!")
#         else:
#             print("Resposta Errada", f"A resposta correta era: {self.resposta}")
        
#         self.tela_confirmar.close()
#         self.close()

#         self.nova_pergunta = TelaPergunta()
#         self.nova_pergunta.show()

#     def fechar_janela(self, event):
#         self.close()

class TelaPergunta(QDialog):
    def __init__(self, tela_anterior):
        super().__init__()
        uic.loadUi("C:/projeto_software/tela_pergunta.ui", self)
        self.tela_anterior = tela_anterior

        # Obtém uma pergunta aleatória
        self.pergunta = obter_pergunta_aleatoria()
        self.opcoes = obter_opcoes(self.pergunta)

        # Define o texto da pergunta e alternativas
        self.label_pergunta.setText(self.pergunta)
        self.label_a.setText(self.opcoes[0]) 
        self.label_b.setText(self.opcoes[1]) 
        self.label_c.setText(self.opcoes[2])  
        self.label_d.setText(self.opcoes[3])

        # Muda o cursor das labels
        self.label_a.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_b.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_c.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_d.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Conecta os cliques às funções, passando o texto clicado como argumento
        self.label_a.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_a.text())
        self.label_b.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_b.text())
        self.label_c.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_c.text())
        self.label_d.mousePressEvent = lambda event: self.confirmar_resposta(event, self.label_d.text())

    def confirmar_resposta(self, event, resposta_escolhida):
        # Abre janela de confirmação passando a resposta escolhida
        self.tela_confirmar = TelaConfirmar(self, self.pergunta, resposta_escolhida)
        self.tela_confirmar.show()


class TelaConfirmar(QDialog):
    def __init__(self, tela_anterior, pergunta, resposta_escolhida):
        super().__init__()
        uic.loadUi("C:/projeto_software/tela_confirmar.ui", self)
        self.tela_anterior = tela_anterior
        self.pergunta = pergunta
        self.resposta_escolhida = resposta_escolhida

        # Define o cursor nos botões
        self.label_sim.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_nao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Conecta os cliques aos métodos
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
            print("ERROU!")
            self.close()
            self.tela_anterior.close()
            nova_janela = random.choice([TelaInicialArara, TelaInicialOnca, TelaInicialCapivara,
                                              TelaInicialJacare, TelaInicialTuiuiu])
            novo_jogo = nova_janela()
            novo_jogo.show()

        print(resposta_certa)
        print(self.resposta_escolhida)

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