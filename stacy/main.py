# grete.stacy.main.py
# grete.sara.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
BEACH = "http://casadeluxoemcamboinhas.com.br/wp-content/uploads/2015/01/28506.jpg"
FUNNYDOG = "https://vignette.wikia.nocookie.net/steven-universe/images/0/06/Funny_dog.png/revision/latest?cb=20150717003538"
DOLLYNHO =  "https://lh3.ggpht.com/vshyoy6DTJtuLpXrqKesDJkJebNmpq7yTI-HUr7ICZ_jOe_xXBEWaGmYDrnbVDZxwA=w300"
LIXO = "http://portaljfonte.com.br/wp-content/uploads/2017/10/lixoI.jpg"

def dogatthebeach():
    beach = Cena ("http://casadeluxoemcamboinhas.com.br/wp-content/uploads/2015/01/28506.jpg")
    funnydog = Elemento("https://vignette.wikia.nocookie.net/steven-universe/images/0/06/Funny_dog.png/revision/latest?cb=20150717003538", tit = "FUNNYDOG",  style = dict(left = 25, top = 60, widht = 60, height = 25))
    txtfunnydog = Texto(beach,"Do you need dolly?")
    funnydog.entra(beach)
    funnydog.vai = txtfunnydog.vai
    beach.vai()
    lixo = Cena ("http://portaljfonte.com.br/wp-content/uploads/2017/10/lixoI.jpg")
    dollynho = Elemento("https://lh3.ggpht.com/vshyoy6DTJtuLpXrqKesDJkJebNmpq7yTI-HUr7ICZ_jOe_xXBEWaGmYDrnbVDZxwA=w300", tit = "DOLLYNHO",  style = dict(left = 25, top = 60, widht = 60, height = 25))
    txtdollynho = Texto(lixo,"who called me?")
    dollynho.entra(lixo)
    dollynho.vai = txtdollynho.vai
    beach.direita = lixo
    lixo.esquerda = beach
    lixo.vai()
    
    
dogatthebeach()