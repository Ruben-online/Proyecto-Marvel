from CircularListDoubleLinked import CircularListDoubleLinked
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit

lista = CircularListDoubleLinked()

lista.insertar_inicio(1)
lista.insertar_inicio(2)
lista.insertar_inicio(3)
lista.insertar_inicio(4)
lista.insertar_inicio(5)
lista.insertar_inicio(6)

# IMPRIMIR
print("Lista Circular")
lista.printList()

# ELIMINAR
print("Eliminar elemento especifico")
lista.eliminar(4)
print("Lista Actualizada")
lista.printList()

# BUSCAR
print("Buscar elemento")
busca = lista.buscar(1)
if busca == None:
    print("El elemento no existe")
else:
    print("Si existe", busca)

# INSERTAR AL INICIO
print("Insertar en un indice")
lista.insertar_indice(1, 1.5)
print("Lista Actualizada")
lista.printList()
