# grete.courtney.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"] = 800
children = "https://i.imgur.com/4fTrn8X.jpg"
toy = "https://i.imgur.com/57cOaZ9.jpg"
sckoolhouse = "https://i.imgur.com/oXsdN2c.jpg"

def claudemilsonarevolta():
    cenasckoolhouse = Cena("https://i.imgur.com/oXsdN2c.jpg")
    children = Elemento("https://i.imgur.com/4fTrn8X.jpg", tit = "children", style = dict(left = 825, top = 10, widht = 60, height = 200))
    txtchildren = Texto(cenasckoolhouse,"please, help me")
    children.entra(cenasckoolhouse)
    children.vai = txtchildren.vai
    cenasckoolhouse.vai()
    
    
claudemilsonarevolta()