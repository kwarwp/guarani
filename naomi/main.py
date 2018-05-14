# grete.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, INVENTARIO, STYLE
STYLE["width"] = 800
STYLE["height"] = "600px"
MIC = "https://i.imgur.com/iqUV0yJ.jpg"
PAN = "https://i.imgur.com/NFhoyd0.jpg"
NGEO = "https://i.imgur.com/VzxARws.jpg"
LGEO = "https://i.imgur.com/zb8RS7U.jpg"
SGEO = "https://i.imgur.com/iybLHJK.jpg"
OGEO = "https://i.imgur.com/js589HB.jpg"

def geografia():
    def vai_trigo():
        from amanda.main import trigonometria
        trigonometria()
    n_geo = Cena(NGEO, meio=Cena(vai=vai_trigo))
    e_geo = Cena(LGEO, esquerda=n_geo)
    s_geo = Cena(SGEO, esquerda=e_geo)
    o_geo = Cena(OGEO, esquerda=s_geo, direita=n_geo)
    n_geo.esquerda, n_geo.direita = o_geo, e_geo
    s_geo.direita, e_geo.direita = o_geo, s_geo
    micstyle = dict(left = 610, top = 100, width = 80, maxHeight = "90px")
    panstyle = dict(left = 750, top = 110, width = 50, maxHeight = "230px")
    volcstyle = dict(left = 30, top = 500, width = 100, maxHeight = "120px")
    mic = Elemento(MIC, tit = "sweep pan", drag=True,
        style=micstyle, cena=s_geo, vai=Texto(s_geo,"please, help me, fix my name",
        foi=lambda: INVENTARIO.bota(mic)).vai)
    pan = Elemento(PAN, tit = "microscope", drag=True,
        style=panstyle, cena=e_geo, vai=Texto(e_geo,"please, help me, fix my name",
        foi=lambda: INVENTARIO.bota(pan)).vai)

    s_geo.vai()
    

if __name__ == "__main__":
    INVENTARIO.inicia()
    geografia()