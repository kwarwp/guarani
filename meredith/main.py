from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

A_NORTE = "https://i.imgur.com/aLEjWgB.png"
A_LESTE = "https://i.imgur.com/sivjAnO.png"
A_SUL = "https://i.imgur.com/otHJhF0.png"

B_NORTE = "https://i.imgur.com/40K5493.png"
B_LESTE = "https://i.imgur.com/R3bpFXD.png"
B_OESTE = "https://i.imgur.com/dlxY8hi.png"
B_SUL = "https://i.imgur.com/eYM3Yp9.png"

C_LESTE = "https://i.imgur.com/94V79TA.png"
C_NORTE = "https://i.imgur.com/YJfnhy9.png"
C_OESTE = "https://i.imgur.com/Fzz2FNz.png"
C_SUL = "https://i.imgur.com/LFKXlB1.png"

D_NORTE = "http://i.imgur.com/1uWH7rU.png"
D_LESTE = "https://i.imgur.com/b0FcjLq.png"
D_OESTE = "https://i.imgur.com/406g75C.png"
D_SUL = "https://i.imgur.com/HQBtUoQ.png"

H_NORTE = "https://i.imgur.com/WjTtZPn.png"
H_LESTE = "https://i.imgur.com/AzvB8hs.png"
H_OESTE = "https://i.imgur.com/SIhLGCP.png"
H_SUL = "https://i.imgur.com/UVnpzzE.png"

I_NORTE= "https://i.imgur.com/RSdQSH1.png"
I_SUL = "https://i.imgur.com/UGCRJ0d.png"
I_LESTE = "https://i.imgur.com/jSn4zsl.png"
I_OESTE= "https://i.imgur.com/eG43vn5.png"

J_NORTE= "https://i.imgur.com/MMO11Dv.png"
J_SUL = "https://i.imgur.com/RkWPb8Z.png"
J_LESTE = "https://i.imgur.com/btv0qfO.png"
J_OESTE= "https://i.imgur.com/lDezYKu.png"

E_NORTE= "https://i.imgur.com/uNkTVGg.png"
E_SUL = "http://i.imgur.com/bculg4O.png"
E_LESTE = "https://i.imgur.com/lUi1E1v.png"
E_OESTE = "https://i.imgur.com/bPBT1d7.png"

K_NORTE= "https://i.imgur.com/Tx9Q6vW.png"
K_SUL = "https://i.imgur.com/rrI94Xh.png"
K_LESTE = "https://i.imgur.com/R6gON2E.png"
K_OESTE= "https://i.imgur.com/Mn69uua.png"

L_NORTE= "https://i.imgur.com/oAu9lkN.png"
L_SUL = "https://i.imgur.com/xTjd7UV.png"
L_LESTE = "https://i.imgur.com/JMQAGvc.png"
L_OESTE = "http://i.imgur.com/UJBMKY7.png"

BATATA = "http://www.dinaarmarinhos.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/f/u/furador-gigante-escalope-retangulo-sku-52354-f1.png"
TRANSPARENTE = "http://photobucket.com/gallery/http://s718.photobucket.com/user/2pherman/media/transparent.png.html"
CHAVE = "http://i.imgur.com/V0FeZZK.png"
FOLHANGUE = "http://static.tvtropes.org/pmwiki/pub/images/bloodstainednote_1441.png"
CARTA = "https://uploads.spiritfanfics.com/fanfics/historias/201510/fanfiction-originais-minha-carta-de-suicidio-4717938-170420161737.jpg"
PANO = "http://www.removermanchas.net/wp-content/uploads/2012/11/Remover-nodoa-sangue-seco.jpg"


def criarsalas():
 a_norte = Cena(img=A_NORTE)
 a_leste = Cena(img=A_LESTE, esquerda=a_norte)
 a_sul = Cena(img=A_SUL, esquerda=a_leste)
 a_norte.direita = a_leste
 a_leste.direita = a_sul
 b_leste = Cena(img=B_LESTE)
 a_leste.meio = b_leste
    
 b_norte = Cena(img=B_NORTE)
 b_sul = Cena(img=B_SUL, esquerda=b_leste)
 b_oeste = Cena(img=B_OESTE, esquerda=b_sul, direita=b_norte)
 b_norte.direita = b_leste
 b_norte.esquerda = b_oeste   
 b_leste.direita = b_sul
 b_leste.esquerda = b_norte
 b_sul.direita = b_oeste
 b_oeste.meio = a_leste
 c_leste= Cena(img=C_LESTE)
 b_leste.meio = c_leste
 
 c_norte = Cena(img=C_NORTE)
 c_sul = Cena(img=C_SUL, esquerda=c_leste)
 c_oeste = Cena(img=C_OESTE, esquerda=c_sul, direita=c_norte)
 c_norte.direita = c_leste
 c_norte.esquerda = c_oeste   
 c_leste.direita = c_sul
 c_leste.esquerda = c_norte
 c_sul.direita = c_oeste
 c_oeste.meio = b_oeste
 d_sul = Cena(img=D_SUL)
 c_sul.meio = d_sul
 
 bau = Elemento(img=TRANSPARENTE, tit="bau misterioso", style=dict(left=150, top=160, width=60, height=30))
 bau.entra(c_leste)
 cbau = Texto(c_leste, "A morte estÃ¡ prÃ³xima")
 #inv.bota(bau, "bau", vai.vai)
 bau.vai = cbau.vai
 
 d_norte = Cena(img=D_NORTE)
 d_leste = Cena(img=D_LESTE, esquerda=d_norte, direita=d_sul)
 d_oeste = Cena(img=D_OESTE, esquerda=d_sul, direita=d_norte)
 d_norte.direita = d_leste
 d_norte.esquerda = d_oeste   
 d_norte.meio = c_norte
 d_norte.direita = d_leste
 d_norte.esquerda = d_oeste
 d_sul.direita = d_oeste
 d_sul.esquerda = d_leste
 h_sul = Cena(img=H_SUL)
 d_sul.meio = h_sul
 
 h_norte = Cena(img=H_NORTE)
 h_leste = Cena(img=H_LESTE, direita=h_sul, esquerda=h_norte)
 h_oeste = Cena(img=H_OESTE, esquerda=h_sul, direita=h_norte)
 h_norte.direita = h_leste
 h_norte.esquerda = h_oeste
 h_sul.direita = h_oeste
 h_sul.esquerda = h_leste
 h_norte.meio = d_norte
 i_leste = Cena(img=I_LESTE)
 h_leste.meio = i_leste
 
 chave = Elemento(img=CHAVE, tit="chave", style=dict(left=200, top=180, width=30, height=15))
 chave.entra(h_leste)
 cchave = Texto(h_leste, "NÃ£o sei o que abre")
 chave.vai = cchave.vai
 
 sangue = Elemento(img=TRANSPARENTE, tit="sangue", style=dict(left=80, top=230, width=25, height=15))
 sangue.entra(h_sul)
 vai = Texto(h_sul, "Nossa, quanto sangue")
 sangue.vai = vai.vai
  
 espada = Elemento(img=TRANSPARENTE, tit="espada", style=dict(left=0, top=60, width=70, height=200))
 espada.entra(h_leste)
 vai = Texto(h_leste, "A espada foi criada no ano I a.C. e Ã© uma Ã³tima arma para causar ferimentos")
 espada.vai = vai.vai
 
 i_oeste = Cena(img=I_OESTE)
 i_norte = Cena(img=I_NORTE, direita = i_leste, esquerda = i_oeste)
 i_sul = Cena(img=I_SUL, direita = i_oeste, esquerda = i_leste)
 i_oeste.direita = i_norte
 i_oeste.esquerda = i_sul
 i_leste.direita = i_sul
 i_leste.esquerda = i_norte
 j_leste = Cena(img=J_LESTE)
 i_leste.meio = j_leste
 i_oeste.meio = h_oeste
 
 folhangue = Elemento(img=FOLHANGUE, tit="papel", style=dict(left=100, top=200, width=40, height=25))
 folhangue.entra(i_leste)
 vai = Texto(i_leste, "As manchas de sangue impedem de ler tudo! PorÃ©m vocÃª consegue ler 'SOCORRO! AlguÃ©m...'")
 folhangue.vai = vai.vai
 
 j_oeste = Cena(img=J_OESTE)
 j_norte = Cena(img=J_NORTE, direita = j_leste, esquerda = j_oeste)
 j_sul = Cena(img=J_SUL, direita = j_oeste, esquerda = j_leste)
 j_oeste.direita = j_norte
 j_oeste.esquerda = j_sul
 j_leste.direita = j_sul
 j_leste.esquerda = j_norte
 j_oeste.meio = i_oeste
 e_norte = Cena(img=E_NORTE)
 j_norte.meio = e_norte
 k_leste = Cena(img=K_LESTE)
 j_leste.meio = k_leste
 saidabloq = Elemento(img=TRANSPARENTE, tit="saida bloqueada", style=dict(left=100, top=100, width=150, height=200))
 saidabloq.entra(j_sul)
 vai = Texto(j_sul, "Esta saÃ­da estÃ¡ bloqueada")
 saidabloq.vai = vai.vai
 
 e_oeste = Cena(img=E_OESTE, direita=e_norte)
 e_leste = Cena(img=E_LESTE, esquerda=e_norte)
 e_sul = Cena(img=E_SUL, esquerda=e_leste, direita=e_oeste)
 e_oeste.esquerda = e_sul
 e_leste.direita = e_sul
 e_norte.direita = e_leste
 e_norte.esquerda = e_oeste
 e_sul.meio = j_sul
 
 carta = Elemento(img=CARTA, tit="carta", style=dict(left=200, top=115, width=50, height=10))
 carta.entra(e_oeste)
 vai = Texto(e_oeste, "A vida nÃ£o Ã© boa mais. NÃ£o hÃ¡ esperanÃ§a. Adeus, mundo cruel!")
 carta.vai = vai.vai
 
 k_oeste = Cena(img=K_OESTE)
 k_sul = Cena(img=K_SUL, esquerda=k_leste, direita=k_oeste)
 k_norte = Cena(img=K_NORTE, esquerda=k_oeste, direita=k_leste)
 k_oeste.direita = k_norte
 k_oeste.esquerda = k_sul
 k_leste.direita = k_sul
 k_leste.esquerda = k_norte
 k_oeste.meio = j_oeste
 l_leste = Cena(img=L_LESTE)
 k_leste.meio = l_leste
 
 pano = Elemento(img=PANO, tit="pano", style=dict(left=170, top=230, width=40, height=10))
 pano.entra(k_norte)
 vai = Texto(k_norte, "O pano estÃ¡ cheio de sangue")
 pano.vai = vai.vai
 
 
 a_leste.vai()
 
criarsalas()