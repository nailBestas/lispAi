#Harici bir metin dosyasini icini okutmak veya cikartmak
# daha once kat.txt dosyasini olusturmustuk simdi onu acalim ve okuylim
myfile = open("kat.txt")
myread = myfile.read()
print(myread)


other_file = open("meyve.txt", "r")
read_file = other_file.read()
print(read_file)