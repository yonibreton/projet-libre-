# un mot au hasard
def word():
    import random
    liste_mot=["JAZZ","ANGLE","ARMOIRE","BANC","BUREAU","CABINET","CARREAU","CHAISE","CLASSE","CLEF","COIN","COULOIR","DOSSIER","EAU","ECOLE","ENTRER","ESCALIER","ETAGERE","EXTERIEUR","LIT","MARCHE","MATELAS"]
    print(random.choice(liste_mot))
# remplacement par des underscores
def underscore(word , L = []):
    r = ''
    for i in len(word):#jusqu'a la fin du mot aléatoires
        if i in L:#si i ets dans L
            r += i + ' '
        else:#sinon
            r += '_ '

    return r[:-1]
# choix d'une lettre
def saisie():
    lettre = input('Entrez une lettre : ')#on propose de rentrer une lettre au joueur
    if len( lettre ) > 1 or ord(lettre) < 65 or ord(lettre) > 122:
        return saisie()
    else:
        return lettre.upper()

# programme principal
lettres_deja_proposees = []#création de la liste des lettrew deja proposée
mot_a_deviner = word()
affichage = underscore( mot_a_deviner )
print( 'Mot à deviner : ' , affichage )
nb_erreurs = 0
while '_' in affichage and nb_erreurs < 11:
    lettre = saisie()
    if lettre not in lettres_deja_proposees:#si la lettres n'est pas déja proposée
        lettres_deja_proposees += [ lettre ]

    if lettre not in mot_a_deviner:#si la lettre proposée n'est pas dans le mot
        nb_erreurs += 1#ajoutée le nombre d'erreurs

    affichage = underscore( mot_a_deviner , lettres_deja_proposees )
    print('Mot à deviner : ' , 'affichage ', ' ''*10 ,' 'Nombre ''erreurs maximum :'' , 11-nb_erreurs' )