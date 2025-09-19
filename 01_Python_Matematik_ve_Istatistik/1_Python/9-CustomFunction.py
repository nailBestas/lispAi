#Ozel fonksiyonlar yani daha once gorduk yerlesik fonksiyonlar
# daha once dir(__builtins__) komutu ile  gormustuk
# pythonda fonksiyonlar def anahtar kelimesi ile baslar.

def yas_hesapla(year):#def anahtar kelimesi ile fonk tanimladik ()icinde ise argumanimizi yani bir nevi buraya bir deger girecez veya degiskenimizi tanimladik
    age = 2025-year
    return age #return ifadesi deger dondurur
yas_hesapla(1985)#bu sekilde kullaniliriz
print(yas_hesapla(1985))#cikti gormek icin print fonskyonundan yararlandik

#baska func tanimlama ornegi
def yazdir():#argumansiz fonsiyounumuzu cagirabildik
    print('fonskyonumuz casliyor')#burrada print kullandik
yazdir()    


#baska func tanimlama orenegi
def hello_world():
    return "Hello World"
hello_world()
print(hello_world())#ekran ciktimiz alabiliriz
#dikkat print ile direkt calisir return ifadesinin calsmasini istiyorsak fonkmuzu print icine yazmaliyiz


#baska func tanimlama ornegi
def us_alma(n):
    return n ** 4# return ifadesi bu fonskyon caslitigi zaman bu degeri dondur anlamindir
print(us_alma(4))


#return ile print arasindaki farklar
def returning():
    return 10
def prnting():
    print(50)
# eger yukaridaki fonsiyounu calistirirsaniz print ekrana yazdirir ama return yazmaz 
# ama uygulamalarda her zaman return kullanin bu daha evrrensel birde turu vardir
print(type(returning()))#return tipnpn int oldugunu 
print(type(prnting()))#printing fonk ise nonetype oldugunu ogrnecez  

#bunun icindir ki int fonsiyonuna deger atayabiliriz ama printige atamayaiz
print(returning() + 80)# hata vermez ve 90 ceani bize  calistirir bunun icin return hep kullanmaliyiz
#print(type(prnting() + 40))#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' hatasi aliriz
#Herhangi bir dizeyi bağımsız değişken olarak alan ve bu dizenin uzunluğunu döndüren bir işlev oluşturalim
def len_string(a):
    return len(a)
print(len_string("Nail"))


#Daha karmasik bir fucntion yapalim
jobs_adress = ['Gures caddesi', 'hz. fakirullah sok.','no :13',6]
personel_pins = {"Nail":1985, "Ali":1980, "Ceren":1965}
print(jobs_adress)
pin = int(input("Lutfen pin numariniz giriniz: "))

def find_file(a):
    myfile = open("kat.txt")
    aparts = myfile.read()
    aparts= aparts.splitlines()#splitlines() , Python'da yerleşik bir dize yöntemidir ve çok satırlı bir dizeyi satır listesine böler
    if a in aparts:
        return "Evet bu kat listede mevcut"
    else:
        return "Hayir bu kat bu listede degil"

if pin in personel_pins.values():
    apart = input("Lutfen kat numarasini giriniz: ")
    print(find_file(apart))# apart argumani a icin fonskyon ne yazdiysa onu yapacak
else:
    print('yanlis deger girdiniz')
    print("bu bilgiye yalnızca şu kişiler erişebilir: ")   
    for key in personel_pins.keys():
        print(key)

    


#Ikili arguman ornegi yapalim
def carp(x,y,z):#argumanlar onemlidir
    return x*y*z
print(carp(1,2,3))

#toplama
def mysum(a, b):
    return a + b
print(mysum(10, 20))


#argumani basta atamamak ve kullanmak
def front_arguman(x=15, y=12, z=40):
    return x + y + z
print(front_arguman())


#Celsius derecelerini Fahrenheit'e dönüştüren bir fonksiyon oluşturun. Celsius'u Fahrenheit'e dönüştürme formülü F = C × 9/5 + 32'dir.
def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 +32
    return fahrenheit
print(cel_to_fahr(10))

#basit bir fonskyon uzunlugunu bulup kosullar ile test edelim
# def letter_len(a):
#     return len(a)#tam sayi girersek ne olur
# print(letter_len(10))#hatali cozum olur

def letter_len(l):
    if type(l) == int:
        print("len fonsksiyonu sadece string idadelerde calisir")
    elif type(l) == float:
        return "Sorry, floats don't have length"    
    else:
        return len(l)
print(letter_len(5.5))