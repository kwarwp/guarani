# grete.courtney.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO
STYLE["width"] = 800
STYLE["height"] = "600px"
children = "https://i.imgur.com/4fTrn8X.jpg"
schoolhouse_n = "https://i.imgur.com/F8vDljG.jpg"
schoolhouse_o = "https://i.imgur.com/Cy3pV4j.jpg"
schoolhouse_s = "https://i.imgur.com/A0CmC45.jpg"
schoolhouse_l = "https://i.imgur.com/wu3DN2C.jpg"

def claudemilsonarevolta():
    def vai_sckoolhouse():
        from naomi.main import geografia
        geografia()
        INVENTARIO.inicia()
    n_schoolhouse = Cena(schoolhouse_n)
    e_schoolhouse = Cena(schoolhouse_l, esquerda=n_schoolhouse)
    s_schoolhouse = Cena(schoolhouse_s, esquerda=e_schoolhouse)
    o_schoolhouse = Cena(schoolhouse_o, esquerda=s_schoolhouse, direita=n_schoolhouse)
    n_schoolhouse.esquerda, n_schoolhouse.direita = o_schoolhouse, e_schoolhouse
    s_schoolhouse.direita,e_schoolhouse.direita = o_schoolhouse, s_schoolhouse
    from naomi.main import Elemento
    n_schoolhouse.vai()
    
claudemilsonarevolta()