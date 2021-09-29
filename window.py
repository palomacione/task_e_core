from PyQt5 import QtCore, QtGui, QtWidgets
from control import Control
from models import Person

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(160, 80, 75, 23))
        self.addButton.setObjectName("addButton")
        self.label_inserir = QtWidgets.QLabel(self.centralwidget)
        self.label_inserir.setGeometry(QtCore.QRect(160, 10, 71, 21))
        self.label_inserir.setObjectName("label_inserir")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(30, 40, 31, 16))
        self.label_nome.setObjectName("label_nome")
        self.nameText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameText.setGeometry(QtCore.QRect(70, 40, 91, 31))
        self.nameText.setObjectName("nameText")
        self.label_idade = QtWidgets.QLabel(self.centralwidget)
        self.label_idade.setGeometry(QtCore.QRect(190, 40, 31, 16))
        self.label_idade.setObjectName("label_idade")
        self.ageText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ageText.setGeometry(QtCore.QRect(230, 40, 81, 31))
        self.ageText.setObjectName("ageText")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(150, 150, 121, 141))
        self.listWidget.setObjectName("listWidget")
        self.alphaListbutton = QtWidgets.QPushButton(self.centralwidget)
        self.alphaListbutton.setGeometry(QtCore.QRect(30, 120, 171, 23))
        self.alphaListbutton.setObjectName("alphaListbutton")
        self.ageListButton = QtWidgets.QPushButton(self.centralwidget)
        self.ageListButton.setGeometry(QtCore.QRect(220, 120, 171, 23))
        self.ageListButton.setObjectName("ageListButton")
        self.label_classify = QtWidgets.QLabel(self.centralwidget)
        self.label_classify.setGeometry(QtCore.QRect(100, 300, 221, 16))
        self.label_classify.setObjectName("label_classify")
        self.listclassify = QtWidgets.QListWidget(self.centralwidget)
        self.listclassify.setGeometry(QtCore.QRect(170, 320, 131, 21))
        self.listclassify.setObjectName("listclassify")
        self.classifyButton = QtWidgets.QPushButton(self.centralwidget)
        self.classifyButton.setGeometry(QtCore.QRect(90, 320, 75, 23))
        self.classifyButton.setObjectName("classifyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.control = Control()
        self.set_actions(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pessoas"))
        self.addButton.setText(_translate("MainWindow", "Adicionar"))
        self.label_inserir.setText(_translate("MainWindow", "Inserir Pessoa"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_idade.setText(_translate("MainWindow", "Idade:"))
        self.alphaListbutton.setText(_translate("MainWindow", "Ver Lista em ordem alfabética:"))
        self.ageListButton.setText(_translate("MainWindow", "Ver Lista ordenada por idade:"))
        self.label_classify.setText(_translate("MainWindow", "Selecione uma idade da lista para classificar"))
        self.classifyButton.setText(_translate("MainWindow", "Classificar"))
    
    def set_actions(self, MainWindow):
        self.addButton.clicked.connect(self.addPerson)
        self.alphaListbutton.clicked.connect(self.showlistAlpha)
        self.ageListButton.clicked.connect(self.showlistAge)
        self.classifyButton.clicked.connect(self.showClassify)
    
    def addPerson(self):
        age = int(self.ageText.toPlainText())
        name = self.nameText.toPlainText()
        self.control.add(name, age)
        self.nameText.clear()
        self.ageText.clear()
    
    def showlistAlpha(self):
        self.listWidget.clear()
        nameList = self.control.showName()
        for i in nameList:
            item = i[0] + ", " + str(i[1])
            self.listWidget.addItem(item)

    def showlistAge(self):
        self.listWidget.clear()
        ageList = self.control.showAge()
        for i in ageList:
            item = i[0] + ", " + str(i[1])
            self.listWidget.addItem(item)
    
    def showClassify(self):
        self.listclassify.clear()
        if self.listWidget.currentItem() is None:
            print("Selecione um objeto da lista")
        else:
            name, age = self.listWidget.currentItem().text().split(",")
            person = Person(name, int(age))
            result = self.control.classify(person)
            self.listclassify.addItem(result)






