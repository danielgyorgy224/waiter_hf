#alprogramok
def beolvas():
    l = []
    with open("adatok.txt", "r", encoding="utf-8") as fm:
        for sor in fm:
            l.append(float(sor.strip()))
    return l
def összegzés(o):
    sum=0
    for szam in o:
        sum+=szam
    return sum

def összegzés2(o):
    sum=0
    for szam in o:
        sum+=round(szam%1,2)
    return sum

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
    return sorszam
    


def kiir(o,o_b,p,m,h):
    print(f"A bevételek:{o}")
    print(f"Az óra bevétele {o_b}")
    print(f"Ennyi fontot keresett peniben kapott az órában:{p}")
    print(f"A legnagyobb összeg amit fizettek neki: {m}")
    print(f"{h}.ik vendég fizetett 9-et.")



#főprogram
#input
osszegek = beolvas()

#számítás
Az_ora_bevetele=összegzés(osszegek)
peni=összegzés2(osszegek)
max_kivalasztas = max(osszegek)
hanyadik_vendeg = hanyadik(osszegek)

#output
kiir(osszegek,Az_ora_bevetele,peni, max_kivalasztas, hanyadik_vendeg)
