# grete.courtney.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
wardrobe = "https://i.imgur.com/FmhekcD.jpg"
toy = "https://i.imgur.com/57cOaZ9.jpg"
sckoolhouse = "https://i.imgur.com/oXsdN2c.jpg"

def claudemilsonarevolta():
    cenasckoolhouse = Cena("https://i.imgur.com/oXsdN2c.jpg")
    wardrobe = Elemento ("https://i.imgur.com/FmhekcD.jpg", tit = "toy", style = dict(left = 150, top = 60, widht = 60, height = 200))
    txtwardrobe = Texto(cenasckoolhouse,"Become Claudemilson")
    wardrobe.entra(cenasckoolhouse)
    wardrobe.vai = txtwardrobe.vai
    cenasckoolhouse.vai()
    
    
claudemilsonarevolta()

