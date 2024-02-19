import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QPushButton, QFileDialog, QFontDialog, QColorDialog


class TextEditorModel:
    def __init__(self):
        self.text = ""

    def load_text(self, filename):
        with open(filename, "r") as file:
            self.text = file.read()

    def save_text(self, filename, text):
        with open(filename, "w") as file:
            file.write(text)


class TextEditorController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.new_button.clicked.connect(self.new_file)
        self.view.open_button.clicked.connect(self.open_file)
        self.view.save_button.clicked.connect(self.save_file)
        self.view.font_button.clicked.connect(self.change_font)
        self.view.text_color_button.clicked.connect(self.change_text_color)
        self.view.bg_color_button.clicked.connect(self.change_bg_color)

    def new_file(self):
        self.view.text_edit.clear()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self.view, "Відкрити файл", "", "Text files (*.txt);;All files (*.*)")
        if filename:
            self.model.load_text(filename)
            self.view.text_edit.setText(self.model.text)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self.view, "Зберегти файл", "", "Text files (*.txt);;All files (*.*)")
        if filename:
            text = self.view.text_edit.toPlainText()
            self.model.save_text(filename, text)

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.view.text_edit.setFont(font)

    def change_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.view.text_edit.setTextColor(color)

    def change_bg_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.view.text_edit.setStyleSheet("background-color: {}".format(color.name()))


class TextEditorView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Текстовий редактор")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 10, 780, 480)

        self.new_button = QPushButton("Новий", self)
        self.new_button.setGeometry(10, 500, 80, 30)

        self.open_button = QPushButton("Відкрити", self)
        self.open_button.setGeometry(100, 500, 80, 30)

        self.save_button = QPushButton("Зберегти", self)
        self.save_button.setGeometry(190, 500, 80, 30)

        self.font_button = QPushButton("Шрифт", self)
        self.font_button.setGeometry(280, 500, 80, 30)

        self.text_color_button = QPushButton("Колір тексту", self)
        self.text_color_button.setGeometry(370, 500, 110, 30)

        self.bg_color_button = QPushButton("Колір фону", self)
        self.bg_color_button.setGeometry(490, 500, 110, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = TextEditorView()
    model = TextEditorModel()
    controller = TextEditorController(view, model)
    view.show()
    sys.exit(app.exec_())
