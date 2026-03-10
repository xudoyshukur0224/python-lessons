import math
# Loop - sikl
# 1. for loop 
# 2. while loop 
# students = ["Charos", "Kumush", "Akmal", "Ozodbek", "Farida", "Asal" ]
# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])
# for student in students:
#     print(f"Hurmatli {student}, sizni interviewga taklif qilamiz.")
#     print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi")
     

# nums = list(range(1, 11))
# for number in nums:
#       print(number)   
#      print(f"{number} sonining kvadrati {number ** 2} ga teng")


# sonlar = list(range(20))
# start_default_value = 0
# print(sonlar) # [0, 1, ..., 18, 19]
# [0, 1, 4, 9, 16, ..., 324, 361]
# sonlar2 = []
# for son in sonlar:
#      sonlar2.append(son **   2)

# print(sonlar2)

# 2 -usul
# for index in range(len(sonlar)):
#      print(index) # element indexi
#      print(sonlar[index]) # element

# 1-marta => index = 0 => sonlar[0] = 0 
# 2-marta => index = 2 => sonlar[2] = 2
# 3-marta => index = 3 => sonlar[3] = 3
# ...
# 20-marta => index = 19 => sonlar[19] = 19

# Amaliyot:
#1. 1 dan 101 gacha bo'lgan sonlarni chiqaring
# sonlar3 = list(range(1, 101))
# for element in sonlar3:
#      print(element)

# for number in range(1, 101):
#      print(number) 

# Amaliyot:

# ismlar =  ["Xayitboy", "Aslbek", "Akmal", "Ozodbek", "Xursandbek" ]
# for ism in ismlar:
#     print(ism)

# print(f"Kod {len(ismlar)} marta takrorlandi")

# sonlar = list(range(10, 100))
# for son in sonlar:
#     print(son ** 3)

# kinolar = []
# for n in range(5):
#    kinolar.append(input(f"{n+1} - kinoni kiriting: "))
# print(kinolar)

# inson_soni = int(input("nechta odam bn uchrashdingiz? "))
# insonlar = []
# for n in range(inson_soni):
#      inson =input (f"{n+1} - insonni ismini kiriting: ")
#      insonlar.append(inson)
# print(insonlar)

# Nechta do'stingiz bor?
# 1-do'stingiz ismi: VAli
# 2-do'stingiz ismi: Ali

# 4ta o'zingiz yoqtirgan telefonni kiritish topshiriq
# 1-siz yoqtirgan telefon nomini kiriting:
# 2-siz
# 3-siz
# Siz yoqtirgan telefonlar ro'yxati: ["iPhone 17 Pro Max orenge", "S 25 ultra"]

# dostlar_soni = int(input("Nechta do'stingiz bor? "))
# dostlar = []
# for n in range(dostlar_soni):
#     dost = input(f"{n+1} - dostingiz ismi: ")
#     dostlar.append(dost)

# print(dostlar)

# input("4ta yoqtirgan telni kiriting: ")
# telefon = []
# for n in range(4):
#     tel = input(f"{n+1} - telefonni kiriting: ")
#     telefon.append(tel)
# print(telefon)

# sonlar = [69, 18, 89, 12, 75, 82, 5, 26 ]
# min_value = min(sonlar)
# results = []
# for son in sonlar:
#     results.append(son / min_value)
    
# print(results)             
# [13.8, 3.6, ... 5.2]
# print(sum(sonlar))
# s = 0
# for son in sonlar:
#     s += son # s = s + son
# print(s) 

# s = 0
# for son in range(2, 50, 2):
#     s += son
# print(s)

# kopaytma = 1
# s = 0
# for son in range(1, 20, 2):
#     kopaytma *= son 
#     s += son 
# print(kopaytma / s)

# nums = [24, 50, 72, 96, 95]
# s = 0 
# for son in nums:
#    s += son ** 2 
# print(s)

# nums = [24, 50, 72, 96, 95]
# s = 0
# for son in nums:
#     s += son
#     yigindi = s / len(nums)
# print(yigindi)

# print(000000000 = 000000000)

# nums = [ 12, -5, 15, 89, -75, -18]                                                                       
# musbat elementlar 
# manfiy elementlar
# s = 0
# k = 1
# for son in nums:
#     if son > 0 :
#         s += son
#     else:
#         k *= son

# print(s)
# print(k)

# kopaytma = 1
# s = 0 
# for n in range(1, 20, ):
#     if n % 2 ==0:
#         kopaytma *= n 
#     else:
#         s += n   
# print(kopaytma / s)

# nums = [ 12, -5, 15, 89, -75, 18]
# s = 0
# for son in nums:
#     s += son
#     yigindi = s / len(nums)
# print(yigindi) 

# kopaytma = 1
# nums = [ 12, -5, 15, 89, -75, 18]
# for m in nums:
#      kopaytma *= m 
# ortacha = math.pow(kopaytma, 1/len(nums))
# print(ortacha)   

# numbers = [7, 97, -58, 90]
# s = 0
# counter = 0
# for son in numbers:
#     if son % 2 == 0:
#          s += son
#          counter += 1
# print(s / counter)
# number = [97, 97, -92, 14, 22]
# s = 0
# for n in number:
#     if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
#      s += n
# print(s)  

# son =[44, 34, 42, 83, 43, 64]
# k =1
# for n in son:
#     if n % 2 == 0 or n % 5 == 0:
#          k *= n
         
# print(math.sin(k))

# son = [93, 89, -90, 74, 62, -83, 58, 15, -37]
# s = 0
# c = 0
# for n in son:
#     if n < 0:
#       s += n
#       c += 1
# print(s / c)


# M = int(input("M sonni kiriting: "))
# sonlar = [12, 88, 30, 87 ]
# s = 0
# for n in sonlar:
#     if n > M:
#       s += n
# print(s)

# 115
# M = int(input("M sonni kiriting: "))
# nums = [85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34]
# s = 0
# for n in nums:
#     if M > n:
#         s += n ** 2
# print(s) 

# 118
# nums = [76, 12, 51, 50, 98]
# s = 0
# counter = 0
# for num in nums:
#     if num % 2 == 1:
#         s += num
#         counter  += 1
# print(s/counter)


# 122
# k = 0
# s = 0
# nums = [44, 59, -75, 73]
# for n in nums:
#     s += n
#     k += n ** 2
# ortacha = (s / len(nums))
# print(k)
# print(ortacha)
 
# 126
# numbers = [7, 24, -5, 23, 99, -3, 24, 51]
# s = 0
# for number in numbers:
#     s += number
# average_value = s / len(numbers)
# log_value = math.log(average_value)
# print(log_value)

# for index in range(len(numbers)):
#     if numbers[index ] < 0:
#         numbers[index] = log_value
        
# print(numbers)  

# 127
# numbers = [46, 23, -52, 34, 6, -18, 52]
# min_value = min (numbers)
# for index in range(len(numbers)):
#      if numbers[index] < 0:
#           numbers[index] = min_value ** 2

# print(*numbers) 

# 110
# m = int(input("M sonni kiriting: "))
# k = int(input("K sonni kiriting: "))
# numbers = [7, 11, 83, 18, 31, ]
# kopaytma = 1
# for n in numbers:
#     if n == k or n == m:
#         kopaytma *= n
# print(kopaytma)

# 104
# sonlar = [74, 0, 1, 33]
# min_value = min(sonlar)
# last_element = sonlar[-1]
# min_index = sonlar.index(min_value)

# sonlar[min_index], sonlar[-1] = last_element, min_value
# sonlar[-1] = min_value
# print(*sonlar)   

# 124
# k = int(input("Element o'rnini kiriting: "))
# numbers = [29, 50, -14, 4, 27, -56]
# max_value = max(numbers)  
# max_index = numbers.index(max_value)
# numbers[max_index] = numbers[k - 1]
# numbers[k - 1] = max_value
# print(numbers)

a = 5; b = 3
# natija: a = 3; b = 5
# 1-usul:
# temporary variable - vaqtinchalik o'zgaruvchi 
# c = a # 5 
# a = b # 3
# b = c # 5
# print(a, b) 

# 2-usul:
# a, b = b, a
# print(a, b)
    
# 3-usul:
# [a, b] = [b, a]
# print( a, b )