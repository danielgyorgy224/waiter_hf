# alprogram
def beolvas():
    l = []
    with open("adatok.txt", "r", encoding="utf-8") as fm:
        for sor in fm:
            l.append(float(sor.strip()))
    return l

def minuszt_keres(l):
    v = False
    i = 0
    while i < len(l) and l[i] >= 0:
        i+=1
    if i < len(l):
        v = True
    return v

def szamol_penny(l):
    db = 0
    for szam in l:
        if round(szam % 1, 2) != 0:
            db+=1
    return db
            
def szamol_min5(l):
    db = 0
    for szam in l:
        if szam >= 5:
            db+=1
    return db

def osszead_8_23(l):
    s = 8.23
    for szam in l:
        s+=szam
    return s

def keres_elso10(l):
    v = False
    i = 0
    ssz = -1
    while i < len(l) and l[i] <= 10:
        i+=1
    if i < len(l):
        v = True
        ssz = i
    return v, ssz+1

def keres_csupa5(l):
    v = False
    i = 0
    while i < len(l) and l[i] % 5 != 0:
        i+=1
    if i < len(l):
        v = True
    return v

def kiir(l,v,pa,l5,o8,v10,e10,c5):
    print(f"a, A lista: {', '.join(map(str, l))}")
    if v:
        print("b, Volt olyan, hogy a pincér vásárolt valamit.")
    else:
        print("b, Nem volt olyan, hogy a pincér vásárolt valamit.")
    print(f"d, {pa} alkalommal kapott biztosan pennyt is.")
    print(f"f, {l5} esetben kapott legalább öt fontot.")
    print(f"h, {o8} font volt a tárcájában óra végén, ha már alapból volt benne 8.23 font.")
    if v10:
        print(f"j, Volt olyan vendég, aki tíz fontnál többet fizetett. {e10}. fizetéskor történt így először.")
    else:
        print(f"j, Nem volt olyan vendég, aki tíz fontnál többet fizetett.")
    if c5:
        print(f"l, Volt olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát.")
    else:
        print(f"l, Nem volt olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát.")
    
# főprogram
osszegek = beolvas()
vane_minusz = minuszt_keres(osszegek)
penny_alkalmak = szamol_penny(osszegek)
legalabb5 = szamol_min5(osszegek)
osszeg_8_23 = osszead_8_23(osszegek)
volte_10f, ssz_elso_10f = keres_elso10(osszegek)
csupa_5font = keres_csupa5(osszegek)
kiir(osszegek, vane_minusz, penny_alkalmak, legalabb5, osszeg_8_23, volte_10f, ssz_elso_10f, csupa_5font)