'''# Donguler konusu tekrar islemleri icin bulunmaz hint kumasi gibidir
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

#kisa kisa ornekelr oilusturalim
listem = [1,2,3,4,5,6]
for item in listem:
    print(item)#listeyi bize dikey olarak verir

#degisken gostermeden direkt dongu olusturabiliriz
for i in (1, 2, 3):
    c = i + 1
    print(c)    

#Dilimleme yontemiyle yapalim degisken tanimladan degiskeni ,listeyi veya szolugu tanimda verelim
for a in ("Nail"[:3]):# bastan 3 kadar bana yazdir dedim
    print(a)


#listenin tüm öğelerini yineleyen ve öğe 2'den büyükse öğeyi yazdıran bir döngü oluşturun
big_num = [1,2,3,4,5,6]
for item in big_num:
    if item > 2:   
        print(item)
'''
#meyve.txt dosyamizda her dizenin uzunlugunu yazdiralim
fruits_list = open("meyve.txt")
fruits_read = fruits_list.read()
fruits_list.close()
fruits_read = fruits_read.splitlines()
for i in fruits_read:
    print(len(i))


#2.yol 
#Başka bir yol da kullanmaktır:readlines()

file = open("meyve.txt")
content = file.readlines()
content = [line.strip() for line in content]
file.close() 
for i in content:    
    print(len(i))

#celciustan fahrenayt pratik olarak for dongusyle donusturme donusturme
hots =[10,-50,100]
def cel_to_fahr(celsius):    
    fahrenheit = celsius * 9/5 + 32    
    return fahrenheit
for temprature in hots:#daha once hots dizisinde olan degiskenleri temperatur degiskenene aktar
    print(cel_to_fahr(temprature))   
#not for dongusu listeleri alt alta siralar ama istersek yatay olarak degistebilirz
