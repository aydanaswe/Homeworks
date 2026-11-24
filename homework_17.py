#tapsirma-1
fruits = ['apple', 'banana', 'orange', 'kiwi']
for i in fruits:
     print(i)

#tapsirma-2
names = ['ali', 'vali', 'hasan', 'husan']
for a in names:
    print(a.upper())

#tapsirma-3
cars = ['bmw', 'mers', 'nexia', 'malibu', 'cobalt']
for car in cars:
    print(car[0])

#tapsirma-4
countries = ['UZBEKISTAN', 'RUSSIA', 'TURKEY', 'USA']
for a in countries:
    print(a.lower())

#tapsirma-5
names = ['ali', 'sardor', 'abdulloh', 'aziz']
for i in names:
    print(f"{i} - {len(i)} ta harf")

#tapsirma-6 range() arqali ozgertilgeni:
animals = ['cat', 'dog', 'lion', 'tiger']
for i in range(0, 4):
    animals[i] = animals[i].upper()
print(animals)

#tapirma-7
names = ['ali', 'sardor', 'sardor', 'aziz']
upper_name = []
for name in names:
    upper_name.append(name.upper())
print(upper_name)

#tapirma-8
names = ['ali', 'hasan', 'husan', 'sardor']
capitalize_name = []
for name in names:
    capitalize_name.append(name.capitalize())
print(capitalize_name)

#tapsirma-9
names = ['ali', 'vali', 'hasan', 'husan', 'sardor', 'aziz']
for a in names[::2]:
    print(a)

#tapsirma-10
animals = ['tiger', 'lion', 'elephant', 'rabbit']
for i in animals:
    print(f"{i[0]} - {i[-1:]}")

#tapsirma-11
words = ['python', 'programming', 'computer', 'developer']
for a in words:
   print(a[0].upper() + a[1:-1] + a[-1].upper())

#tapirma-12
cars = ['bmw', 'nexia', 'malibu', 'cobalt', 'damas']
for i in range(len(cars)):
    cars[i] = cars[i].upper()
print(cars)

#tapsirma-13
question = input("Ism kiriting:")
question_2 = int(input("Necha marta chiqarilsin:"))
for i in range(question_2):
    print(question)
