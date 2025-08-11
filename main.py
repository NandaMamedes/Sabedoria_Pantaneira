import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from apresentacao_ui.tela_inicial.janela_inicial import iniciar_jogo

if __name__ == "__main__":
    iniciar_jogo()