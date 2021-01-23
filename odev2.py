


def fn1(aranan1,aranan2):
    girdi = input("İşlem için metin giriniz:")
    girdicopy = girdi.lower()
    liste = girdicopy.split(" ")
    
    sonuc = list()
    for i in liste:
        if i.startswith(aranan1):
            a = girdicopy.find(i)
            sonuc.append(girdi[a])
        if i.startswith(aranan2):
            sonuc.append(i)
    print(sonuc)


def fn2(aranan1,aranan2):
    girdi = input("İşlem için metin giriniz:")
    liste = girdi.split(" ")
    parametre1 = list()
    parametre2 = list()
    for i in liste:
        if i.endswith(aranan1):
            parametre1.append(i)
        if i.endswith(aranan2):
            parametre2.append(i)
    print(parametre1,parametre2)
    
def fn3(aranan1, aranan2):
    
    girdi = input("İşlem için metin giriniz:")
    liste = girdi.split(" ")
    parametre1 = list()
    parametre2 = list()
    for i in liste:
        if i.startswith(aranan1):
            continue
        if i.endswith(aranan1):
            continue
        if i.count(aranan1):
            parametre1.append(i)
    for i in liste:
        if i.startswith(aranan2):
            continue
        if i.endswith(aranan2):
            continue
        if i.count(aranan2):
            parametre2.append(i)
    print(parametre1,parametre2)

def fn4(aranan1,aranan2):
    q = aranan1[0]
    z = aranan1[-1]
    t = aranan2[0]
    y = aranan2[-1]
    girdi = input("İşlem için metin giriniz:")
    girdi1= girdi
    parametre1 = list()
    parametre2 = list()
    for i in girdi:
        if i == q:
            a =girdi.find(q)
            b =girdi.find(z)
            parametre1.append(girdi[a:b+1])
            girdi = girdi[b+1::]
    girdi = girdi1
    for j in parametre1:
        if parametre1.count(""):
            parametre1.remove("")
    
    for i in girdi:
        if i == t: 
            c =girdi.find(t)
            d =girdi.find(y)
            parametre2.append(girdi[c:d+1])
            girdi = girdi[d+1::]
        else:
            continue
    for j in parametre2:
        if parametre2.count(""):
            parametre2.remove("")
    print(parametre1,parametre2)
    
def fn5(aranan1,aranan2):
    a = aranan1[0]
    b = aranan1[2]
    c = aranan1[-1]
    d = aranan2[0]
    e = aranan2[2]
    f = aranan2[-1]


    girdi = input("İşlem için metin giriniz:")
    girdi1= girdi
    parametre1 = list()
    parametre2 = list()
    k = girdi.find(a)
    l = girdi.find(b)
    m = girdi.find(c)
    for i in girdi:

        if k < l < m:
             s = girdi[k:m]
             parametre1.append(s)
             girdi = girdi[k+1::]
    girdi = girdi1
    n = girdi.find(d)
    p = girdi.find(e)
    r = girdi.find(f)   
    
    for i in girdi:
    
        if n <  p < r:
            t = girdi[n:r]
            parametre2.append(t)
            girdi = girdi[n+1::]
            
    print(parametre1,parametre2)

        
    
