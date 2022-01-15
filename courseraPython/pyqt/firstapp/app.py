import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit
from random import choice


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    # def __init__(self):
    #     super(MainWindow, self).__init__()
    #     self.button_state = False
    #     self.n_times_clicked = 0
    #     self.setWindowTitle("My app")

    #     self.button = QPushButton("Push Me!")
    #     # button.setCheckable(True)
    #     # button.setChecked(self.button_state)
    #     self.button.clicked.connect(self.button_was_clicked)
    #     self.windowTitleChanged.connect(self.window_title_changed)
    #     # button.clicked.connect(self.button_was_toggled)

    #     self.setCentralWidget(self.button)
    #     self.setMinimumSize(QSize(400, 300))
    #     # self.setMaximumSize(QSize(1000, 800))

    # def button_was_clicked(self):
    #     # self.button.setText("You already Clicked me!")
    #     # self.button.setEnabled(False)
    #     # self.setWindowTitle("My Onehot App")
    #     print("Clicked!")
    #     new_window_title = choice(window_titles)
    #     print("Setting Title: %s" % new_window_title)
    #     self.setWindowTitle(new_window_title)

    # # def button_was_toggled(self, checked):
    # #     self.button_state = checked
    # #     print("Checked?", self.button_state)

    # def window_title_changed(self, window_title):
    #     print("Window Title Changed: %s" % window_title)
    #     if window_title == 'Something went wrong':
    #         self.button.setDisabled(True)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.label = QLabel("Click here")

        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)

        # container = QWidget()
        # container.setLayout(layout)
        self.setMouseTracking(True)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
