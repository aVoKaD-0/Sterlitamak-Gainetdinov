from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddEditCoffeeForm(object):
    def setupUi(self, AddEditCoffeeForm):
        AddEditCoffeeForm.setObjectName("AddEditCoffeeForm")
        AddEditCoffeeForm.resize(300, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddEditCoffeeForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.verticalLayout.addWidget(self.nameLineEdit)
        self.roastLevelLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.roastLevelLineEdit.setObjectName("roastLevelLineEdit")
        self.verticalLayout.addWidget(self.roastLevelLineEdit)
        self.groundBeanLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.groundBeanLineEdit.setObjectName("groundBeanLineEdit")
        self.verticalLayout.addWidget(self.groundBeanLineEdit)
        self.descriptionLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.verticalLayout.addWidget(self.descriptionLineEdit)
        self.priceLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.priceLineEdit.setObjectName("priceLineEdit")
        self.verticalLayout.addWidget(self.priceLineEdit)
        self.packageVolumeLineEdit = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.packageVolumeLineEdit.setObjectName("packageVolumeLineEdit")
        self.verticalLayout.addWidget(self.packageVolumeLineEdit)
        self.saveButton = QtWidgets.QPushButton(parent=AddEditCoffeeForm)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        self.retranslateUi(AddEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(AddEditCoffeeForm)

    def retranslateUi(self, AddEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        AddEditCoffeeForm.setWindowTitle(_translate("AddEditCoffeeForm", "Добавить/Редактировать Кофе"))
        self.nameLineEdit.setPlaceholderText(_translate("AddEditCoffeeForm", "Название"))
        self.roastLevelLineEdit.setPlaceholderText(_translate("AddEditCoffeeForm", "Уровень обжарки"))
        self.groundBeanLineEdit.setPlaceholderText(_translate("AddEditCoffeeForm", "Молотый/Зерно"))
        self.descriptionLineEdit.setPlaceholderText(_translate("AddEditCoffeeForm", "Описание"))
        self.priceLineEdit.setPlaceholderText(_translate("AddEditCoffeeForm", "Цена"))
        self.packageVolumeLineEdit.setPlaceholderText(_translate("AddEditCoffeeForm", "Объем упаковки"))
        self.saveButton.setText(_translate("AddEditCoffeeForm", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddEditCoffeeForm = QtWidgets.QWidget()
    ui = Ui_AddEditCoffeeForm()
    ui.setupUi(AddEditCoffeeForm)
    AddEditCoffeeForm.show()
    sys.exit(app.exec())
