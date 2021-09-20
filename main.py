import time
from functools import partial

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QWidget, QPushButton, QLineEdit, QInputDialog, \
    QDialog
from PyQt5.QtGui import QPixmap
import sys
import os


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.setWindowTitle('Просмотр техники')
        self.app_height = app_height
        self.app_width = app_width
        self.setGeometry(0, 0, self.app_width, self.app_height)

    def select_degree_of_damage(self):
        """Запуск формы с возможностью выбрать степень повреждения на изображении"""
        self.test = DegreeForm()
        degree = """тут мы каким-то образом получим данные из формы"""
        return degree

    def move_to_folder(self, folder_name):
        """Получаем степень повреждения. Перемещаем фото в выбранную папку, добавляя степень к его имени"""
        degree = self.select_degree_of_damage()
        new_path = work_dir + f'/{folder_name}' + folder_name[0] + degree + self.image_path[
                                                                            self.image_path.rindex('/'):]
        # os.replace(self.image_path, new_path)

    def load_image(self, image_path):
        pixmap = QPixmap(image_path).scaled(self.app_width - 100, self.app_height - 100, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.resize(self.app_width, self.app_height)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_path = image_path

    def show_toolbar(self):
        folder_list = list(filter(lambda s: '.' not in s, os.listdir(work_dir)))
        toolbar = QToolBar('Toolbar')

        """Кнопка перехода к предыдущему фото"""
        toolbar.addWidget(QtWidgets.QPushButton(text='previous'))

        """Выкладываем на панель инструментов кнопки для каждой из имеющихся в рабочей директории папок """
        for folder in folder_list:
            folder_button = QtWidgets.QPushButton(folder, self)
            folder_button.clicked.connect(partial(self.move_to_folder, folder_name=folder))
            toolbar.addWidget(folder_button)

        """Кнопка перехода к следующему фото"""
        toolbar.addWidget(QtWidgets.QPushButton(text='next'))

        self.addToolBar(toolbar)



"""Эту НЁХ нам предоставил дизайнер и мы очень хотим её завести но пока не получается"""
class DegreeForm(object):
    def __init__(self):
        form = QDialog()
        self.setupUi(form)

    def setupUi(self, Form):
        Form.setObjectName("Form666")
        Form.resize(417, 72)
        Form.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.zero_button = QtWidgets.QPushButton(Form)
        self.zero_button.setGeometry(QtCore.QRect(10, 20, 85, 33))
        self.zero_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.zero_button.setObjectName("zero_button")
        # self.zero_button.clicked.connect(self.return_data)
        self.one_button = QtWidgets.QPushButton(Form)
        self.one_button.setGeometry(QtCore.QRect(110, 20, 85, 33))
        self.one_button.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.one_button.setObjectName("one_button")
        self.two_button = QtWidgets.QPushButton(Form)
        self.two_button.setGeometry(QtCore.QRect(210, 20, 85, 33))
        self.two_button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.two_button.setObjectName("two_button")
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(310, 20, 85, 33))
        self.cancel_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.setEnabled(False)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.zero_button.setText(_translate("Form", "0"))
        self.one_button.setText(_translate("Form", "1"))
        self.two_button.setText(_translate("Form", "2"))
        self.cancel_button.setText(_translate("Form", "Отмена"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    """Получаем данные размера окна """
    app_geometry = app.desktop().screenGeometry()
    app_height = app_geometry.height()
    app_width = app_geometry.width()

    """Создание объекта окна просмотра изображения"""
    view_window = Window()

    """Получаем путь к файлу изображения"""
    wb_patch = QtWidgets.QFileDialog.getOpenFileName(options=QtWidgets.QFileDialog.DontUseNativeDialog)[0]

    """Получаем путь к рабочей папке с изображениями и папками для сортировки"""
    work_dir = wb_patch[:wb_patch.rindex('/'):]

    view_window.load_image(wb_patch)
    view_window.show_toolbar()
    view_window.show()

    sys.exit(app.exec_())
