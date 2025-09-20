# string formatting dize bicimlendirme anlamina geliyor daha once loop konusunda anlatmistik biraz simdi orneklerini verelim
# eski python ozellikleri sikkintiliydi simdi ise f ile herseyi yapabiyoruz
a = 12
b = 6
txt = f"a ve b sayilarinin carpimi: {a * b} dir"
print(txt)


price = 100
tax = 0.50
sum_price = f"fiyat {price +(price * tax) }dollars"
print(sum_price)
#javascrpte sablon degizmeleri diyorduk f {} 


price = 99
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"#burada string formatting ozelligimize kosul ifadelerinin degisik bir kullanim ornegi mevcut
print(txt)

not1 = 61
test_exam = f"harf notunuz {'C' if not1>60   else 'F'}"#kosul ifadelerini de baglayabiliriz
print(test_exam)