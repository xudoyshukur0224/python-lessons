# # List - royxat
# fruit = "apple"
# fruit2 = "grape"
# fruit3 = 'banana'
# print(fruit2)
# fruits = ["apple", "grape", 'banana' ]
# # List elementi index orqali olinadi
# # Dasturlash indexlash 0 dan boshlanadi
# # List elementini olish
# print(fruits[2])
# mix_data =[12, 0.55, 77, 5.54 'test']
# print(type(fruits))
# print(type(mix_data))
# # list elemenini ozgartirish
# fruits[1] = 'cherry'
# print(fruits)
# # list uzumligi (length) - ro'yxatda saqlangan elementlar soni
# print(len(fruits))
# print(len(mix_data))
# # listdagi so'ngi elementni topish
# # last element
# length = len(mix_data)
# last_index= length - 1
# last_element = mix_data[last_index]
# print(last_element)


# # Ro'yxat elementlari ustida amallar
# numbers = [12, -15, 88.99, 10, 15.93, -8.75 ]
# # 1. Ro'yxat elementini o'zgartirish
# numbers[1] = 20
# print(numbers)

# # Ro'yxatga yangi element qo'shish
# # 1. list.append(new_element) method
# numbers.append(17)
# numbers.append(-102.89)
# print(numbers)

# # 2. list.insert(index, element) method
# numbers.insert(2, 13)
# print(numbers)
# numbers.insert(0, 0)
# print(numbers)

# # CRUD - create / read / update / delete
# # Ro'yxat elementini o'chirish
# # 1. list.remove(element)
# numbers.remove(0)
# print(numbers)
# numbers.remove(numbers[3])
# print(numbers)

# # 2. del operator
# del numbers [5]
# print(numbers)

# # Ro'yxatdagi elementi sug'irib olish
# # list.pop(index?) method
# number = numbers.pop(2)
# print(number)
# print(numbers)
# last_element = numbers.pop()
# print(last_element)

# Amaliyot
# 1
ismlar = ("Xayitboy", 'Ozodbek', "Akmal")
print("Olib keldingmi " + ismlar[1] + " do'stim") 
print(ismlar[0] + " kading bomi?")
print( ismlar[2] + " kecha olimpiada qiynalmadingmi")
# 2
sonlar = [67, 7238, -93, -895649.7954, 753.0956, ]
print(sonlar)
sonlar.insert(0, 44)
print(sonlar)
sonlar[3] = 54
print(sonlar)
# 3
t_shaxslar = ["Amir Temur", "Alisher Navoiy", 'Mirzo Ulugbek']
z_shaxslar = ["Ilonmask", "Shavkat Mirziyoyev", 'Xayitboy Normetov']
print(t_shaxslar)
print(z_shaxslar)
print(f"Men tarixiy shaxslardan {t_shaxslar [0]} zamonaviy shaxslardan esa {z_shaxslar[1]} bilan uchrashishni istardim" )    
# 4 
friends = []
friends.append  ('Xayitboy') 
friends.append  ('Ozodbek') 
friends.append  ('Akmal')
friends.append  ('Madina')  
print(friends) 
friends.remove ('Ozodbek')
friends.remove ('Akmal')
print(friends)

# 5 
mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(0))
print("Kelgan mehmonlar", mehmonlar)  