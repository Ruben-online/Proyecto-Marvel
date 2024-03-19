import sys
import requests
import hashlib
import time
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QDialog, \
    QGridLayout, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt



# Clase para la ventana principal
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    # Ventana principal
    def init_ui(self):
        self.setWindowTitle("Marvel API")
        self.setFixedSize(1200, 600)

        # Poner imagen en el background
        background_label = QLabel(self)
        pixmap = QPixmap("marvel_studios.jpg").scaled(self.size())
        background_label.setPixmap(pixmap)

        main_layout = QVBoxLayout()

        background_layout = QVBoxLayout()
        background_layout.addWidget(background_label)
        main_layout.addLayout(background_layout)

        buttons_layout = QHBoxLayout()

        # Botones
        btn_comics = QPushButton("Ver Comics", self)
        btn_comics.clicked.connect(self.show_comics)
        self.stylize_button(btn_comics)
        btn_comics.setMaximumSize(100, 30)
        buttons_layout.addWidget(btn_comics)

        btn_characters = QPushButton("Ver Personajes", self)
        btn_characters.clicked.connect(self.show_characters)
        self.stylize_button(btn_characters)
        btn_characters.setMaximumSize(100, 30)
        buttons_layout.addWidget(btn_characters)

        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    # Estetica de los botones
    def stylize_button(self, button):
        button.setStyleSheet(
            """
            QPushButton {
                background-color: #0077cc;
                color: white;
                border: 2px solid #005fa3;
                border-radius: 5px;
                padding: 5px;
            }

            QPushButton:hover {
                background-color: #005fa3;
            }
            """
        )

    # Boton para ir a la ventana 'Comics'
    def show_comics(self):
        comics_window = ComicsWindow()
        comics_window.exec()

    # Boton para ir a la ventana 'Personajes'
    def show_characters(self):
        characters_window = CharactersWindow()
        characters_window.exec()

# Clase para la ventana de los comics
class ComicsWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Comics")
        self.setGeometry(450, 200, 600, 400)

        # Para poner una imagen en el background
        background_label = QLabel(self)
        pixmap = QPixmap("comics_window_background.jpg").scaled(self.size())
        background_label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(background_label)

        btn1 = QPushButton("Listado de comics", self)
        btn1.clicked.connect(self.show_comics_list)
        self.stylize_button(btn1)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(btn1)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    # La estetica de los botones
    def stylize_button(self, button):
        button.setStyleSheet(
            """
            QPushButton {
                background-color: #0077cc;
                color: white;
                border: 2px solid #005fa3;
                border-radius: 5px;
                padding: 5px;
            }

            QPushButton:hover {
                background-color: #005fa3;
            }
            """
        )

    # Funcion para que el boton de la lista de comics
    def show_comics_list(self):
        comics_list_window = ComicsListWindow()
        comics_list_window.exec()