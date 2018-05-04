# grete.ruzwana.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
ZOO = "https://i2.wp.com/ckturistando.com.br/wp-content/uploads/2015/11/zoologico-de-sao-paulo-ckturistando.png?w=1140"
DOG = "https://pbs.twimg.com/media/DZYLDTIXkAECOli.jpg"

def adventureatthezoo():
    zoo = Cena (img = ZOO)
    dog = Elemento(img = DOG, tit = "dog", style = dict(left = 150, top = 60, widht = 60, height = 200))
    txtdog = Texto(zoo,"essa girafa está me engolindo")
    txtdog.entra(zoo)
    dog.vai = txtdog.vai
    zoo.vai()
    
    
adventureatthezoo()
