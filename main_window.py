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
        


# Clase para la ventana 'Personajes'
class CharactersWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personajes")
        self.setGeometry(450, 200, 600, 400)

        # Para poner una imagen en el background
        background_label = QLabel(self)
        pixmap = QPixmap("characters_window_background.jpg").scaled(self.size())
        background_label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(background_label)

        # Botón
        btn_open_another_window = QPushButton("Listado de personajes", self)
        btn_open_another_window.clicked.connect(self.open_characters_list)
        self.stylize_button(btn_open_another_window)
        layout.addWidget(btn_open_another_window)

        self.setLayout(layout)

    # Estilo de los botones
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

    # Boton para ingresar a ventana 'Lista de personajes'
    def open_characters_list(self):
        characters_list_window = CharactersListWindow()
        characters_list_window.exec()

# Clase para la ventana 'Lista de comics'
class ComicsListWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Listado de Comics")
        self.setFixedSize(1200, 600)

        layout = QVBoxLayout()

        # Campo de búsqueda
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar comics por nombre...")
        self.search_input.returnPressed.connect(self.search_comics)
        layout.addWidget(self.search_input)

        self.comics_container = QWidget()
        self.comics_layout = QGridLayout()
        self.comics_container.setLayout(self.comics_layout)
        layout.addWidget(self.comics_container)

        # Botones de navegación
        self.prev_button = QPushButton("Anterior")
        self.prev_button.clicked.connect(self.load_prev_comics)
        self.next_button = QPushButton("Siguiente")
        self.next_button.clicked.connect(self.load_next_comics)

        self.page = 0
        self.total_comics = 0
        self.comics_per_page = 10

        self.load_comics()

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.prev_button)
        nav_layout.addWidget(self.next_button)
        layout.addLayout(nav_layout)

        self.setLayout(layout)

    # Cargar la info de los comics
    def load_comics(self):
        public_key = "f9712edbc70c02735339a12234d8b1ff"
        private_key = "aa753940dacd70f1d2f39da2f8557cdb8a2d8084"
        timestamp = str(int(time.time()))
        hash_value = hashlib.md5((timestamp + private_key + public_key).encode('utf-8')).hexdigest()

        base_url = "http://gateway.marvel.com/v1/public/comics"
        params = {
            "ts": timestamp,
            "apikey": public_key,
            "hash": hash_value,
            "limit": self.comics_per_page,
            "offset": self.page * self.comics_per_page
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            self.total_comics = data["data"]["total"]
            self.update_pagination_buttons()

            comics = data["data"]["results"]
            self.show_comics(comics)
        else:
            print(f"Error en la solicitud: {response.status_code}")
            print(response.text)

    # Cargar las imagenes
    def load_image(self, url):
        response = requests.get(url)
        image = QPixmap()
        if response.status_code == 200:
            image.loadFromData(response.content)
        else:
            print(f"Error al cargar la imagen: {response.status_code}")
        return image

    # Funcion para mostrar la info de los comics en la ventana 'Lista de comics'
    def show_comics(self, comics):
        # Limpiar el layout antes de cargar nuevos cómics
        self.clear_comics_container()

        row = 0
        col = 0

        for comic in comics:
            comic_name = comic["title"]
            comic_img_url = f"{comic["thumbnail"]["path"]}/portrait_uncanny.{comic["thumbnail"]["extension"]}"

            try:
                comic_img = QLabel()
                pixmap = self.load_image(comic_img_url)
                comic_img.setPixmap(pixmap)
                self.comics_layout.addWidget(comic_img, row, col)

                comic_label = QLabel(f"{comic_name}")
                comic_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.comics_layout.addWidget(comic_label, row + 1, col)

                col += 1
                if col >= 5:
                    row += 2
                    col = 0
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")
                print(f"URL de la imagen: {comic_img_url}")

    # Funcion que permite avanzar y regresar
    def update_pagination_buttons(self):
        self.prev_button.setEnabled(self.page > 0)
        self.next_button.setEnabled((self.page + 1) * self.comics_per_page < self.total_comics)

    # Funcion para el boton regresar, regresa a la pagina anterior
    def load_prev_comics(self):
        self.page -= 1
        self.load_comics()

    # Funcion para el boton siguiente, avanza a la siguiente pagina
    def load_next_comics(self):
        self.page += 1
        self.load_comics()

    # API request
    def search_comics(self):
        search_text = self.search_input.text()
        if search_text:
            public_key = "f9712edbc70c02735339a12234d8b1ff"
            private_key = "aa753940dacd70f1d2f39da2f8557cdb8a2d8084"
            timestamp = str(int(time.time()))
            hash_value = hashlib.md5((timestamp + private_key + public_key).encode('utf-8')).hexdigest()

            base_url = "http://gateway.marvel.com/v1/public/comics"
            params = {
                "ts": timestamp,
                "apikey": public_key,
                "hash": hash_value,
                "limit": self.comics_per_page,
                "titleStartsWith": search_text
            }

            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                self.clear_comics_container()
                self.total_comics = data["data"]["total"]
                comics = data["data"]["results"]
                self.show_comics(comics)
            else:
                print(f"Error en la solicitud: {response.status_code}")
                print(response.text)

    # Para borrar la informacion, asi al avanzar, no se ponen una encima de la otra. Limpia antes de avanzar
    def clear_comics_container(self):
        for i in reversed(range(self.comics_layout.count())):
            widget = self.comics_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)