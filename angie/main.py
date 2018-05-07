# grete.angie.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"] = 800
children = "https://i.imgur.com/4fTrn8X.jpg"
toy = "https://i.imgur.com/57cOaZ9.jpg"
sckoolhouse = "https://i.imgur.com/oXsdN2c.jpg"

def claudemilsonarevolta():
    cenasckoolhouse = Cena("https://i.imgur.com/oXsdN2c.jpg")
    chistyle = dict(left = 800, top = 10, width = 100, maxHeight = "100px")
    #chistyle.update({"max-height" = 200})
    children = Elemento("https://i.imgur.com/4fTrn8X.jpg",tit = "children",
    style=chistyle)
    txtchildren = Texto(cenasckoolhouse,"please, help me")
    children.entra(cenasckoolhouse)
    children.vai = txtchildren.vai
    cenasckoolhouse.vai()
    
    
claudemilsonarevolta()