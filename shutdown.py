# importações utilizadas:
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QLineEdit, QPushButton, QCheckBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIntValidator
import os


# Classe da janela
class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()

        # Dados da tela:
        self.topo = 250
        self.esquerda = 250
        self.largura = 510
        self.altura = 250
        self.titulo = 'Liga/Desliga'
        self.setFixedSize(450, 250)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # Variaveis:
        self.OnlyInt = QIntValidator()

        # Label1:
        label1 = QLabel(self)
        label1.setText('Marque o que você deseja que seja feito:')
        label1.move(20, 10)
        label1.resize(450, 40)
        label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:black}')

        # RadioButton, opção de desligar:
        self.RbDesligar = QRadioButton(self)
        self.RbDesligar.move(30, 40)
        self.RbDesligar.resize(125, 35)
        self.RbDesligar.setText('Desligar')
        self.RbDesligar.setStyleSheet('QRadioButton {font-size:20px;color:black}')
        self.RbDesligar.clicked.connect(self.click_radiobutton)
        self.RbDesligar.setCursor(QtCore.Qt.PointingHandCursor)

        # RadioButton, opção de reiniciar:
        self.RbReiniciar = QRadioButton(self)
        self.RbReiniciar.move(150, 40)
        self.RbReiniciar.resize(125, 35)
        self.RbReiniciar.setText('Reiniciar')
        self.RbReiniciar.setStyleSheet('QRadioButton {font-size:20px;color:black}')
        self.RbReiniciar.clicked.connect(self.click_radiobutton)
        self.RbReiniciar.setCursor(QtCore.Qt.PointingHandCursor)

        # RadioButton, opção de reiniciar:
        self.RbAuxiliar = QRadioButton(self)
        self.RbAuxiliar.move(270, 40)
        self.RbAuxiliar.resize(125, 35)
        self.RbAuxiliar.setText('auxiliar')
        self.RbAuxiliar.setStyleSheet('QRadioButton {font-size:20px;color:black}')
        self.RbAuxiliar.setCursor(QtCore.Qt.PointingHandCursor)
        self.RbAuxiliar.setVisible(False)

        # EditText, caixa de texto para o tempo:
        self.EditText_Tempo = QLineEdit(self)
        self.EditText_Tempo.move(40, 85)
        self.EditText_Tempo.resize(275, 35)
        self.EditText_Tempo.setStyleSheet('QLineEdit {font-size:22px;color:black;padding-left:10px;}')
        self.EditText_Tempo.setPlaceholderText("Insira o tempo desejado:")
        self.EditText_Tempo.setValidator(self.OnlyInt)
        self.EditText_Tempo.setEnabled(False)
        self.EditText_Tempo.textChanged.connect(self.textchangedtempo)

        # Label2, erro caso tempo seja menor ou igual a 0:
        self.label2 = QLabel(self)
        self.label2.setText('tempo deve ser\n > do que 0\n (Zero)')
        self.label2.move(330, 78)
        self.label2.resize(450, 45)
        self.label2.setStyleSheet('QLabel {font:bold;font-size:12px;color:red}')
        self.label2.setVisible(False)

        # Label3:
        label3 = QLabel(self)
        label3.setText('O tempo fornecido foi em:')
        label3.move(20, 125)
        label3.resize(450, 40)
        label3.setStyleSheet('QLabel {font:bold;font-size:20px;color:black}')

        # CheckBox, seleção de que o tempo fornecido foi em segundos:
        self.CkSegundos = QCheckBox(self)
        self.CkSegundos.move(30, 155)
        self.CkSegundos.resize(125, 35)
        self.CkSegundos.setText('Segundos')
        self.CkSegundos.setStyleSheet('QCheckBox {font-size:20px;color:black}')
        self.CkSegundos.clicked.connect(self.segundosclick)
        self.CkSegundos.setEnabled(False)
        self.CkSegundos.setCursor(QtCore.Qt.PointingHandCursor)

        # CheckBox, seleção de que o tempo fornecido foi em minutos:
        self.CkMinutos = QCheckBox(self)
        self.CkMinutos.move(150, 155)
        self.CkMinutos.resize(125, 35)
        self.CkMinutos.setText('Minutos')
        self.CkMinutos.setStyleSheet('QCheckBox {font-size:20px;color:black}')
        self.CkMinutos.clicked.connect(self.minutosclick)
        self.CkMinutos.setEnabled(False)
        self.CkMinutos.setCursor(QtCore.Qt.PointingHandCursor)

        # CheckBox, seleção de que o tempo fornecido foi em horas:
        self.CkHoras = QCheckBox(self)
        self.CkHoras.move(270, 155)
        self.CkHoras.resize(125, 35)
        self.CkHoras.setText('Horas')
        self.CkHoras.setStyleSheet('QCheckBox {font-size:20px;color:black}')
        self.CkHoras.clicked.connect(self.horasclick)
        self.CkHoras.setEnabled(False)
        self.CkHoras.setCursor(QtCore.Qt.PointingHandCursor)

        # Botão, ativa a ação desejada:
        self.botao_Ativar = QPushButton('Realizar ação!', self)
        self.botao_Ativar.move(50, 195)
        self.botao_Ativar.resize(175, 40)
        self.botao_Ativar.setStyleSheet('QPushButton {background-color:#B0C4DE;font:bold;font-size:20px} '
                                        'QPushButton:hover {color:red}')
        self.botao_Ativar.setCursor(QtCore.Qt.PointingHandCursor)
        self.botao_Ativar.setEnabled(False)
        self.botao_Ativar.clicked.connect(self.realiza_acao)

        # Botão, cancela alguma ação que foi inciada:
        self.botao_Cancelar = QPushButton('CANCELAR!', self)
        self.botao_Cancelar.move(250, 195)
        self.botao_Cancelar.resize(175, 40)
        self.botao_Cancelar.setStyleSheet('QPushButton {background-color:#deb0b0;font:bold;font-size:20px} '
                                          'QPushButton:hover {color:blue}')
        self.botao_Cancelar.setCursor(QtCore.Qt.PointingHandCursor)
        self.botao_Cancelar.clicked.connect(self.cancela_acao)

        # Abre a janela
        self.loadjanela()

    # Função que Carrega a Janela:
    def loadjanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    # Funçao click, radiobuttons:
    def click_radiobutton(self):
        self.EditText_Tempo.setText("")
        self.EditText_Tempo.setEnabled(True)
        self.EditText_Tempo.setFocus()

    # Funçao click, tempo em segundos:
    def segundosclick(self):
        self.CkMinutos.setChecked(False)
        self.CkHoras.setChecked(False)
        self.ativar_desativar_btn()

    # Funçao click, tempo em minutos:
    def minutosclick(self):
        self.CkSegundos.setChecked(False)
        self.CkHoras.setChecked(False)
        self.ativar_desativar_btn()

    # Funçao click, tempo em horas:
    def horasclick(self):
        self.CkMinutos.setChecked(False)
        self.CkSegundos.setChecked(False)
        self.ativar_desativar_btn()

    # Função de ativar botão de ativar ação:
    def ativar_desativar_btn(self):
        if self.CkSegundos.isChecked() or self.CkMinutos.isChecked() or self.CkHoras.isChecked():
            self.botao_Ativar.setEnabled(True)
        else:
            self.botao_Ativar.setEnabled(False)

    # Função mudança de texto:
    def textchangedtempo(self):
        self.CkMinutos.setChecked(False)
        self.CkSegundos.setChecked(False)
        self.CkHoras.setChecked(False)
        self.botao_Ativar.setEnabled(False)
        self.EditText_Tempo.setText(self.EditText_Tempo.text().replace(".", ""))
        self.label2.setVisible(False)
        if self.EditText_Tempo.text().replace(" ", "") == "":
            self.CkMinutos.setEnabled(False)
            self.CkSegundos.setEnabled(False)
            self.CkHoras.setEnabled(False)
        else:
            self.CkMinutos.setEnabled(True)
            self.CkSegundos.setEnabled(True)
            self.CkHoras.setEnabled(True)

    # função de clique do botao que ativa a ação:
    def realiza_acao(self):
        # print("{}".format(int(self.EditText_Tempo.text())))
        tempotransformado = 0
        comando = ''
        if self.CkSegundos.isChecked():
            tempotransformado = int(self.EditText_Tempo.text()) * 1
        elif self.CkMinutos.isChecked():
            tempotransformado = int(self.EditText_Tempo.text()) * 60
        elif self.CkHoras.isChecked():
            tempotransformado = int(self.EditText_Tempo.text()) * 3600

        if tempotransformado <= 0:
            self.EditText_Tempo.setText("")
            self.EditText_Tempo.setFocus()
            self.label2.setVisible(True)
        else:
            if self.RbDesligar.isChecked():
                comando = "shutdown /s /t {}".format(tempotransformado)
            elif self.RbReiniciar.isChecked():
                comando = "shutdown /r /t {}".format(tempotransformado)
            os.system(comando)
            self.limpa()

    # função que cancela uma ação realizada:
    def cancela_acao(self):
        comando = "shutdown -a"
        os.system(comando)
        self.limpa()

    # função limpa tudo:
    def limpa(self):
        print("")
        self.RbDesligar.setChecked(False)
        self.RbReiniciar.setChecked(False)
        self.EditText_Tempo.setEnabled(False)

        self.EditText_Tempo.setText("")
        self.CkHoras.setEnabled(False)
        self.CkSegundos.setEnabled(False)
        self.CkMinutos.setEnabled(False)
        self.botao_Ativar.setEnabled(False)
        self.RbAuxiliar.setChecked(True)


# Inicialização da Tela
application = QApplication(sys.argv)
Window = Janela()
sys.exit(application.exec_())
