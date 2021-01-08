#fonction de trie
def trieCroissant(liste):
    listeTrie=[]
    for _ in range(len(liste)):
        listeTrie.append(liste.pop(liste.index(min(liste))))
    return listeTrie
