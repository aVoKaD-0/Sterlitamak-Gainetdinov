import sqlite3
from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtCore import pyqtSignal

class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        uic.loadUi('main.ui', self)
        self.load_data()
        
        # Connect buttons to methods
        self.addButton.clicked.connect(self.openAddEditForm)
        self.editButton.clicked.connect(self.openAddEditForm)

    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        connection.close()

        # Получаем ссылку на виджет таблицы
        table_widget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        
        # Устанавливаем количество строк в таблице
        table_widget.setRowCount(len(rows))
        table_widget.setColumnCount(7)  # Убедитесь, что количество столбцов соответствует количеству полей

        # Заполняем таблицу данными
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                table_widget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(data)))

    def openAddEditForm(self):
        self.addEditForm = AddEditCoffeeForm()
        self.addEditForm.saved.connect(self.load_data)  # Подключаем сигнал
        self.addEditForm.show()

# New class for the add/edit form
class AddEditCoffeeForm(QtWidgets.QWidget):
    saved = pyqtSignal()  # Определяем сигнал

    def __init__(self):
        super(AddEditCoffeeForm, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        
        # Connect save button to method
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
        connection = sqlite3.connect('coffee.sqlite')
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