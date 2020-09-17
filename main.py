import datetime
import sys
import os

from PySide2 import QtWidgets, QtCore, QtSql, QtGui
from PySide2 import *
from PySide2.QtCore import QCoreApplication, QDate, QSortFilterProxyModel
from PySide2.QtGui import Qt
from PySide2.QtWidgets import *

from mailmerge import MailMerge
from pytils import dt, numeral

from dogovors import OpenDogovorsWindow
from mainWindow import Ui_MainWindow

from otherTest import *

import sqlite3 as sq

"""
Главный класс главного окна
"""
class MainApp(QtWidgets.QMainWindow, Ui_MainWindow, ExtendedComboBoxDogovor):
        ### Инициализация подключения к DB
    # def getConnections(self):
    #     sqlite_file = 'db\DataBase.db'
    #     if os.path.exists(sqlite_file):
    #         print('Норм подкл')
    #         return sqlite_file
    #
    #     else:
    #         print('File NOT exists')
    #         QMessageBox.critical(self, "Ошибка ", "Нет подключения к базе данных! \nПроверьте наличие базы данных в папке db", QMessageBox.Ok)

        ### Конструктор класса
    def __init__(self) -> object:
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        # Показать наше окно
        self.show()
        #self.fill_doc_name()
        #self.fill_uslugi()


            ### Даты (текущие)
        today = datetime.datetime.today()  # Текущая дата
        date_yer = today.strftime('%Y')
        date_mon = today.strftime('%m')
        date_day = today.strftime('%d')
        #print(numeral.in_words(14456138))

            ### Фильтрация comboBox_Documents
        string_list = ['hola muchachos', 'adios amigos', 'hello world', 'good bye']
        filter_dogovor = ExtendedComboBoxDogovor()
        filter_dogovor.addItems(string_list)



        ### Запросы к базе данных
    def querys(self, sql):
        dbName = 'db\DataBase.db'
        con = sq.connect(dbName)
        with con:
            cur = con.cursor()
            cur.execute(sql)
            res = cur.fetchall()
        if con:
            con.close()

        return res



    """
    Подготовка и печать документа word
    """
    def printToWord(self):
            ### Определение переменных для замены в word документе
        num_dogovor = self.lineEdit_NumDogovor.text() # Номер договора
        receipt = self.lineEdit_NumReceipt.text() # Номер квитанции
        fio = self.lineEdit_Fio.text() # ФИО пациента
        fio_short = self.shorten_to_initials(self.lineEdit_Fio.text()) # Фамилия и инициалы пациента
        document_name = self.comboBox_Documents.currentText() # Название документа удостоверяющего личность
        doc_number = self.lineEdit_NumDoc.text() # № документа удостоверяющего личность
        address = self.lineEdit_Address.text() # Адрес
        usluga = self.comboBox_Usluga.currentText() # Название услуги
        summ = self.lineEdit_PriceUsluga.text() # Сумма
        summ_word = numeral.in_words(int(summ)) # Сумма прописью
        date_mini = dt.ru_strftime('%d.%m.%Y') # Форматированные текущая дата 01.01.2020
        date_full = dt.ru_strftime('%d %B %Y', inflected=True) # Форматированные текущая дата 01 января 2020

            ### Формирование и сохранение документа word
        doc_name = '{}_{}_{}_{}'.format(fio, date_full, num_dogovor, receipt) # Формирование имени документа ФИО_Дата.docx
        template = r"res\usluga_template.docx"
        document = MailMerge(template)
        #print(document.get_merge_fields()) # Какие поля используются в шаблоне
        document.merge(
            num_dogovor=num_dogovor,
            receipt = receipt,
            fio=fio,
            fio_short=fio_short,
            document=document_name,
            doc_number=doc_number,
            address=address,
            usluga=usluga,
            summ=summ,
            summ_word = summ_word,
            date_full = date_full,
            date_mini = date_mini,
        )
        document.write("docx\{}.docx".format(doc_name,))
        os.startfile("docx\{}.docx".format(doc_name,)) # Запуск word документа и печать - os.startfile("res\generated_usluga.docx",  "print")

        ### Сокращенное имя (Иванов Иван Петрович -> Иванов И.П.)
    def shorten_to_initials(self, full_name):
        """u'Иванов Иван Петрович' -> u'Иванов И.П.'"""
        last, name, patronymic = full_name.split()
        return u"{last} {name[0]}.{patronymic[0]}.".format(**vars())

    def setSummaLineEdit(self):
        price = self.comboBox_Usluga.currentData()
        self.lineEdit_PriceUsluga.setText(str(price))

        ### Очистка формы
    def clearForm(self):
        self.lineEdit_Fio.clear()
        self.lineEdit_NumDoc.clear()
        self.comboBox_Documents.clear()
        self.lineEdit_Address.clear()
        self.comboBox_Usluga.clear()
        self.lineEdit_NumDogovor.clear()
        self.lineEdit_PriceUsluga.clear()
        self.lineEdit_NumReceipt.clear()

        ### Заполняем Combobox Услуги
    def fill_uslugi(self):
        querys_str = 'SELECT * FROM tbl_uslugi'
        rows = self.querys(querys_str)

        for i in range(len(rows)):
            row = rows[i]
            self.comboBox_Usluga.addItem(str(row[1]) + ' ' + str(row[2]), int(row[2]))
            # self.comboBox_Documents.itemData(row[0], QtCore.Qt.UserRole)

    #     ### Заполняем Combobox Услуги
    # def fill_uslugi(self):
    #     querys_str = 'SELECT * FROM tbl_uslugi'
    #     rows = self.querys(querys_str)
    #
    #     for i in range(len(rows)):
    #         row = rows[i]
    #         self.comboBox_Usluga.addItem(str(row[1]) + ' ' + str(row[2]), int(row[2]))
    #         # self.comboBox_Documents.itemData(row[0], QtCore.Qt.UserRole)

        ### Заполняем Combobox Документы
    def fill_doc_name(self):
        querys_str = 'SELECT * FROM tbl_documents'
        rows = self.querys(querys_str)

        for i in range(len(rows)):
            row = rows[i]
            self.comboBox_Documents.addItem(str(row[1]), int(row[0]))
            #self.comboBox_Documents.itemData(row[0], QtCore.Qt.UserRole)


        ### Тестовые сообщения
    # def text_to_label(self):
    #     fio = self.lineEdit_Fio.text()
    #     short_names = self.shorten_to_initials(fio)
    #     print(short_names)
    #     # curData = self.comboBox_Documents.currentData()
    #     # QMessageBox.critical(self, "Ошибка ",
    #     #                      str(curData) + ' - ' + str(short_names),
    #     #                      QMessageBox.Ok)

"""
Инициализация запуска приложения
"""
if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса Калькулятор, который мы создадим далее
    main = MainApp()
    # Запуск
    sys.exit(app.exec_())