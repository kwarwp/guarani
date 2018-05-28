# grete.courtney.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO
STYLE["width"] = 800
STYLE["height"] = "600px"
children = "https://i.imgur.com/4fTrn8X.jpg"
schoolhouse_n = "https://i.imgur.com/F8vDljG.jpg"
schoolhouse_o = "https://i.imgur.com/VvB1JWN.jpg"
schoolhouse_s = "https://i.imgur.com/A0CmC45.jpg"
schoolhouse_l = "https://i.imgur.com/wu3DN2C.jpg"

def claudemilsonarevolta():
    def vai_sckoolhouse():
        from naomi.main import geografia
        geografia()
        INVENTARIO.inicia()
    n_schoolhouse = Cena(sckoolhouse_n)
    e_schoolhouse = Cena(sckoolhouse_e, esquerda=n_sckoolhouse)
    s_schoolhouse = Cena(sckoolhouse_s, esquerda=e_sckoolhouse, meio=Cena(vai=vai_geo))
    o_sckoolhouse = Cena(sckoolhouse_o, esquerda=s_sckoolhouse, direita=n_sckoolhouse)
    n_sckoolhouse.esquerda, n_sckoolhouse.direita = o_sckoolhouse, e_sckoolhouse
    s_sckoolhouse.direita,e_sckoolhouse.direita = o_sckoolhouse, s_sckoolhouse
    from naomi.main import Elemento