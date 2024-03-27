def beolvas():
    l = []
    with open("adatok.txt", "r", encoding="utf-8") as fm:
        for sor in fm:
            l.append(float(sor.strip()))
    return l

osszegek = beolvas()