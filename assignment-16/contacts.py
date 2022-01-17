import sqlite3
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('contacts.ui')
        self.ui.show()
        self.conn = sqlite3.connect('contacts.db')
        self.cursor = self.conn.cursor()
        self.id = 0
        self.ui.themeButton.clicked.connect(self.change_theme)
        self.ui.showContactsButton.clicked.connect(self.show_data)
        self.ui.addNewContactButton.clicked.connect(self.add_new_contact)
        self.ui.deleteSpecificContactButton.clicked.connect(self.delete_contact_by_id)
        self.ui.deleteAllContactsButton.clicked.connect(self.delete_contacts)

    def change_theme(self):
        self.ui.setStyleSheet("background-color: rgb(100, 100, 100);")

    def show_data(self):
        try:
            self.cursor.execute('SELECT * FROM contacts')
            result = self.cursor.fetchall()
            for item in result:
                self.id += 1
                label = QLabel()
                label.setText(str(item[0]) + '\t' + item[1] + '\t' + item[2] + '\t' + item[3] + '\t' + item[4] + '\t' + item[5])
                self.ui.verticalLayout.addWidget(label)
        except:
            print('Check out database and make sure all the fields are filled!')

    def add_new_contact(self):
        try:
            self.id += 1
            first_name = self.ui.firstNameEdit.text()
            last_name = self.ui.lastNameEdit.text()
            phone = self.ui.phoneEdit.text()
            mobile = self.ui.mobileEdit.text()
            email = self.ui.emailEdit.text()
            self.cursor.execute(f"INSERT INTO contacts VALUES({self.id},'{first_name}','{last_name}','{phone}','{mobile}','{email}');")
            self.conn.commit()
            label = QLabel()
            label.setText(str(self.id) + '\t' + first_name + '\t' + last_name + '\t' + phone + '\t' + mobile + '\t' + email)
            self.ui.verticalLayout.addWidget(label)
        except:
            pass

    def delete_contact_by_id(self):
        id = int(self.ui.deletingIDEdit.text())
        self.cursor.execute(f"DELETE FROM contacts WHERE ID = {id};")
        self.conn.commit()
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().deleteLater()
        self.show_data()

    def delete_contacts(self):
        self.cursor.execute("DELETE FROM contacts;")
        self.conn.commit()
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().deleteLater()
        self.id = 0


if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    app.exec()
