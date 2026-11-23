#tapsirma-1
fruits = ['apple', 'banana', 'orange', 'kiwi', 'grape']
print(fruits)

#tapsirma-2
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(numbers[2])

#tapirma-3
colors = ['red', 'green', 'blue', 'yellow']
colors[1] = "black"
colors[3] = "white"
print(colors)

#tapsirma-4
students = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
print(len(students))

#tapsirma-5
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
a = numbers[2:5]
print(a)

#tapsirma-6
letters = ['a', 'b', 'c', 'd', 'e', 'f',]
a = letters[::-1]
print(a)

#tapsirma-7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = numbers[::2]
print(a)

#tapsirma-8
students = [
    ['Ali', 90, 'English'],
    ['Vali', 85, 'Math'],
    ['Hasan', 95, 'Python']
]
print(students[0][0])
print(students[0][1])
print(students[0][2])

#tapsirma-9
students = [
    ['Ali', 90],
    ['Vali', 95],
    ['Hasan', 95]
]
students[0][1] = 100
print(students)

#tapirma-10
programming = [
    ['HTML', 'CSS'],
    ['Python', 'JavaScript'],
    ['Java', 'C++']
]
print(programming[1][0])
print(programming[1][1])

#tapsirma-11
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[1::3])

#tapsirma-12
numbers = [12, 7, 8, 15, 20, 33, 44, 51, 60]
a = numbers[::2]
print(a)

#tapsirma-14
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print("1-list" , numbers[:4])
print("2-list" , numbers[4:])

#tapirma-15
numbers = [10, 20, 30, 40, 50]
a = numbers[1]
numbers[1] = numbers[3]
numbers[3] = a
print(numbers)

#tapsirma-16
students = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
a = students[0]
students[0] = students[4]
students[4] = a
print(students)

#tapsirma-17
students = [
    ['Ali', 85],
    ['Vali', 90],
    ['Hasan', 75],
    ['Husan', 75]
]
a = students[0]
students[0] = students[2]
students[2] = a
print(students)

#tapsirma-18
miywe = ['', 'Olma', 'Uzum', 'Banan', 'Anor', 'Shaftoli']
print("Mevalar:")
print("1.", miywe[1])
print("2.", miywe[2])
print("3.", miywe[3])
print("4.", miywe[4])
print("5.", miywe[5])

choose = int(input("Qaysi mevani tanlaysiz?:"))
print(f"Siz {miywe[choose]} mevasini tanladingiz!")


#tapsirma-19
fruits = ['', 'Olma', 'Uzum', 'Banan', 'Anor', 'Shaftoli']
prices = ['', 5, 8, 12, 10, 15]
print("FRUIT MARKET")
print(fruits)
print(f"1. {fruits[1]} - {prices[1]}$")
print(f"2. {fruits[2]} - {prices[2]}$")
print(f"3. {fruits[3]} - {prices[3]}$")
print(f"4. {fruits[4]} - {prices[4]}$")
print(f"5. {fruits[5]} - {prices[5]}$")

choose = int(input("Qaysi mevani tanlaysiz?:"))
kg = float(input(f"{choose} mevasidan necha kg olasiz?:"))
jami = kg * prices[choose]
print("CHEK")
print(f"Meva:", {fruits[choose]})
print(f"Miqdori:  {kg} kg")
print(f"1 kg narxi: {prices[choose]}$")
print(f"Umumiy narxi: {jami}$")

#tapsirma-20
fruits = ['apple', 'banana', 'orange']
fruits.append('mango')
fruits.insert(1, 'strawberry')
print(fruits)

#tapsirma-21
cars = ['BMW', 'Mercedes', 'Audi', 'Tesla']
cars.remove('BMW')
print(cars)

#tapsirma-22
numbers = [10, 20, 30, 40, 50]
oshirilgen = numbers.pop()
print("Ochirilgan element:", oshirilgen)
print("Qolgan list:", numbers)

#tapsirma-23
fruits = ['apple', 'banana', 'apple', 'orange', 'apple', 'kiwi']
a = fruits.count('apple')
print("Apple soni:", a)

#tapsirma-24
languages = ['Java', 'C++', 'Python', 'JavaScript', 'PHP']
indeks = languages.index('Python')
print("Python indeksi:", indeks)

#tapsirma-25
numbers = [45, 12, 89, 3, 21, 67, 10]
numbers.sort()
print(numbers)
