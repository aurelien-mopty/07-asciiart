import sys
sys.setrecursionlimit(2000)

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
      passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    l=[]
    lst_caractere=[s[0]]
    lst_occurences=[1]
    i=1
    while i<len(s):
        if s[i]==s[i-1]:
            lst_occurences[-1]+=1
            i+=1
        else:
            lst_caractere.append(s[i])
            lst_occurences.append(1)
            i+=1
    for elt in zip(lst_caractere,lst_occurences):
        l.append(elt)
    return l


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
     passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s)==0:
        return []
    reste = artcode_r(s[1:])
    if reste and reste[0][0] == s[0]:
        caractere, occ = reste[0]
        reste[0] = (caractere, occ + 1)
        return reste
    return [(s[0], 1)] + reste

def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
