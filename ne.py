from arbres import *
from itertools import zip_longest

def PrintTree(root, compact = False):
    def height(root):
        return 1 + max(height(root.filsGauche()), height(root.filsDroit())) if root else -1  
    
    nlevels = height(root)
    width = pow(2, nlevels + 1)

    q = [(root, 0, width, 'c')]
    levels = []

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.filsGauche(),level+1,x-seg,'l'))
            q.append((node.filsDroit(),level+1,x+seg,'r'))

    last = None
    
    res = []
    
    for i, l in enumerate(levels):
        
        pre = 0
        preline = 0
        linestr = ''
        pstr = ''
        seg = width//(pow(2, i + 1))
        
        # NOTE seg - 1 is the len of the spaces 
        # between two branches going out from the root.
        
        for n in l:
            
            try:
                valstr = str(n[0].racine())
            
            except:
                valstr = ' '
                n[3] = ''
            
            # Right branch
            if n[3]=='r':
                
                linestr += '*' * (n[2]-preline-1-seg-seg//2) + '─' * (seg+seg//2) + '╮'
                preline = n[2]
            
            # Left branch
            if n[3]=='l':
                
               linestr += ' ' * (n[2] - preline - 1) + '╭' + '─' * (seg + seg // 2)
               preline = n[2] + seg + seg // 2
            
            pstr += ' ' * (n[2]-pre-len(valstr)) + valstr
            
            pre = n[2]
        
        is_tail = False
        
        if last is None:
            sep = pstr.replace(valstr, '│')
            joined_linestr = linestr
        
        else:
            sep = ''.join(['│' if c in '╭╮' else ' ' for c in linestr])
        
            joined_linestr = ''
            for char, charsep in zip_longest(linestr, last):
                
                if charsep == '│':
                    
                    joined_linestr += '┴'
                else:
                    joined_linestr += char if char else '*'
            
            joined_linestr += ' '
        
        stars = ''
        for c in joined_linestr:
            if c == '*': stars += '*'
            else: stars += ' '
        
        # Remove blanks
        for string in stars.split():
            char = '─' if len(string) == (seg - 1) // 2 else ' '
            joined_linestr = joined_linestr.replace(string, char * len(string), 1)
        
        # When no node
        old = joined_linestr
        joined_linestr = joined_linestr.replace(' ┴ ', '   ')
        if old != joined_linestr: is_tail = True
        
        # When only right node
        joined_linestr = joined_linestr.replace(' ┴', ' ╰')
        
        # When only left node
        joined_linestr = joined_linestr.replace('┴ ', '╯ ')
            
        # Print branches
        # print(joined_linestr)
        res += [joined_linestr]
        if not compact and last is not None:
            # print(sep)
            res += [sep]
        
        # Print nodes
        # print(pstr)
        res += [pstr]
        if not compact and not is_tail:
            # print(sep)
            res += [sep]
        
        last = sep
    
    return res

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def find_empty(arbreli: list) -> list:
    
    inv = arbreli[::-1]
    
    # TODO put same width for each line
    
    last = None
    res = []
    lgbt = len(inv) - 1
    
    for i, line in enumerate(inv):
        
        if last is None: last = line
        
        # Compare
        indexes = find(line, '│')
        
        for index in indexes:
            
            if last[index].strip() == '':
                
                res += [(lgbt - i, index)]
        
        last = line
    
    return res[::-1]

def remove_empty(raw: list, idxs: list) -> list:
    
    for line, index in idxs:
        
        l = list(raw[line])
        l[index] = ' '
        raw[line] = ''.join(l)
    
    return raw

def paint(raw: list, s = None) -> list:
    
    res = []
    
    s = s or 'abcdefghijklmnopqrstuvwxyz0123456789'
    
    for line in raw:
        line: str
        
        indexes = []
        for char in s:
            
            indexes += [(char, find(line, char))]
        
        for char, _indexes in indexes:
            
            line: list = list(line)
            
            for idx in _indexes:
                line.pop(idx)
                line.insert(idx, '\033[91m' + char + '\033[91m')
            
            line: str = ''.join(line)
        
        res += [line]
        
    return res

def display_tree(tree: ArbreBinaire, colorize = False, header = True, **kwargs) -> None:
    '''
    Prints a tree in an ascii form in the console.
    '''
    
    # Get the raw ascii tree 
    raw = PrintTree(tree, **kwargs)
    
    # Remove emtpy branches
    raw = remove_empty(raw, find_empty(raw))
    
    # TODO
    if colorize: raw = paint(raw)

    # Remove blank lines
    raw = [l for l in raw if l.strip()]
    
    # Add headers and footers
    if header:
        raw.insert(0, '')
        raw += ['']

    # Print
    print('\n'.join(raw))

# EOF