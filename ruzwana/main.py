# grete.ruzwana.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]=800
ZOO = "https://i2.wp.com/ckturistando.com.br/wp-content/uploads/2015/11/zoologico-de-sao-paulo-ckturistando.png?w=1140"
DOG = "https://pbs.twimg.com/media/DZYLDTIXkAECOli.jpg"
COOL_PENGUIN = "https://png.pngtree.com/element_origin_min_pic/16/06/03/20575177bbcf1f9.jpg"
PROF_CARLO = "https://0.academia-photos.com/21882/7290/6975/s200_carlo_emmanoel.tolla_de_oliveira.jpg"

def adventureatthezoo():
    zoo = Cena (img = ZOO)
    dog = Elemento(img = DOG, tit = "dog", style = dict(left = 350, top = 60, widht = 60, height = 200))
    cool_penguin = Elemento(img = COOL_PENGUIN, tit = "cool_penguin", style = dict(left = 10, top = 160, widht = 60, height = 200)) 
    prof_carlo = Elemento(img = PROF_CARLO, tit = "prof_carlo", style = dict(left = 650, top = 60, widht = 60, height = 200))
    txtdog = Texto(zoo,"essa girafa está me engolindo!")
    txtcool_penguin = Texto(zoo,"eu going to salvar you!")
    txtprof_carlo = Texto(zoo," Seu pinguim pamonha! Não presta atenption na class!")
    dog.entra(zoo)
    cool_penguin.entra(zoo)
    prof_carlo.entra(zoo)
    dog.vai = txtdog.vai
    cool_penguin.vai = txtcool_penguin.vai
    prof_carlo.vai = txtprof_carlo.vai
    zoo.vai()
    
    
adventureatthezoo()
