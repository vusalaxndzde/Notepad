import sys
from PyQt5 import QtWidgets, QtGui
import os

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QtWidgets.QTextEdit()
        self.font = 11
        self.yazi_tipi = 'Arial'

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_alani)

        self.setLayout(v_box)


class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Pencere()

        self.menu_olustur()

        self.setCentralWidget(self.pencere)
        self.setWindowTitle("Notepad")
        self.setGeometry(300, 170, 800, 430)
        self.setWindowIcon(QtGui.QIcon("ic/Notepad_icon.svg.png"))
        self.show()

    def menu_olustur(self):
        menubar = self.menuBar()

        dosya = menubar.addMenu("File")

        dosya_ac = QtWidgets.QAction("Open File..", self)
        dosya_ac.setShortcut("Ctrl+O")

        kaydet = QtWidgets.QAction("Save..", self)
        kaydet.setShortcut("Ctrl+S")

        cikis = QtWidgets.QAction("Quit", self)
        cikis.setShortcut("Ctrl+Q")

        temizle = QtWidgets.QAction("Clean", self)
        temizle.setShortcut("Ctrl+D")

        edit = menubar.addMenu("Edit")

        undo_typing = QtWidgets.QAction("Undo Typing", self)
        undo_typing.setShortcut("Ctrl+Z")

        view = menubar.addMenu("View")

        font_size = view.addMenu("Font Size")

        enlarge_font = QtWidgets.QAction("Enlarge font", self)
        enlarge_font.setShortcut("Ctrl+P")

        minimize_font = QtWidgets.QAction("Shrink font", self)
        minimize_font.setShortcut("Ctrl+M")

        standard_font = QtWidgets.QAction("Standard Font", self)
        standard_font.setShortcut("Ctrl+0")

        type = view.addMenu("Type")

        arial = QtWidgets.QAction("Arial", self)
        helvetica = QtWidgets.QAction("Helvetica", self)
        gabriola = QtWidgets.QAction("Gabriola", self)
        caveat = QtWidgets.QAction("Caveat", self)
        impact = QtWidgets.QAction("Impact", self)
        ink_free = QtWidgets.QAction("Ink Free", self)
        script = QtWidgets.QAction("Script", self)
        terminal = QtWidgets.QAction("Terminal", self)
        mv_boli = QtWidgets.QAction("MV Boli", self)
        monotype_corsiva = QtWidgets.QAction("Monotype Corsiva", self)
        small_font = QtWidgets.QAction("Small Fonts", self)
        modern = QtWidgets.QAction("Modern", self)
        self.type_list = [arial, helvetica, gabriola, caveat, impact, ink_free, script, terminal, mv_boli, monotype_corsiva, small_font, modern]

        for i in self.type_list:
            type.addAction(i)
        edit.addAction(undo_typing)
        edit.addAction(temizle)
        font_size.addAction(enlarge_font)
        font_size.addAction(minimize_font)
        font_size.addAction(standard_font)
        dosya.addAction(dosya_ac)
        dosya.addAction(kaydet)
        dosya.addAction(cikis)

        type.triggered.connect(self.type_writing)
        dosya.triggered.connect(self.response)
        view.triggered.connect(self.response)
        edit.triggered.connect(self.response)

    def response(self, action):

        if action.text() == "Open File..":
            dosya_ismi = QtWidgets.QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))

            with open(dosya_ismi[0], "r", encoding="utf-8") as file:
                self.pencere.yazi_alani.setText(file.read())

        elif action.text() == "Save..":
            dosya_ismi = QtWidgets.QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("HOME"))

            with open(dosya_ismi[0], "w", encoding="utf-8") as file:
                file.write(self.pencere.yazi_alani.toPlainText())

        elif action.text() == "Quit":
            QtWidgets.qApp.quit()

        elif action.text() == "Clean":
            self.pencere.yazi_alani.clear()

        elif action.text() == "Enlarge font":
            self.pencere.font += 3
            self.pencere.yazi_alani.setFont(QtGui.QFont(self.pencere.yazi_tipi, self.pencere.font))


        elif action.text() == "Shrink font":
            if self.pencere.font == 2:
                pass
            else:
                self.pencere.font -= 3
                self.pencere.yazi_alani.setFont(QtGui.QFont(self.pencere.yazi_tipi, self.pencere.font))

        elif action.text() == "Standard Font":
            self.pencere.font = 11
            self.pencere.yazi_alani.setFont(QtGui.QFont(self.pencere.yazi_tipi, self.pencere.font))

        elif action.text() == "Undo Typing":
            yazi_alani_text = self.pencere.yazi_alani.toPlainText()
            list(yazi_alani_text).pop()


    def type_writing(self, action):
        self.pencere.yazi_tipi = action.text()
        self.pencere.yazi_alani.setFont(QtGui.QFont(self.pencere.yazi_tipi, self.pencere.font))


app = QtWidgets.QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
