import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PySide6.QtGui import QAction
from PySide6.QtPrintSupport import QPrintPreviewDialog, QPrinter
from PySide6.QtGui import QPainter, QTextDocument

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.create_actions()
        self.create_menus()

    def create_actions(self):
        self.print_preview_action = QAction("Print Preview...", self)
        self.print_preview_action.triggered.connect(self.handle_print_preview)

    def create_menus(self):
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(self.print_preview_action)

    def handle_print_preview(self):
        # Create a QPrinter object
        printer = QPrinter()
        
        # Create the print preview dialog, passing the printer
        preview_dialog = QPrintPreviewDialog(printer, self)
        
        # Connect the paintRequested signal to our drawing function
        preview_dialog.paintRequested.connect(self.print_document)
        
        # Show the dialog
        preview_dialog.exec()

    def print_document(self, printer):
        # This function is called by the preview dialog to render each page
        document = self.editor.document()
        document.print_(printer) # QTextDocument has a built-in print_ method

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
