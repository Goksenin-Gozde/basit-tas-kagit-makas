import random
oyun = {"taş":"makas","makas":"kağıt","kağıt":"taş"}
li = ["taş","kağıt","makas"]
bilgisayar = random.choice(li)
oyuncu = input("taş mı? kağıt mı? makas mı?").lower()
print("TAŞ")
print("KAĞIT")
print("MAKAS")
if oyun[oyuncu] == bilgisayar:
    print("Bilgisayar", bilgisayar, "değerini girmişti")
    print("Tebrikler KAZANDINIZ!!!")
else:
    print("Bilgisayar",bilgisayar,"değerini girmişti")
    print("Bilgisayar oyunu kazandı")
