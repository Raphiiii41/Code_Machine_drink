""" Interface bluetooth (Edrink)"""
""" Programmeur : Raphaël Genois """


from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel



def PB(texte, taille=(100, 30), couleur_fond="#4CAF50", couleur_texte="white", position=(0, 0), taille_texte=12):
    """
    Description des paramètre de la fonction:

    texte: Texte affiché sur le bouton.
    taille: Tuple (largeur, hauteur) de la taille du bouton.
    couleur_fond: Couleur de fond du bouton (format hexadécimal ou nom de couleur).
    couleur_texte: Couleur du texte du bouton (format hexadécimal ou nom de couleur).
    position: Tuple (x, y) de la position du coin supérieur gauche du bouton.
    taille_texte: Taille du texte du bouton.
    """
    bouton = QPushButton(texte)

    # Définition de la taille du bouton
    bouton.setFixedSize(*taille)

    # Utilisation de la feuille de style pour définir les couleurs et la taille du texte
    bouton.setStyleSheet(f"background-color: {couleur_fond}; color: {couleur_texte}; font-size: {taille_texte}px;")

    # Définition de la position du bouton
    bouton.move(*position)

    return bouton

def txt(texte, taille=(100, 30), couleur_texte="black", position=(0, 0), police="Arial", taille_texte=12):
    """
    Description des paramètre de la fonction:

    texte: Texte affiché.
    taille: Tuple (largeur, hauteur) de la taille du texte.
    couleur_texte: Couleur du texte (format hexadécimal ou nom de couleur).
    position: Tuple (x, y) de la position du coin supérieur gauche du texte.
    police: Nom de la police du texte.
    taille_texte: Taille du texte.
    """
    texte_widget = QLabel(texte)

    # Définition de la taille du texte
    texte_widget.setFixedSize(*taille)

    # Utilisation de la feuille de style pour définir la couleur et la taille du texte
    texte_widget.setStyleSheet(f"color: {couleur_texte}; font-family: {police}; font-size: {taille_texte}px;")

    # Définition de la position du texte
    texte_widget.move(*position)

    return texte_widget

if __name__ == '__main__':

    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

    app = QApplication([])

    fenetre = QWidget()

    # Création des boutons
    PB1 = PB("Rhum n Coke", taille=(500, 100), couleur_fond="#5AF740", couleur_texte="black", position=(500, 150), taille_texte=20)
    PB2 = PB("Gin Tonic", taille=(500, 100), couleur_fond="#5AF740", couleur_texte="black", position=(500, 275), taille_texte=20)

    # Création des textes
    Txt1 = txt("Machine à Drink", taille=(400, 50), couleur_texte="purple", position=(625, 10), police="Helvetica", taille_texte=36)
    Txt2 = txt("Menu", taille=(200, 50), couleur_texte="black", position=(710, 75), police="Helvetica",taille_texte=30)
    Txt3 = txt("1 c'est bien mais 2 c'est mieux!", taille=(500, 50), couleur_texte="black", position=(585, 675), police="Helvetica", taille_texte=26)


    # Configuration de la mise en page
    layout = QVBoxLayout()
    fenetre.setLayout(layout)

    # Ajout des boutons à la fenêtre après avoir défini sa position
    PB1.setParent(fenetre)
    PB2.setParent(fenetre)

    # Ajout des textes à la fenêtre après avoir défini sa position
    Txt1.setParent(fenetre)
    Txt2.setParent(fenetre)
    Txt3.setParent(fenetre)

    # Configuration de la fenêtre principale
    fenetre.setGeometry(200, 150, 1500, 750)
    fenetre.setWindowTitle('Bouton Personnalisé')

    fenetre.show()
    app.exec_()

