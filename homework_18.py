#tapsirma-1
age = int(input("Yoshingizni kiriting:"))
if age >= 18:
    print("Siz voyaga yetgansiz!")
else:
    print("Siz voyaga yetmagansiz!")

#tapsirma-2
parol = input("Parolni kiriting:")
if parol == "python123":
    print("Hush kelibsiz!")
else:
    print("Parol notogri!")

#tapirma-3
bahasi = int(input("Mahsulot narxini kiriting:"))
if bahasi > 500000:
    shegirme = bahasi * 0.10
    uliwma_bahasi = bahasi - shegirme
    print(f"Chegirma: {shegirme} som")
    print(f"Yakuniy narx: {uliwma_bahasi} som")

#tapsirma-4
araliq = int(input("Araliqti kiritin:"))
if araliq > 10:
    km_bahasi = 3000
else:
    km_bahasi = 2000

uliwma_bahasi = araliq * km_bahasi
print(f"1 km bahasi: {km_bahasi} swm")
print(f"Uliwma bahasi: {uliwma_bahasi} swm")

#tapsirma-5
bahasi = int(input("Buyirtpa bahasi?:"))
if bahasi > 100000:
    jetkiziw = 0
    print("Jetkiziw biypul!")
else:
    jetkiziw = 15000
    print(f"Jetkerip beriw: {jetkiziw} sum")

jami_tolem = bahasi + jetkiziw
print(f"Buyirtpa bahasi: {int(bahasi)}")
print(f"Jami tolem: {int(jami_tolem)} sum")

#tapsirma-6
ball = int(input("Ballingizni kiriting:"))
if ball >= 90 and ball <= 100:
    print("Sizning bahoyingiz: A'lo")
elif ball >= 75 and ball <= 89:
    print("Sizning bahoyingiz: Yaxshi")
elif ball >= 60 and ball <= 74:
    print("Sizning bahoyingiz: Qoniqarli")
else:
    print("Sizning bahoyingiz: Qoniqarsiz")

#tapsirma-7
transportlar = ['Avtobus', 'Metro', 'Taksi', 'Velosiped']
narxlar = [2000, 1700, 15000, 1000]
print("==== TRANSPORT TANLASH ====")
for i in range(len(transportlar)):
    print(f"{i}. {transportlar[i]}")

choose = int(input("Transport tanlang:"))
indeks = choose - 1
print(f"Siz {transportlar[indeks]} transportini tanladingiz.")
print(f"Narxi: {narxlar[indeks]} som")

#tapsirma-8
mevalar = ['olma', 'banan', 'uzum', 'anor', 'shaftoli']
meva = input("Meva nomini kiriting?:")

if meva in mevalar:
    print(f"{meva} royxatda mavjud!")
else:
    print(f"{meva} royxatda yoq!")

#tapsirma-9
oquvchilar = ['Ali', 'Vali', 'Sardor', 'Malika', 'Madina']
name = input("Ism kiriting:")

if name in oquvchilar:
    print(f"Oquvchi royxatda mavjud!")
    print(f"Birinchi harfi: {name[0]}")
else:
    print("Oquvchi royxatda yoq")

#tapsirma-10
numbers = [12, 5, 8, 17, 20, 3, 10, 7]
for san in numbers:
    if san % 2 == 0 :
        print(f"{san} - Juft son")
    else:
        print(f"{san} - Toq son")

#tapsirma-11
numbers = [2, 5, 8, 11, 14, 17]
for i in range(len(numbers)):
    if numbers[i] < 10:
       numbers[i] = numbers[i] * 2
    else:
        numbers[i] = numbers[i] + 5 

print(numbers)

#tapsirma-12
products = ['Gosht', 'Non', 'Sut', 'Tuxum', 'guruch']
prices = [90000, 4000, 12000, 1800, 15000]
print("Mahsulotlar:")

for i in range(len(products)):
    print(f"{i+1}. {products[i] - {prices[i]}} som")

choose = int(input("Qaysi mahsulot kerak?:"))
quantity = int(input(f"{products[choose]} qancha kerak?"))
total_sum = prices[choose] * quantity

print(f"Mahsulot: {products[choose]}")
print(f"Soni: {quantity}")
print(f"Umumiy summa:{total_sum} som")
