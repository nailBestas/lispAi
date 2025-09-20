# 3-Dersimiz numbers yani sayilar

#1-float(kayan sayi) ve int(tamsayi) 
x = 5
print(x)
print(type(x))#tamsayi
print(type(100))#int tamsayisi turunuv erir
print(type(-100))#int turu syisini veir
print(type(0.5))#float sayisini verir
print(type(1.900))#float sayisi veir
print(type(1.1))#sayi turunu bize floa verir
print(1e6)#1000000.0 sayisi
print(200000000000000000.0)#2e+17 sayisi
print(1e-4)#1/100000 anlaminagelen float sayi
print(2e400)#sonsuz inf + sayi
print(type(2e400))
print(-2e400)#-sonsuz inf float sayi

#2-Dort islem yapma
print(1+2)#aritmetik toplama
print(1.2 + 3)#int + float yaptik
print(1-1)#cikarma islmei yaptik
print(type(5.0 -2))#unutma sonuc float olur.. sayi oludgu surece float olur
print(1- -3)# 1 sayisindan -3 sayisini cikariyoruz sonuc +4 olacak
print(2- -3)#sonuc 5 oalcak aralarinda bosluk pep 8 ile uyumlu olandir
print(1 - (-3))#sonuc 4 olacak ayni matematikte yaptigimiz islem gibi
print(3 * 3)#carpma islemi sonuc 9 olur
print(3 * 9.2)#sonuc 27.6
print(12 / 4 )#bolme islemi toplama+bolme ve cikarma da souc otomatik deger veya turu atarken bolme islemi sonucu float dondurur sonuc 3.0 olacak pythonda sonuc float olarak dondurur eger int sayi istiorsaniz asagidaki ornege bakin
print(int(12 / 4))#sonuc direkt int olacak 3 sonra noktali sayi olamayacak
print(int(7 / 2)) # sonucu bize 3 verir neden cunku int tamsayi kismini alir
print(7 // 2) # ustteki tamsayiaya cevirme olmadan yani int yazmadan  direkt tamsayi kismini alabiriz 
print(3 // 2) #pozitif oldugu icin sonucu bolme islemini yapar tamsayiya dondurur ve 1 dondurur
print(-3 // 2) # negatif deger pozitif deger gibi degildir pozitif sayi tamsayiya yakin olan onceki sayiyi baz alir ama negatif sayi sonraki sayiya tamamlar sonuc 2 olur
#print(1 / 0) bu kod hata vercektir cunku 1 sayiy sifira bolunemez
print(5.0 // 2) # sonuc 2.0 oalrak bize verir 

#3-Uslu ifadeler
print(3 ** 2)# bu bir uslu sayi ifadesidir sonuc 3 2 kuvveti yani 9 verecektir
print(3 ** 1.5)#uslerin tamsayi olmasi gerekmez
print(3 ** -2) #sayinin tersi ve us kuvvetini alabiliriz

#4-modul operatoru veya moduler aritmetik yani kalani hesaplama
print(5 % 3)#kalan 2 dir
print(16 % 8)#kalan 0 olur
#print(1 % 0)# dvision error hatasi verir
print(5 % -3)# bu sonuc biraz karmasiktir ve sonuc -1 olur denkleme gore yapiyor bunu x -(y * (x // y))

#5-standart hileler
print(0.1 + 0.2)#sonuc 0.3 gostermesi gerekirken 0.30000000000000004 bu aslinda python ile ilgili degildir virgulli sayilarin bilgisayar deposunda saklanma seklidir

#Not Oncelik sirasi 
#İşlem sırası (1) üs alma, (2) çarpma, (3) bölme, (4) toplama ve (5) çıkarma şeklindedir.
print(1 + 2 * 5**2)#sonuc 51 olur

x = 1
y = 2
z = 3
print((x * y) ** z / 8)#once parantez ici sonra us sonrada bolme


#sonuclari ve turlerini sirasiyla bize verecektir
#dikkat edilmesi gereken tamsayilarin - ve + arlarinda 	-2.147.483.648 ile 2.147.483.647 32 bit tamsayi alabildgini 
#float	4	3,4E +/- 38 (yedi basamak) 32 bit ama pythonda double float olarak gecer
#double	8	1,7E +/- 308 (on beş basamak) 64 bit uzunlugunda 
#E burada sabitleri verir 1e6 orneginde 1 den sonra 6 sifirin geldigini bize soyluyor
# 00000000000000000.0 orneginde ise 2e+17 seklinde olur yani virgulun solunda 17 tane sifirin oldugunu bize soyler 2 basamakli oldugu zaman direk toplayarak gosteririz
# 1e-4 Kelimenin tam karşılığı , 1/10000 veya kuvvetine yükseltilmiş 1e-4olarak yorumlanır .10-40.0001
#2e400 inf sonsuzluk anlamına gelir ve oluşturmaya çalıştığınız sayının bilgisayarınızda izin verilen maksimum kayan nokta değerinin üzerinde olduğu anlamına gelir.



