from PySide2.QtWidgets import QApplication
from cuteseq.gui import CuteSeqWidget

import sys

if __name__ == "__main__":

    #  Création d'une application
    app = QApplication(sys.argv)

    # Création d'un widget
    w = CuteSeqWidget()

    # affichage du widget
    w.show()

    #  execution de la boucle evenementielle
    app.exec_()
