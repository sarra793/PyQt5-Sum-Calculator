from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def play():
    a=windows.x.text()
    b=windows.y.text()
    if a=="" or not a.isdecimal():
        windows.r.setText("verif champ 1")
    elif b=="" or not b.isdecimal():
        windows.r.setText("verif champ 2")
    else:
        x=int(a)
        y=int(b)
        s=somme(x,y)
        ch=a+"+"+b+"="+str(s)
        windows.r.setText(ch) 
        tt=windows.h.toPlainText()
        if tt=="":
            tt+=ch
        else:
            tt=tt+"\n"+ch
        windows.h.setText(tt)
def somme(x,y):
    return x+y
def retablir():
    windows.x.clear()
    windows.y.clear()
    windows.r.clear()
    windows.h.clear()
    
app = QApplication([])
windows = loadUi("somme.ui")
windows.show()
windows.bt1.clicked.connect(play)
windows.bt2.clicked.connect(retablir)
app.exec_()