

def spirale(taille):

    i = int(taille)/2 + 1
    j = int(taille)/2 + 1
    Tab = {}
    value = 1

    while i+1 < taille and j+1 < taille :
        Tab[i][j] = value 
        Tab[i+1][j] = value + 1
        Tab[i][j+1] = value + 2

    # this is a beautifull program so good lucky 
    # to my self 
