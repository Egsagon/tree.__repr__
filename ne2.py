from arbres import *
from itertools import zip_longest

class Tree(ArbreBinaire): pass

def get_height(node: Tree) -> int:
    '''
    Get the height of a tree.
    '''
    return 1 + max(get_height(node.n.g), get_height(node.n.d))


def _ascii(tree: Tree, compact = False, colorize = False) -> None:
    '''
    Ascii backend.
    '''

    height = get_height(tree)
    width = pow(2, height + 1)

    res = []
    last = None
    levels = []
    q = [(tree, 0, width, 'c')]

    while q:
        node, level, x, align = q.pop(0)

        if len(levels) <= level: levels += [[]]

        levels[level] += [[node, level, x, align]]
        seg = width // pow(2, level + 1)

        q += [[node.n.g, level + 1, x - seg, 'l']]
        q += [[node.n.d, level + 1, x + seg, 'r']]

    for i, line in enumerate(levels):
        
        pre, preline = 0, 0
        linestr, pstr = '', ''
        
        # Get padding between the 2 nodes branches
        seg = width // pow(2, i + 1)

        for node in line:

            # Get the value of the node (#TODO)
            try: valstr = str(n[0].n.r)
            except: valstr, n[3] = ' ', ''

            h = seg // 2

            # Right branch
            if n[3] == 'r':
                linestr += '*' * (n[2] - preline - 1 - seg - h)\
                         + '─' * (seg + h) + '╮'
                preline = n[2] + seg + h
            
            # Left branch
            if n[3] == 'l':
                linestr += ' ' * (n[2] - preline - 1) + '╭' \
                         + '─' * (seg + h)

            pstr += ' ' * (n[2] - pre - len(valstr)) + valstr
            pre = n[2]
        
        is_tail = False

        if last is None:
            sep = pstr.replace(valstr, '│')
            joined = ''
        
        else:
            sep = ''.join(['│' if c in '╭╮' else ' ' for c in linestr])
            joined = ''.join(['┴' if s == '│' else char if char else '*'
            for c, s in zip_longuest(linestr, last)]) + ' '
            # Adding an extra space for the nextchar replacement
        
        # Remove the stars to blanks or pipes
        for string in ''.join([c if c == '*' else ' '
        for c in joined]).split():
            char = '─' if len(string) == (seg - 1) // 2 else ' '
            joined = joined.replace(string, char * len(string), 1)

        # Pipes replacement
        old = joined_linestr
        joined = joined.replace(' ┴ ', '   ')   # no node
        joined = joined.replace(' ┴', ' ╰')     # right only
        joined = joined.replace('┴ ', '╯ ')     # left only

        if old != joined: is_tail = True

        # Print branches
        