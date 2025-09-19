# Donguler konusu tekrar islemleri icin bulunmaz hint kumasi gibidir
#for dongusu kullanim ornekleri

#once bir liste yapalim
list1 = [1,2,3,4,5,6]
for i in list1:#burada liste ogesini tek tek yeni olusturdumuz i degiskenine atama yapiyoruz
    print(i)

#sozluk olarak bir tane yaapalim
dict1 = {"Nail":1985, "Musa":1989, "Okan":1968}
for item in dict1.values():
    print(item)
for i in dict1.keys():
    print(i)

#sayisal bir ornek yapalim
list2 = [0,1,2,3,4,5,6]
print(list2)
for item in list2:
    c = item + 10
    print(c)

#dosya okumada yapalim
dosyam = open("kat.txt")
dread = dosyam.read()
print(dread)    