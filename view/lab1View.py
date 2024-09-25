from PyQt6.QtWidgets import QWidget
class Lab1View(QWidget):
    def __init__(self, main_window, controller=None):
        super().__init__()
        self.main_window = main_window
        self.controller = controller
        self.setupUi()
    def setupUi(self):
        self.main_window.startButton.clicked.connect(self.on_start_button_clicked)
    def set_controller(self, controller):
        self.controller = controller
    def on_start_button_clicked(self):
        if self.controller:
            self.controller.onStartButtonClicked()