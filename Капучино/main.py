import sqlite3
from PyQt6 import QtWidgets, uic
import sys

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
        self.addEditForm.show()

# New class for the add/edit form
class AddEditCoffeeForm(QtWidgets.QWidget):
    def __init__(self):
        super(AddEditCoffeeForm, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        
        # Connect save button to method
        self.saveButton.clicked.connect(self.saveCoffee)

    def saveCoffee(self):
        # Logic to save or update coffee record in the database
        # Example: get data from form fields and save to database
        name = self.nameLineEdit.text()
        # ... get other fields
        # Save to database
        print(f"Saving coffee: {name}")
        # Close the form after saving
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec()) 