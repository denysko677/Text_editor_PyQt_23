import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QVBoxLayout, QWidget, QPushButton, QMessageBox, QFileDialog


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Текстовий редактор")
        self.setGeometry(100, 100, 800, 600)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createToolBar()

    def createActions(self):
        self.newAction = QAction("&Новий", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.newFile)

        self.openAction = QAction("&Відкрити", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.openFile)

        self.saveAction = QAction("&Зберегти", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.saveFile)

        self.exitAction = QAction("&Вихід", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.triggered.connect(self.close)

    def createMenus(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu("&Файл")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)

    def createToolBar(self):
        toolbar = self.addToolBar("Засоби")

        toolbar.addAction(self.newAction)
        toolbar.addAction(self.openAction)
        toolbar.addAction(self.saveAction)

    def newFile(self):
        self.textEdit.clear()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Відкрити файл", "", "Text files (*.txt);;All files (*.*)")

        if filename:
            with open(filename, "r") as file:
                text = file.read()
                self.textEdit.setText(text)

    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Зберегти файл", "", "Text files (*.txt);;All files (*.*)")

        if filename:
            with open(filename, "w") as file:
                text = self.textEdit.toPlainText()
                file.write(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
