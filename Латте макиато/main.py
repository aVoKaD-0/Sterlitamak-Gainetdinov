import sys
import os
import sqlite3
from PyQt6 import QtWidgets

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
    def __init__(self):
        super(AddEditCoffeeForm, self).__init__()
        self.setupUi(self)  
        
        self.saveButton.clicked.connect(self.saveCoffee)

    def saveCoffee(self):
        name = self.nameLineEdit.text()
        print(f"Saving coffee: {name}")
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec()) 