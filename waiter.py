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
        


def kiir(o,o_b,p):
    print(f"A bevételek:{o}")
    print(f"Az óra bevétele {o_b}")
    print(f"Ennyi fontot keresett peniben kapott az órában:{p}")
#főprogram
#input
osszegek = beolvas()

#számítás
Az_ora_bevetele=összegzés(osszegek)
peni=összegzés2(osszegek)

#output
kiir(osszegek,Az_ora_bevetele,peni)