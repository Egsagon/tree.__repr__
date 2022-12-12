class Noeud:
    genre ='noeud'
    def  __init__ (self, valeur, gauche, droit):
            self.r = valeur
            self.g = gauche
            self.d = droit
            self.racine = lambda *_: self.r

class ArbreBinaire:
    genre = 'arbre'
    def __init__ (self, c):
        self.n = c
    def creeVide():
        return ArbreBinaire(None)
    def creeNGD(valeur, gauche, droit):
        return ArbreBinaire(Noeud(valeur, gauche, droit))
    def estVide(self):
        return (self.n is None)
    def racine(self):
        assert not(self.n is None), 'Arbre vide'
        return self.n.r
    def filsGauche(self):
        # assert not(self.n is None), 'Arbre vide'
        try:
            return self.n.g
        except: pass
    
    def filsDroit(self):
        # assert not(self.n is None), 'Arbre vide'
        
        try:
            return self.n.d
        except: pass

vide = ArbreBinaire(None)

def creeFeuille(x):
    return ArbreBinaire.creeNGD(x, vide, vide)

def taille(a):
    if a.estVide():
        return 0
    else:
        return 1 + taille(a.filsGauche()) + taille(a.filsDroit())

def profondeur(a):
    if a.estVide():
        return -1
    else:
        return (1 + max(profondeur(a.filsGauche()), profondeur(a.filsDroit())))

class ABR(ArbreBinaire):
    def __init__ (self,c):
        ArbreBinaire.__init__(self,c)

    def creeNGD(valeur, gauche, droit):
        return ABR(Noeud(valeur, gauche, droit))

    def cherche(self,x):
        if ArbreBinaire.estVide(self):
            return False
        elif x == self.racine():
            return True
        elif x < self.racine():
            return self.filsGauche().cherche(x)
        else:
            return self.filsDroit().cherche(x)

    def ajoute(self,x):
        if ArbreBinaire.estVide(self):
            self.n = Noeud(x, ABR(None), ABR(None))
        elif x <= self.racine():
            self.filsGauche().ajoute(x)
        else:
            self.filsDroit().ajoute(x)

def creeFeuille(x):
    return ABR.creeNGD(x, ABR(None), ABR(None))

a1 = ArbreBinaire.creeNGD(4, ArbreBinaire.creeNGD(3, creeFeuille(1), vide), creeFeuille(6))
a2 = ArbreBinaire.creeNGD(12, ArbreBinaire.creeNGD(9, vide, creeFeuille(11)), creeFeuille(14))
a = ArbreBinaire.creeNGD(8, a1, a2)

b = ArbreBinaire.creeNGD('r',
                         ArbreBinaire.creeNGD('a',
                                              ArbreBinaire.creeNGD('c',
                                                                   vide,
                                                                   creeFeuille('h')),
                                              ArbreBinaire.creeNGD('d',
                                                                   creeFeuille('i'),
                                                                   ArbreBinaire.creeNGD('j',
                                                                                        creeFeuille('l'),
                                                                                        vide))),
                         ArbreBinaire.creeNGD('b',
                                              ArbreBinaire.creeNGD('e',
                                                                   creeFeuille('k'),
                                                                   vide),
                                              creeFeuille('f')))


c = ArbreBinaire.creeNGD('64',
                         ArbreBinaire.creeNGD('4',
                                              ArbreBinaire.creeNGD('3',
                                                                   vide,
                                                                   creeFeuille('2')),
                                              creeFeuille('5')
                                              ),
                         
                         ArbreBinaire.creeNGD('9',
                                              creeFeuille('5'),
                                              ArbreBinaire.creeNGD('12',
                                                                   creeFeuille('11'),
                                                                   creeFeuille('13'))))


d = ArbreBinaire.creeNGD('r',
                         ArbreBinaire.creeNGD('a',
                                              vide,
                                              creeFeuille('c')),
                         
                         ArbreBinaire.creeNGD('b',
                                              creeFeuille('d'),
                                              creeFeuille('e')))

e = ArbreBinaire.creeNGD('r',
                         creeFeuille('a'),
                         creeFeuille('b'))

f = ArbreBinaire.creeNGD('a',
                         ArbreBinaire.creeNGD('a',
                                              ArbreBinaire.creeNGD('a',
                                                                   ArbreBinaire.creeNGD('a',
                                                                                        ArbreBinaire.creeNGD('a', vide, vide),
                                                                                        vide),
                                                                   vide),
                                              vide),
                         vide)

g = ArbreBinaire.creeNGD('R',
                         ArbreBinaire.creeNGD('GAUCHE',
                                              vide,
                                              vide),
                         
                         ArbreBinaire.creeNGD('DROITE',
                                              vide,
                                              vide),)
# EOF