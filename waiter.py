# alprogramok
def beolvas():
    l = []
    with open("adatok.txt", "r", encoding="utf-8") as fm:
        for sor in fm:
            l.append(float(sor.strip()))
    return l

# Gyuri feladatai: b, d, f, h, j, l
def összegzés(o):
    sum=0
    for szam in o:
        sum+=szam
    return sum

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

# Bence feladatai: c, e, g, i, k, m
def összegzés2(o):
    sum=0
    for szam in o:
        sum+=round(szam%1,2)
    return round(sum,2)
  
def max(o):
    max_ertek = 0
    for i in range(1, len(o)):
        for j in range(1, len(o)):
            if (o[i] > o[j]):
                max_ertek = o[i]
    return max_ertek

def hanyadik(o):
    sorszam = -1
    i=0
    while not o[i]==9:
        i+=1
    sorszam=i
    return sorszam+1
    
def tiznel_tobb(o):
    van = False
    sorszam = 0
    for i in range(1, len(o)):
        if i<10:
            van = True
            if van == True:
                for j in range(1, len(o)):
                    if j<10:
                        sorszam = j
    return sorszam+1

def megszamolas(o):
    osszeg = 0
    for i in range(0, len(o)):
        osszeg+=1
    return osszeg/2

def kiir(l,v,pa,l5,o8,v10,e10,c5,o_b,p,m,h,hany_tiz_tobb,f):
    print(f"a, A lista: {', '.join(map(str, l))}")
    if v:
        print("b, Volt olyan, hogy a pincér vásárolt valamit.")
    else:
        print("b, Nem volt olyan, hogy a pincér vásárolt valamit.")
    print(f"c, Az óra bevétele {o_b}")
    print(f"d, {pa} alkalommal kapott biztosan pennyt is.")
    print(f"e, Ennyi fontot keresett pennyben kapott az órában: {p}")
    print(f"f, {l5} esetben kapott legalább öt fontot.")
    print(f"g, A legnagyobb összeg amit fizettek neki: {m}")
    print(f"h, {o8} font volt a tárcájában óra végén, ha már alapból volt benne 8.23 font.")
    print(f"j, {h}.ik vendég fizetett 9-et.")
    if v10:
        print(f"j, Volt olyan vendég, aki tíz fontnál többet fizetett. {e10}. fizetéskor történt így először.")
    else:
        print(f"j, Nem volt olyan vendég, aki tíz fontnál többet fizetett.")
    print(f"k, {hany_tiz_tobb}. vendég volt, aki utoljára fizetett 10nél többet")
    if c5:
        print(f"l, Volt olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát.")
    else:
        print(f"l, Nem volt olyan vendég, akinek módjában állt csupa ötfontossal kiegyenlíteni a számlát.")
    print(f"m, {f} fonttal zárta az órát a pincér")
    
# főprogram
osszegek = beolvas()

vane_minusz = minuszt_keres(osszegek)
penny_alkalmak = szamol_penny(osszegek)
legalabb5 = szamol_min5(osszegek)
osszeg_8_23 = osszead_8_23(osszegek)
volte_10f, ssz_elso_10f = keres_elso10(osszegek)
csupa_5font = keres_csupa5(osszegek)
az_ora_bevetele=összegzés(osszegek)
penny=összegzés2(osszegek)
max_kivalasztas = max(osszegek)
hanyadik_vendeg = hanyadik(osszegek)
hanyadik_tiznel_tobb = tiznel_tobb(osszegek)
fizetes = megszamolas(osszegek)

kiir(osszegek, vane_minusz, penny_alkalmak, legalabb5, osszeg_8_23, volte_10f, ssz_elso_10f, csupa_5font, az_ora_bevetele, penny, max_kivalasztas, hanyadik_vendeg, hanyadik_tiznel_tobb, fizetes)
