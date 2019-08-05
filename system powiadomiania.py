def ile(lista):
    licznik = 0
    rozpatrzone = []
    for i in lista:
        if i not in rozpatrzone:
            rozpatrzone.append(i)
            wsk = lista[i-1]
            while wsk != i:
                rozpatrzone.append(wsk)
                wsk = lista[wsk-1]
            licznik = licznik + 1
    return licznik 
