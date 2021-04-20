liste_lettre = 'abcdefghijklmnopqrstuvwxyz'
liste_lettre = list(liste_lettre)
a,b = (3,4)
u = 0 
while (a*u)%26!=1:
        u+=1
def coder(lettre):
    y = (a*liste_lettre.index(lettre)+b)%26
    return (y,liste_lettre[y])
def decoder(lettre):
    y = liste_lettre.index(lettre)
    x = (u*y-u*b)%26
    return (x,liste_lettre[x])
mot = 'hdepu'
mot = list(mot)
mot_originel = ''
mot_originel_liste = list()
for k in mot:
    mot_originel+=decoder(k)[1]
    mot_originel_liste.append(decoder(k))
print(mot_originel, '\n', mot_originel_liste)

