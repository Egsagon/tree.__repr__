#!/usr/bin/python3


from arbres import *

def to_json(node: ArbreBinaire) -> str:
    '''
    Converti un arbre en string json.
    '''
    
    if node is not None and not node.estVide():
        return '"' + node.racine() + '", [' + to_json(node.n.g) + to_json(node.n.d) + '], '
    
    return ''

def prefixe(node: ArbreBinaire) -> str:
    '''
    Parcours un arbre.
    '''
    
    if node is not None and not node.estVide():
        return node.racine() + prefixe(node.n.g) + prefixe(node.n.d)
    
    return ''

def postfixe(node: ArbreBinaire) -> str:
    '''
    Parcours un arbre.
    '''
    
    if node is not None and not node.estVide():    
        return prefixe(node.n.g) + prefixe(node.n.d) + node.racine()
    
    return ''

def infixe(node: ArbreBinaire) -> str:
    '''
    Parcours un arbre.
    '''
    
    if node is not None and not node.estVide():
        return prefixe(node.n.g) + node.racine() + prefixe(node.n.d)

    return ''

def largeur(parents: ArbreBinaire) -> str:
    '''
    Parcours un arbre.
    '''

    base = parents
    res = [parents.racine()]
    parents = [parents]
    p2 = []

    while 1:
        for parent in parents:
            if not parent.estVide():
                g, d = parent.filsGauche(), parent.filsDroit()
                
                if not g.estVide(): res += [g.racine()]
                if not d.estVide(): res += [d.racine()]
                p2 += [g, d]
            
            elif taille(base) == len(res): return '-'.join(res)
        
        parents = p2
        p2 = []

# EOF