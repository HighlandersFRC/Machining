import sys
import Gear_Cutting
import pyperclip
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit,\
                            QPushButton, QMessageBox, QLabel,\
                            QPlainTextEdit, QFileDialog
from PyQt5.QtCore import pyqtSlot



class GearCutterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setGeometry(300, 300, 460, 400)
        self.setWindowTitle('Gear Cutter - G Code Generator')

        self.teeth_textbox_label = QLabel(self)
        self.teeth_textbox_label.setText('Number of Teeth')
        self.teeth_textbox_label.move(20, 20)
        self.teeth_textbox_label.resize(140, 40)

        self.teeth_textbox = QLineEdit(self)
        self.teeth_textbox.move(160, 20)
        self.teeth_textbox.resize(280, 40)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        self.thickness_textbox_label = QLabel(self)
        self.thickness_textbox_label.setText('Thickness')
        self.thickness_textbox_label.move(20, 80)
        self.thickness_textbox_label.resize(140, 40)

        self.thickness_textbox = QLineEdit(self)
        self.thickness_textbox.move(160, 80)
        self.thickness_textbox.resize(280, 40)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        self.name_textbox_label = QLabel(self)
        self.name_textbox_label.setText('Program Number')
        self.name_textbox_label.move(20, 140)
        self.name_textbox_label.resize(140, 40)

        self.name_textbox = QLineEdit(self)
        self.name_textbox.move(160, 140)
        self.name_textbox.resize(280, 40)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


        self.generate = QPushButton('Generate G Code', self)
        self.generate.move(20, 200)
        self.generate.clicked.connect(self.on_generate)


        self.generate = QPushButton('Copy', self)
        self.generate.move(160, 200)
        self.generate.clicked.connect(self.on_copy)

        self.generate = QPushButton('Save', self)
        self.generate.move(300, 200)
        self.generate.clicked.connect(self.on_save)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        self.output_textbox = QPlainTextEdit(self)
        self.output_textbox.move(20, 260)
        self.output_textbox.resize(420, 120)


        self.show()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.nc)", options=options)
        if filename:
            f = open(filename, "w")
            f.write(self.code)
            f.close()

    @pyqtSlot()
    def on_generate(self):
        try:
            num_teeth = int(float(self.teeth_textbox.text()))
        except:
            QMessageBox.question(self, "", "Number of Teeth Must be an Integer", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            thickness = float(self.teeth_textbox.text())
        except:
            QMessageBox.question(self, "", "Thickness Must be an Numeric Value", QMessageBox.Ok, QMessageBox.Ok)
            return

        name = self.teeth_textbox.text()
        self.code = Gear_Cutting.generate_Gcode(num_teeth, thickness, name)
        self.output_textbox.setPlainText(self.code)
        dia = float((num_teeth + 2) / 20)
        QMessageBox.question(self, "G Code Generated", "Gear blank OD is: " + str(dia) + "\nThickness: " + str(thickness), QMessageBox.Ok, QMessageBox.Ok)


    @pyqtSlot()
    def on_copy(self):
        if(self.code != None):
            pyperclip.copy(self.code)
            QMessageBox.question(self, "", "Text Copied to Clipboard", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.question(self, "", "No G Code Generated", QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_save(self):
        if (self.code != None):
            self.saveFileDialog()
        else:
            QMessageBox.question(self, "", "No G Code Generated", QMessageBox.Ok, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GearCutterPage()
    sys.exit(app.exec_())