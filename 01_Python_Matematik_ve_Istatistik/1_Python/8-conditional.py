#Conditional -Kosul ifadeleri
'''Python'da koşul ifadeleri, belirli koşullara bağlı olarak belirli kod bloklarını yürütmek için kullanılır.
 Bu ifadeler, bir programın akışını kontrol etmeye yardımcı olarak farklı durumlarda farklı davranmasını sağlar'''
sifreler = {"nail":1234, "Arya":4567, "ceylo":0000}
print(sifreler)
print(sifreler.values())
#print(4567 in sifreler.values())#4567 sifreler sozlugunde deger olarak var mi ?
pins = 1234 #istersek yeni bir degisken yapip karsilastirabiliriz 
keys = 'ceylo'
if pins in sifreler.values():
    print("Yes")
else:
    print("NO")    

if keys in sifreler.keys():
    print("Yess")
else:
    print('Nooo')    


#baska ornek yapalim
if 3 > 3:
    print("Dogru")
else:    
    print("hayir yanlis")

# ornek
a = 50
b = 40
c = a+b 

if a > b :
    print("dogru")
else:
    print("yanlis") 

#elif if else birlikte kullanalim
user_input = float(input("Lutfen bir sayi giriniz: "))
if user_input > 100:
    print("Cok buyuk")
elif user_input == 100:
    print("Orta 100 den kucuk sayi girdiniz")  
elif user_input > 50 :
    print("girdiginiz sayi 50 den buyuk")
elif user_input < 50:
    print("Girdiginiz sayi elliden kucuk")
elif user_input < 10 :
    print('lutfen 10 dan buyuk sayi giriniz :')       

#baska bir ornek
score = 80
#basari_harf = ""#istersek onceden degisken atamasi bos olarak girebilirz istersek dongudede atayabiliriz

if score >= 90:
    basari_harf = "A"
elif score >= 80:
    basari_harf = "B"
elif score >= 70:
    basari_harf = "C"
elif score >= 60:
    basari_harf = "D"
else :
    basari_harf = "F"

print("Basari durumunuz:", basari_harf , "sinifi gectiniz")             

# NOTlaar
# Bir if ifadesi tek basina kullanilabilir ama else asla olmaz
#Bu elif ifade, birden fazla koşulu sırayla kontrol etmenize ve hangi koşulun doğru olduğuna bağlı olarak farklı kod bloklarını çalıştırmanıza olanak tanır.
#Dikkat degisken kosul oalrak else de kullanilmaz
