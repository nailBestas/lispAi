#Python'da sözlük oluşturmak basit ve kolaydır. Daha önce de belirtildiği gibi, Python'daki sözlükler, anahtar-değer çiftlerinin değiştirilebilir, sırasız koleksiyonlarını depolamak için kullanılan bir veri yapısı türüdür
#listelerden farkli olarak koseli parantez yerine suslu parantez {} kullanilir
#diger farki eleman bulmak ve indexkemek icin [..dize mantigi degil][anahtar degeri girmek lazim "nail"]
keysPin  = {"nail":1985, "arya":2017, "ceylin":2021}
print(keysPin)
print(keysPin["nail"])#anahtar degeri ile degere ulasiyoruz
print(keysPin["arya"])
print(keysPin["ceylin"])
print(keysPin.keys())#anahtar keilimelerin ne oldugunu dict_keys(['nail', 'arya', 'ceylin'])bize gosterir
print(keysPin.values())#dict_values([1985, 2017, 2021]) degerleri verir



person = {"name":"nail", "surname":"bestas", "age":"38"}

#anahtar deger cifti kaldirma(Removing pair) "name":"nail" pop()fonksiyonu ile kaldirdik
person.pop("name")#anahtar kalktimi degeri otomatik kalkar pop() komutu cok populer
print(person)


#anahtar deger cifti eklemek (Adding new pair) "name":"nail"
person["name"] = "nail"
print(person)
person["child"] = "Ceylo"
print(person)
person["sira no"] = 1
print(person)
person.pop("sira no")
print(person)

# deger degistirme(Changing an existing value)
person["age"] = 30
print(person)

#iki listeyi bir sozlukte ekleme(Mapping two lists to a dictionary:)
keys = ["a", "b", "c"]
values = [1, 2, 3]
mydict = dict(zip(keys, values))
print(mydict)

#anlaminiz acisindan bir ornek daha 
meyve_sirasi = [1 ,2, 3]
meyveler = ["kivi" ,"muz", "karpuz"]
siraliSozluk = dict(zip(meyve_sirasi , meyveler))
print(siraliSozluk)
