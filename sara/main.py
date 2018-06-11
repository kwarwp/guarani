# grete.sara.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
BEACH = "https://www.guiaviagensbrasil.com/imagens/bela-praia-camboinha-joao-pessoa-p"
FUNNYDOG = "http://www.instatube.com.br/wp-content/uploads/2015/08/pugs-mais-engracados-do-mundo-vi-480x293.jpg"

def dogatthebeach():
    beach = Cena ("https://www.guiaviagensbrasil.com/imagens/bela-praia-camboinha-joao-pessoa-p")
    funnydog = Elemento("http://www.instatube.com.br/wp-content/uploads/2015/08/pugs-mais-engracados-do-mundo-vi-480x293.jpg", tit = "FUNNYDOG",  style = dict(left = 150, top = 60, widht = 60, height = 200))
    txtfunnydog = Texto(cenabeach,"do you need dolly?")
    txtfunnydog.entra(cenabeach)
    funnydog.vai = txtfunnydog.vai
    cenabeach.vai()
    
    
dogatthebeach()