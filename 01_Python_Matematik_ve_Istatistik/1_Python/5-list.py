# Listeler bir veri turu olup string ve int ten daha gelismis bir yapidadir
# yani listeler tumlesik veri turunu barindirabilirler sayi +string 
# liste birden fazla ogeyi barindiran veri turudur [koslei parantez icinde koldar yaziliyor]
adress = ['Gures caddesi', '1512 Sok', 'Siirt']
print(adress)
#liste ogelerine erismek icin dizin mantigi kullaniyoruz yani indise gore dizi arama mantigina gore  gidiyoruz
print(adress[0])
print(adress[1])
print(adress[2])
print(adress[0],adress[1],adress[2])#buradaki , ler argumandir

#listenin uzunlugunu
print(len(adress))

#Anlamamiz icin daha gercekci bir ornek yapalim
sebzeler = ['marol', 12 ,'tomato' ,147]
print(sebzeler)
print(sebzeler[0], sebzeler[1] , sebzeler[2] , sebzeler[3])
#ciktida gordugunuz gibi , yani , bolumleme yaparargumanlariyla yanyana yazablir string ve int yanyana rahatca ve
#dizi mantigina gore 0 dan baslayarak istedigmiz indiste eleman alabiliyoruz

#negatif indexleme yani listede bir nevi son elemanlari bulma
print(sebzeler[-1])#147
print(sebzeler[-2])#tomato
print(sebzeler[-3])#12
print(sebzeler[-4])#marol 


#liste dilimleme [x:y] slicing islemi
#dilimlemede mantik ornegin 1 dizinden :buraya kadar anlamindadir 
print(sebzeler[0:3])#'marol', 12 ,'tomato' verecek o dan 3 elemana kadar
print(sebzeler[1:2])# 1den 2 elemana kadar burda 1 eleman dahil degil anlaminda
print(sebzeler[:2])#0 dan 2 elemana kadar
print(sebzeler[:4])#o dan 4 elemana  kadar
print(sebzeler[:])#butun elemanlari kapsiyor

#negatif dilimleme
print(sebzeler[-1:-2])#bize bos bir dize dondurur sebebi basit den buraya kadar dilimle unutmayalim
print(sebzeler[-4:])#bu bize sondan gelecek sekilde butun elemanlari kapsayacak sekilde verir
#-4 elemanindan sona kadar demek 
print(sebzeler[-4:-1])#-4 den -1 kadar dilimle dedim 147 verisi haric hepsi gelecek
print(sebzeler[-4:-3])#marol ciktisi verir 

#Diger liste ozellikleri 
print(list(range(1,20))) 
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Gördüğünüz gibi sadece içindeki liste sınırlarını belirtmemiz gerekiyordu. Bu yüzden 1 ve 20'u belirledik. 20'un listeye dahil edilmediğini unutmayın. Oluşturulan liste her zaman üst sayıdan önce bir sayıya kadar çalışır. Örneğimizde üst sayı 20 olduğu için 19'a kadar çıkıyor.range()
#Bir adımı üçüncü bağımsız değişken olarak da belirtebilirsiniz:
print(list(range(1, 10, 3)))# range komutu burda (baslangic,bitis,artirma seklinde calisir)
# 1-9 kadar 3 er 3 er artir ekrana yazidr dedim 
print(list(range(1,10,2)))#burada list() fonskyonu cok onemli eger sarmalanmazsa range(....) cikar

name = "nail bestas"
print(name[2])#2 numaradaki index degeriniv ver dedim  sonuc i olur
print(name[2:4])# string ifadedeki 2 den 4 kadar olan degeri ver sonuc 'il' olur
#dikkat dilimleme ozelliginde 0 dizisi yoktur yani eleman sifirdan baslamiyor
print(name[1:6])#1 den 6 kadar string ifadeyi verecektir


letters = 'fsuofhso;gfhsghdsag;oihasg'
print(letters[-2])
print(letters[-3:-1])


mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(mylist[17])#sonuc r olur liste mantigi dizi mantigidir 0 dan baslar ama parcalama den buraya kada mantigi


#listeden eleman kaldirma
numbers = [1, 2, 3, 4, 5]

numbers.remove(5)# liste icerisinde eleman olmak sartiyla remove() komutuyla herseyi kadlirabilirz
print(numbers)


#listeye eleman ekleme append
sebzeler = ['marol', 12 ,'tomato' ,147]
sebzeler.append('hiyar')#append ile eleman ekledik ama unutmadan sadece listenin sonuna bir defada  bir eleman eklyebliyoruz 2 eleman ayni anda atamiyoruz
print(sebzeler)
sebzeler.remove('hiyar')#remove komutu ile tekrar kaldirdik
print(sebzeler)
#Dikkar print(sebzeler.remove('hiyar')) komutu none degerini dondurur 

#listeden listeye eleman ekleme
list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,11,12]
list1.append(list2[-6])#sondan sayarak ilk elemanin yani 7 eklemeyi basardik
print(list1)

#liste ogelerini birlestirme
list3 =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
list4 =list3[0] + list3[-1]
print(list4)

#Python'da adı verilen başka bir veri türü daha vardır:tuple

mytuple = (1, 2, "Three")
print(mytuple)

#Tam olarak bir istisna gibi:list
#1. Tanımlama grubunu tanımlamak için köşeli parantez yerine parantez kullanırsınız.
#2. Bir tuple değiştirilemez, yani listelerde olduğu gibi tuple ye  öğe ekleyemez veya kaldıramazsınız. Bir demete yöntem eklemeye çalışmak bir hata verir:append
#3. Tuple'lar nadiren kullanılır. Ancak, gerçekten değiştirilmesini istemediğimiz bir listeye ihtiyacınız olursa, liste yerine demet kullanmak iyi bir fikirdir.