import turtle
from arbres import *
from ne import display_tree

class Backends:
    # Turtle backend
    def turtle_print(arbre: ArbreBinaire, taille = 50, colorset = None) -> None:
        
        # Definir les couleurs par default
        defaultset = {'bg': '#fff', 'fg': '#000', 'left': '#0f0', 'right': '#f00'}
        
        if colorset:
            colorset = {key: (colorset[key] if key in colorset.keys() else val) for key, val in defaultset.items()}
        
        else: colorset = defaultset
        
        def draw_sommet(s: str, coords: list) -> None:
            turtle.color(colorset['fg'])
            turtle.goto(*coords)
            turtle.dot(15)
            turtle.goto(coords[0], coords[1] + 10)
            turtle.write(s, font = ('Arial', 15), align = 'center')
        
        # Paramètres
        turtle.speed(0)
        sx, sy = turtle.screensize()
        turtle.bgcolor(colorset['bg'])
        turtle.color(colorset['fg'])
        turtle.hideturtle()
        turtle.width(3)
        
        start = [0, sy]
        sommets = []
        
        def dis(arbre: Noeud, coords: list, f: list = [0, 0],
                rep = None, col = None, ctx = None):
            if arbre is not None and not arbre.estVide():
                
                if col is not None: turtle.color(col)
                x, y = coords
                
                # Tracer le segment
                turtle.penup(); turtle.goto(*f)
                turtle.pendown(); turtle.goto(*coords)
                
                # Ecrire le sommet
                ctx.append([coords, arbre.racine()])

                # Recursivité
                dis(arbre.n.g, [x - taille * rep, y - taille * rep], coords, rep // 2, colorset['left'], ctx)
                dis(arbre.n.d, [x + taille * rep, y - taille * rep], coords, rep // 2, colorset['right'], ctx)
        
        # Dessiner
        dis(arbre, start, start.copy(), profondeur(b), None, sommets)
        turtle.penup()
        for cds, s in sommets: draw_sommet(s, cds)
        
        # Mainloop
        turtle.getscreen()._root.mainloop()

    # Directory backend
    def dir_print(arbre, prefix = '', is_tail = True, is_right = False, colorize = True):
        
        if arbre.estVide():
            print('Empty tree')
            return

        # Set the color of the branch based on whether it is on the left or right
        branch_color = '\033[32m' if not is_right else '\033[31m'
        if not colorize: branch_color = ''

        # Print the node value and the colored branch
        print(prefix + ('└── ' if is_tail else '├── ') + branch_color +  str(arbre.racine()) + ('\033[0m' if colorize else ''))
        
        left_tree, right_tree = arbre.filsGauche(), arbre.filsDroit()
        last_branch = False

        if right_tree.estVide() and left_tree.estVide():
            last_branch = True

        if not left_tree.estVide():
            Backends.dir_print(left_tree, prefix + ("    " if is_tail else "│   "), last_branch, False, colorize)

        if not right_tree.estVide():
            Backends.dir_print(right_tree, prefix + ("    " if is_tail else "│   "), True, True, colorize)

    # Ascii backend (ChatGPT)
    def ascii_print(tree, depth = 0):
        
        if tree.estVide(): return

        print('    ' * depth + tree.racine())
        
        Backends.ascii_print(tree.filsGauche(), depth + 1)
        Backends.ascii_print(tree.filsDroit(), depth + 1)

    # Better ascii backend
    ascii2_print = display_tree

def repr_arbre(arbre: ArbreBinaire, backend: str = 'ascii', **args) -> None:
    '''
    Créée une représentation d'un arbre.
    
    Backends possibles:
        turtle  ->  Dessine dans une fenetre tk avec le module turtle.
        ascii   ->  Dessine de manière primitive dans la console.
        dir     ->  Dessine avec un style de représentation de fichier.
    
    Arguments:
        arbre   ->  L'arbre à utiliser.
        backend ->  La backend à utiliser.
        **args  ->  Arguments communiqués à la backend.
    '''
    
    if not backend in ['turtle', 'ascii', 'dir', 'ascii2']:
        raise Exception(f'Mauvaise backend: {backend}.')
    
    return eval(f'Backends.{backend}_print')(arbre, **args)

# Exemples
# repr_arbre(b, 'turtle')
# repr_arbre(b, 'dir')
# repr_arbre(b, 'ascii')
repr_arbre(b, 'ascii2')

# TODO
# - ascii2 ne marche pas si la racine prend plus d'un charactere
# - (**)colorize de ascii2 ne fonctionne pas