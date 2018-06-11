# grete.angie.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"] = 800
children = "https://i.imgur.com/4fTrn8X.jpg"
toy = "https://i.imgur.com/57cOaZ9.jpg"
sckoolhouse = "https://i.imgur.com/oXsdN2c.jpg"
leyden  = "https://i.imgur.com/abeXKwL.jpg"
volcano  = "https://i.imgur.com/4Y5aie8.jpg"
globe  = "https://i.imgur.com/EQtHzod.jpg"
ball  = "https://i.imgur.com/rBbRsFU.jpg"
trig_s  = "https://i.imgur.com/9ZcjTjb.jpg"
trig_o  = "https://i.imgur.com/SyHdvjw.jpg"
trig_n  = "https://i.imgur.com/ChRcEvB.jpg"
trig_e  = "https://i.imgur.com/JD6oGRg.jpg"

def trigonometria():
    n_trig = Cena(trig_n)
    e_trig = Cena(trig_e, esquerda=n_trig)
    s_trig = Cena(trig_s, esquerda=e_trig)
    o_trig = Cena(trig_o, esquerda=s_trig, direita=n_trig)
    n_trig.esquerda, n_trig.direita = o_trig, e_trig
    s_trig.direita, e_trig.direita = o_trig, s_trig
    chistyle = dict(left = 610, top = 90, width = 80, maxHeight = "80px")
    #chistyle.update({"max-height" = 200})
    vdgball = Elemento(ball,tit = "earth globe",
    style=chistyle)
    txtchildren = Texto(n_trig,"please, help me")
    vdgball.entra(e_trig)
    vdgball.vai = txtchildren.vai
    e_trig.vai()
    
    
trigonometria()