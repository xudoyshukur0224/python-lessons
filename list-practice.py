# List bilan ishlash
# list methods
# 1. list.append(element)
# 2. list.insert(index, element)
# 3. list.remove(element)
# 4. list.pop(index?)
# 5. list.sort()
# cars = ['bmw', 'mersedec benz', 'volvo', 'damas', 'tesla', 'audi']
# # cars.sort() # alifbo(english) ketma-ketlik bo'yicha tartiblash
# # print(cars)
# # cars.sort(reverse=True) # reverse(teskari)
# # print(cars)
# sorted_list = sorted(cars)
# reversed_sort_list = sorted(cars, reverse=True)
# print(cars)
# print(sorted_list)
# print(reversed_sort_list)                    

# ages = [12, 98, 34, 65, 34, 76, 11 ]
# ages.sort() # o'sish tartibi
# print(ages)
# print(sorted(ages, reverse=True)) # kamayish tartibi

# # list.reverse()
# fruits =['pear', 'banana', 'apple', 'watermelon', 'lemon']
# fruits.reverse()
# print(fruits)
# print(len(fruits)) # 5

# # list() funksiyasi

# users = ['akmal', 'farzona', 'shodlik']
# students = list(('jamol', 'asal', 'kamol', 'zebo'))
# print(students)
# range() funksiyasi - ma'lum oraliqdagi sonlarni shakllantirish uchun ishlatiladi
# range(start, stop, step?)
# range(0,10)
# juft_sonlar = list(range(2, 21, 2))
# print(sonlar)
# print(juft_sonlar)

# narhlar = [12000, 22500, 23767, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh", arzon "Eng qimmat", qimmat, "Jami:", jami)

# ROYXATNI KESISH

# techs = ['AI', 'Robot', 'Python', 'DB', 'Chat GPT', 'Web']
# my_techs = techs[2:5]
# print(my_techs)
# print(techs[:4]) # Royxat boshidan 4 gacha kesadi (0, 1, 2, 3)
# print(techs[2:]) # 2-indexdagi elementdan boshlab ro'yxat oxirigicha kesib oladi    

# Dasturlash indexlash 0 dan 

# listda index 0 dan 

# people = [ 'Kumush', 'Akmal', 'Doston', 'Farida', 'Ozodbek']
# manfiy ixdexlash oxirdan boshlanadi (-1, -2, -3, -4)
# print(people[-1]) # Ozodbek
# print(people[-2]) # Farida
# print(people[-5]) # Kumush
# print(people[-4 : -2]) # ['Akmal', 'Doston']
# print(people[-3 :])  
# print(people[: -5])

# Ro'yxatdan nusxa olish

# sonlar = list(range(1,6)) # [ 1, 2, 3, 4, 5, ]
# sonlar2 = sonlar
# print(sonlar2)
# print(sonlar)
# shalow(sayoz) copy

# sonlar2.append(6)
# sonlar2.append(7)
# print(sonlar2)
# print(sonlar)
# deep(chuqur) copy

# sonlar3 = sonlar[:]
# print(sonlar3)
# sonlar3.append(6)
# print(sonlar3) # [1, 2, 3, 4, 5, ]
# print(sonlar)

# # Tuple - o'zgarmas ro'yxat
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys)
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# Amaliyot

#1
davlat = ['Ozbekiston', 'Turkiya', 'Rossia', 'Parij']
print(davlat)
print(len(davlat))
print(sorted(davlat))
print(sorted(davlat, reverse=True))
print(davlat)
davlat.reverse(  )

#
even_numbers = list(range(120, 1200, 2))
# [1, 2, ..., n]
print(even_numbers)
# boshidan 20 ta element
print(even_numbers[: 20])
# oxirdan 20 ta element
print(even_numbers[-20])
# o'rtasidan 20 t element
lenght = len(even_numbers)
start_index  = lenght // 2 - 10
end_index = lenght // 2 + 10
print(even_numbers[start_index : end_index])