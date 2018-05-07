# grete.libby.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
CAMPO = "https://image.freepik.com/fotos-gratis/paisagem-de-campo-de-golfe_1388-96.jpg"
CASAL = "https://www.temporadalivre.com/blog/wp-content/uploads/casal-sem-crise-10-dicas-que-o-casal-necessita-para-ser-feliz.jpg"

def boyfriendsatthecamp():
    campo = Cena (img = CAMPO)
    casal = Elemento(img = CASAL, tit = "casal", style = dict(left = 150, top = 60, height = 200))
    txtcasal = Texto(casal,"let's eat something!")
    casal.entra(campo)
    casal.vai = txtcasal.vai
    campo.vai()
    
    
boyfriendsatthecamp()