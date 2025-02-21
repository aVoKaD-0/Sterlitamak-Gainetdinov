import sys
import os
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
sys.path.append(os.path.join(os.path.dirname(__file__), 'UI'))

from UI.main_ui import Ui_MainWindow  
from UI.addEditCoffeeForm_ui import Ui_AddEditCoffeeForm  

class CoffeeApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        self.setupUi(self)
        self.load_data()
        
        # Connect buttons to methods
        self.addButton.clicked.connect(self.openAddEditForm)
        self.editButton.clicked.connect(self.openAddEditForm)

    def load_data(self):
        connection = sqlite3.connect('data/coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        connection.close()

        table_widget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        
        table_widget.setRowCount(len(rows))
        table_widget.setColumnCount(7)  

        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                table_widget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(data)))

    def openAddEditForm(self):
        self.addEditForm = AddEditCoffeeForm()
        self.addEditForm.show()

class AddEditCoffeeForm(QtWidgets.QWidget, Ui_AddEditCoffeeForm):
    saved = pyqtSignal()  # Определяем сигнал
    def __init__(self):
        super(AddEditCoffeeForm, self).__init__()
        self.setupUi(self)  
        
        self.saveButton.clicked.connect(self.saveCoffee)

    def saveCoffee(self):
        # Получаем данные из полей ввода
        name = self.nameLineEdit.text()
        roast_level = self.roastLevelLineEdit.text()
        ground_bean = self.groundBeanLineEdit.text()
        description = self.descriptionLineEdit.text()
        price = self.priceLineEdit.text()
        package_volume = self.packageVolumeLineEdit.text()

        # Логика для сохранения записи в базе данных
        connection = sqlite3.connect('data/coffee.sqlite')
        cursor = connection.cursor()
        
        # Вставка новой записи в таблицу coffee
        cursor.execute("""
            INSERT INTO coffee (name, roast_level, ground_or_bean, description, price, package_volume)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, roast_level, ground_bean, description, price, package_volume))
        
        connection.commit()  # Сохраняем изменения
        connection.close()  # Закрываем соединение

        self.saved.emit()  # Вызываем сигнал о сохранении
        self.close()  # Закрываем форму после сохранения

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec()) 