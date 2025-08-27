# ------------------------------------------------------------------
# Código main.py para rodar o jogo
# ------------------------------------------------------------------

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from apresentacao_ui.interface_game import iniciar_jogo

if __name__ == "__main__":
    iniciar_jogo()