# grete.kathryn.main.py
from _spy.vitollino.main import Cena,Elemento,Texto, INVENTARIO
CLASS1 = "https://i.imgur.com/KsJNT1W.jpg"
CLASS2 = "https://i.imgur.com/xJWIH1J.jpg"
CLASS3 = "https://i.imgur.com/P3iSUby.jpg"
CLASS4 = "https://i.imgur.com/m3UOcXX.jpg"
CORACAO = "https://i.imgur.com/6UKpUyW.jpg"
GLOBOS = "https://i.imgur.com/tzt1Ch4.jpg"
LEON   = "https://i.imgur.com/zUhR9wk.jpg"
def aventurasnaescola():
    class1 = Cena (img = CLASS1)
    class2 = Cena (img = CLASS2)
    class3 = Cena (img = CLASS3)
    class4 = Cena (img = CLASS4)
    coracao = Cena (img = CORACAO)
    INVENTARIO.inicia()
    class1 = Cena(class1)
    class2 = Cena(class2, esquerda=class1)
    class3 = Cena(class3, esquerda=class2)
    class4 = Cena(class4, esquerda=class3, direita=class1)
    class1.esquerda, class1.direita = class4, class2
    class3.direita, class2.direita = class4, class3
    globos = Elemento(img = GLOBOS, tit = "globos", style = dict(left = 340, top = 55, widht = 55, height = 180))
    leon = Elemento(img = LEON, tit = "leon", style = dict(left = 350, top = 60, widht = 60, height = 200))
    leon.entra(class1)
    globos.entra(class1)
    txtleon = Texto(class1,"Eu quero viajar para cÃ¡!!")
    globos.entra(class2)
    leon.entra(class2)
    txtglobos = Texto(class2,"Ei,cuidado!!")
    globos.entra(class3)
    leon.entra(class3)
    txtleon = Texto(class3,"Desculpa!!")
    globos.entra(class4)
    leon.entra(class4)
    txtglobos = Texto(class4,"Vamos ser amiguinhos?!?!")
    globos.entra(coracao)
    leon.entra(coracao)
    txtleon = Texto(coracao,"Siiiiim!!!!!")
    txtglobos = Texto(coracao,"Siiiim!!!!!")
    class1.vai()
    
aventurasnaescola()
    
     