from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QPlainTextEdit,
    QPushButton,
)
import sys

from cuteseq import algorithm


class CuteSeqWidget(QWidget):
    def __init__(self):
        """Construction de l'interface graphique 
        """
        super().__init__()

        self.setWindowTitle("CuteSeq")

        #  Création des widgets
        ## Création des deux zones de textes
        self.input_edit = QPlainTextEdit()
        self.output_edit = QPlainTextEdit()

        ## Création de la liste déroulante
        self.algo_combo = QComboBox()

        ## Création du bouton appliquer
        self.apply_button = QPushButton("Apply")

        # Organisation des widgets dans un layout
        ## Création du layout principale vertical
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_edit)
        main_layout.addWidget(self.output_edit)
        ## Création du layout horizontal contenant la liste déroulante et le bouton
        bar_layout = QHBoxLayout()
        bar_layout.addStretch()
        bar_layout.addWidget(self.algo_combo)
        bar_layout.addWidget(self.apply_button)
        ## Ajout du dernier layout
        main_layout.addLayout(bar_layout)

        # Application du layout au widget
        self.setLayout(main_layout)

        #  Redimensionne le widget
        self.resize(400, 300)

        # Charge les fonctions dans la liste deroulante
        # Le deuxieme argument permet de stocker n'importe quoi, comme ici une fonction
        self.algo_combo.addItem("Reverse", algorithm.reverse)
        self.algo_combo.addItem("complement", algorithm.complement)
        self.algo_combo.addItem("reverse-complement", algorithm.reverse_complement)

        # Connection de l'evenement bouton "clicked" à la méthode on_apply
        self.apply_button.clicked.connect(self.on_apply)

    def on_apply(self):
        """
        Méthode appelé lorsque l'on clique sur le bouton 
        """

        #  On récupère le texte en entré
        seq_in = self.input_edit.toPlainText()
        # On récupère la fonction choisi
        transform = self.algo_combo.currentData()
        # On applique la transformation
        seq_out = transform(seq_in)
        #  On écrit le résultat dans la sortie
        self.output_edit.setPlainText(seq_out)
