lista = [
    ["Elemento1","Elemento2","Elemento3"],
    ["Elemento1","Elemento2","Elemento3"],
    ["Elemento1","Elemento2","Elemento3"]
]

def recorre_lista(item, index):
    for x in item[index]:
        if isinstance(x,list):
            recorre_lista(x)
        else: print(x , "Lista1")

    for x in item[index+1]:
        if isinstance(x,list):
            recorre_lista(x)
        else: print("\t" , x , "Lista2")

    for x in item[index+2]:
        if isinstance(x,list):
            recorre_lista(x)
        else: print("\t\t" , x , "Lista3")

recorre_lista(lista, 0)