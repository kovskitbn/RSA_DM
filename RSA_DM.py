alphabet = 'abcdefghijklmnopqrstuvwxyz'
liste_lettre = list(alphabet)
cle = (3,4)
def coder(lettre):
    y = (cle[0]*liste_lettre.index(lettre)+cle[1])%26
    return (y,liste_lettre[y])
def decoder(lettre):
    y = liste_lettre.index(lettre)
    u = 0 
    while (cle[0]*u)%26!=1:
        u+=1
    x = (u*y-u*cle[1])%26
    return (x,liste_lettre[x])
mot = 'hdepu'
mot = list(mot)
mot_originel = ''
mot_originel_liste = list()
for k in mot:
    mot_originel+=decoder(k)[1]
    mot_originel_liste.append(decoder(k))
print(mot_originel, '\n', mot_originel_liste)
