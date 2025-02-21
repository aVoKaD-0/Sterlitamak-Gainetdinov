import sqlite3
from PyQt6 import QtWidgets, uic

class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        uic.loadUi('main.ui', self)
        self.load_data()

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

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec()) 