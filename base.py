from PyQt5 import uic,QtWidgets


def soma_valores():
    tela1.show()
    A = tela1.lineEdit.text()
    B = tela1.lineEdit_2.text()
    resultado = ''
    texto = 'Selecione'

    if tela1.radioButton.isChecked():
        resultado = int(A) + int(B)
        print(resultado)
        tela1.label_4.setText(f'{resultado:>7.2f}')
    elif tela1.radioButton_2.isChecked():
        resultado = int(A) / int(B)
        print(resultado)
        tela1.label_4.setText(f'{resultado:>7.2f}')
    elif tela1.radioButton_3.isChecked():
        resultado = int(A) * int(B)
        print(resultado)
        tela1.label_4.setText(f'{resultado:>7.2f}')
    elif tela1.radioButton_4.isChecked():
        resultado = int(A) - int(B)
        print(resultado)
        tela1.label_4.setText(f'{resultado:>7.2f}')
    else:
        print('Selecione')
        tela1.label_5.setText('Selecione')


app=QtWidgets.QApplication([])
tela1=uic.loadUi('tela1.ui')
tela1.pushButton.clicked.connect(soma_valores)

tela1.show()


app.exec()