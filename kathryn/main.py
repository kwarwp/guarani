# grete.kathryn.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
CLASS1 = "https://i.imgur.com/KsJNT1W.jpg"
CLASS2 = "https://i.imgur.com/xJWIH1J.jpg"
CLASS3 = "https://i.imgur.com/P3iSUby.jpg"
CLASS4 = "https://i.imgur.com/m3UOcXX.jpg"
GLOBOS = "https://i.imgur.com/tzt1Ch4.jpg"
LEON   = "https://i.imgur.com/zUhR9wk.jpg"
def aventurasnaescola():
    class1 = Cena (img = CLASS1)
    class2 = Cena (img = CLASS2)
    class3 = Cena (img = CLASS3)
    class4 = Cena (img = CLASS4)
    globos = Elemento(img = GLOBOS, tit = "globos", style = dict(left = 340, top = 55, widht = 55, height = 180))
    leon = Elemento(img = LEON, tit = "leon", style = dict(left = 350, top = 60, widht = 60, height = 200))
    txtleon = Texto(class1,"Eu quero viajar para cá")