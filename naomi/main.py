# grete.naomi.main.py
from _spy.vitollino.main import Cena,Texto, INVENTARIO, STYLE, PSTYLE, EIMGSTY, ESTYLE
from _spy.vitollino.main import Elemento as Element
from browser import html, alert, doc
STYLE["width"] = 800
STYLE["height"] = "600px"
MIC = "https://i.imgur.com/iqUV0yJ.jpg"
PAN = "https://i.imgur.com/NFhoyd0.jpg"
NGEO = "https://i.imgur.com/VzxARws.jpg"
LGEO = "https://i.imgur.com/zb8RS7U.jpg"
SGEO = "https://i.imgur.com/iybLHJK.jpg"
OGEO = "https://i.imgur.com/js589HB.jpg"
CORRECT = "My correct name: {}"
class Elemento(Element):

    def __init__(self, img="", vai=None, style={}, tit="", alt="",
            x=0, y=0, w=100, h=100, texto='',
            cena=INVENTARIO, score={}, drag=False, drop='', **kwargs):
        self._auto_score = self.score if score else self._auto_score
        self.img, self.title, self.real = img, tit, drop
        self._drag = self._over = self._drop = self._dover = self.vai = lambda *_: None
        self.cena = cena
        self.opacity = 0
        self.texto=texto
        self.vai = Texto(cena,texto, foi=self.foi ).vai if texto else vai if vai else self.vai
        # height = style["height"] if "height" in style else style["maxHeight"] if "maxHeigth" in style else 100
        # height = height[:-2] if isinstance(height, str) and "px" in height else height
        self.style = dict(**PSTYLE)
        self.style.update(**{'position': 'absolute', 'overflow': 'hidden',
                    'left': x, 'top': y, 'width':'{}px'.format(w), 'height':'{}px'.format(h),
                    'background-image': 'url({})'.format(img),
                    'background-position': '{} {}'.format(0, 0),
                    'background-size': '{}px {}px'.format(w, h)
        })
        # self.style["min-width"], self.style["min-height"] = w, h
        self.style.update(**style)
        self.elt = html.DIV(Id=tit+drop, title=tit, style=self.style)
        self.xy = (-111, -111)
        self.scorer = dict(ponto=1, valor=cena.nome, carta=tit or img, casa=self.xy, move=None)
        self.scorer.update(score)
        if False:
            self.img = html.IMG(Id="img_"+tit, src=img, title=tit, alt=alt, style=EIMGSTY)  # width=self.style["width"])
            self.elt <= self.img
        self.elt.onclick = self._click
        self.c(**kwargs)
        #_ = Dragger(self.elt) if drag else None
        #_ = Droppable(self.elt, drop, self.vai) if drop else None
        _ = self.entra(cena) if cena and (cena != INVENTARIO) else None
        self.elt.ondragstart = lambda ev: self._drag(ev)
        self.elt.onmouseover = lambda ev: self._over(ev)
        self.elt.ondrop = lambda ev: self._drop(ev)
        self.elt.ondragover = lambda ev: self._dover(ev)
        #self.img.onmousedown = self.img_prevent
        self.do_drag(drag)
        self.do_drop(drop)
        
    def foi(self):
        #mic.entra(INVENTARIO)
        item_img = self.elt
        #style = dict(item_img.style)
        style = {'opacity': "inherited", 'width': 30, 'height': "30px", 'min-height': '30px', 'float': 'left',
'position': 'unset', 'overflow': 'hidden',
                    'background-image': 'url({})'.format(self.img),
                    'background-position': '{} {}'.format(0, 0),
                    'background-size': '{}px {}px'.format(30, 20),
        }
        #item_img.style = style
        #INVENTARIO.bota(mic)
        self.do_drag(False)
        Texto(self.cena,"Finally,got my correct name: {}".format(self.tit)).vai()
        _texto = self.texto if self.tit == self.title else CORRETO.format(self.tit)
        self.vai = Texto(self.cena, _texto).vai

        clone_mic = Elemento(self.img, tit = self.title, drag=True, style=style, cena=INVENTARIO)
        clone_mic.entra(INVENTARIO)

    @property
    def tit(self):
        return self.elt.title

    @tit.setter
    def tit(self, texto):
        self.elt.title = texto

    def do_texto(self):
        self.texto = Texto(self.cena, texto, foi=self.foi)

    def img_prevent(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        return False

    def mouse_over(self, ev):
        #ev.preventDefault()
        ev.target.style.cursor = "pointer"
        return False

    def img_drag_start(self, ev):
        #ev.preventDefault()
        ev.stopPropagation()
        return False

    def drag_start(self, ev):
        #ev.preventDefault()
        ev.stopPropagation()
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'
        return False
        
    def do_drag(self, drag=True):
        self.elt.draggable = drag
        if drag:
            self._drag = self.drag_start
            self._over = self.mouse_over
        else:
            self._drag = self._over = lambda *_: None
        
    def do_drop(self, drop=True):
        if drop:
            self._drop = self.drop
            self._dover = self.drag_over
        else:
            self._drop = self._dover = lambda *_: None
        

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()
        return False

    def drop(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        src_id = ev.data['text']
        tit = doc[src_id].title
        if tit != self.real:
            Texto(self.cena,"Hey, this is not my name: {}".format(tit)).vai()
            return False
        self.tit = tit
        Texto(self.cena,"Finally, my correct name: {}".format(self.tit), foi=self.foi).vai()
        self.vai = Texto(self.cena, CORRECT.format(self.tit) ).vai
        doc[src_id].remove()

def geografia(oeste=False):
    def mic_foi():
        #mic.entra(INVENTARIO)
        item_img = mic.elt
        #style = dict(item_img.style)
        style = {'opacity': "inherited", 'width': 30, 'height': "30px", 'min-height': '30px', 'float': 'left',
'position': 'unset', 'overflow': 'hidden',
                    'background-image': 'url({})'.format(mic.img),
                    'background-position': '{} {}'.format(0, 0),
                    'background-size': '{}px {}px'.format(30, 20),
        }
        #item_img.style = style
        #INVENTARIO.bota(mic)
        mic.do_drag(True)    
        clone_mic = Elemento(MIC, tit = "sweep pan", drag=True, style=style, cena=INVENTARIO)
        clone_mic.entra(INVENTARIO)
        
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
    '''
    mic = Elemento(MIC, tit = "sweep pan", drag=False,
        x = 610, y = 100, w = 80, h = 90,
        cena=s_geo, vai=lambda *_: Texto(s_geo,"please, help me, fix my name",
        foi=mic.foi ).vai() )
    pan = Elemento(PAN, tit = "microscope", drag=False, drop="sweep pan",
        x = 750, y = 110, w = 50, h = 230,
        style=panstyle, cena=e_geo, vai=Texto(e_geo,"please, help me, fix my name",
        foi=lambda *_: INVENTARIO.bota(pan)).vai)
    '''
    mic = Elemento(MIC, tit = "sweep pan", drag=False, drop="microscope",
        x = 610, y = 100, w = 80, h = 90,
        cena=s_geo, texto = "please, help me, fix my name")
    #mic.do_drag(False)
    pan = Elemento(PAN, tit = "microscope", drag=False, drop="sweep pan",
        x = 750, y = 110, w = 50, h = 230,
        style=panstyle, cena=e_geo, texto="please, help me, fix my name")
    

    o_geo.vai() if oeste else s_geo.vai()
    
def geo_oeste():
    geografia(oeste=True)
    
    

if __name__ == "__main__":
    INVENTARIO.inicia()
    geografia()