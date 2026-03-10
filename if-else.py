# Tarmoqlanish operatori. if -agar, else- aks holda
# age = int(input("Yoshingizni kiriting:"))
# if age < 18:
#     print("Siz hali yoshsiz, kirishga ruxsat yo'q")
# else: 
#     print("Sizga kirishga ruxsat bor") 

#       
# age = int(input("Yoshingizni kiriting:"))
# if age < 16:
#     print("Siz hali yoshsiz sizga passport olishga ruxsat yo'q")
# else:
#     print("Tabriklaymiz siz passport olishingiz mumkin")

# Amaliyot
# 1-mashq
# son = int (input("Xohlagan sonni kiriting: "))
# if son > 0:
#     print("Musbat son")
# elif son == 0:
#     print("Son nolga teng")
# else:
#     print("Manfiy son")

# 2-mashq
# son = int (input("Xohlagan sonni kiriting: "))
# if son % 2 ==0:
#     print("Juft son")
# else:
#     print("Toq son")

# 3-mashq
# son = int (input("Xohlagan sonni kiriting: "))
# if son % 2 == 0 and son % 3 == 0:
#     print("6 ga bolinadi")
# else:
#     print("6 ga bolinmaydi")

# 4-mashq
# a = int (input(" 1-sonni kiriting: "))
# b = int (input(" 2-sonni kiriting: "))
# c = int (input(" 3-sonni kiriting: "))
# if a + b > c and a + c > b and b + c > a:
#     print("Uchburchak yasash mumkin")
# else:
#      print("Uchburchak yasash mumkin emas")

# 5 - mashq
# a = int (input(" 1-sonni kiriting: "))
# b = int (input(" 2-sonni kiriting: "))
# if a <  b :
#     print(a)
# else:
#     print(a, b )
# 6-mashq
# a = int (input(" 1-sonni kiriting: "))
# b = int (input(" 2-sonni kiriting: "))
# if a <=  b:
#     a = 0
#     print(a, b )
# else:
#     print(a, b)

# 7-mashq
# import math
# a = int (input(" 1-sonni kiriting: "))
# b = int (input(" 2-sonni kiriting: "))
# c = int (input(" 3-sonni kiriting: "))
# if a >= b >=c:
#     a = a*2
#     b = b*2
#     c = c*2
#     print(a, b, c)      
# else:
#  print(int(math.fabs(a)), int(math.fabs(b)), math.fabs(c))

# 8-mashq
# x = int (input(" x sonni kiriting: "))
# y = int (input(" y sonni kiriting: "))
# a = 2 * x * 2 * y
# b = (x + y) / 2
# if x > y:
#     x = a
#     y = b
# else:
#     y = a
#     x = b

# print(x, y)

# 9-mashq
# a = int (input(" 1-sonni kiriting: "))
# b = int (input(" 2-sonni kiriting: "))
# c = int (input(" 3-sonni kiriting: "))
# if a < b < c:
#     print("Yes")
# else:
#     print("No")

# 15, -5, 0, 104, 189, 89, 77.
# print(max(15, -5, 0, 104, 189, 89, 77))
# print(min(15, -5, 0, 104, 189, 89, 77))

# 10-mashq
# x = int (input("x sonni kiriting: "))
# y = int (input("y sonni kiriting: "))
# z = int (input("z sonni kiriting: "))
# a = max(x+ y+ z,  x, y, z)
# b = min(x + y /2, x, y, z)**2
# print("%.2f" % a, "%.2f" % b) 

import math 
 
# x = float (input("x sonni kiriting: ")) 
# y = float (input("y sonni kiriting: ")) 
# if x < 0 and y < 0: 
#     print(math.fabs(x), math.fabs(y)) 
# elif x < 0 or y < 0:  
#     x = x + 0.5 
#     y  = y + 0.5 
#     print(x, y) 
# else: 
#     print(x, y)           

# a = int (input(" 1-sonni kiriting: "))
# b = int (input(" 2-sonni kiriting: "))
# c = int (input(" 3-sonni kiriting: "))   
# D = b**2 - 4*a*c
# if D > 0:
#     x1 =(- b + math.sqrt(D)) / (2 * a)
#     x2 = (- b - math.sqrt(D)) / (2 * a)
#     print( "%.2f" % x1, "%.2f" % x2)
# elif D == 0:
#     x = - b / (2 * a)
#     print( "%.2f" % x)
# else:
#     print("NO")

# x = int (input(" 1-sonni kiriting: "))
# y = int (input(" 2-sonni kiriting: "))
# z = int (input(" 3-sonni kiriting: "))
# if x > 0:
#     x = x**2
# if y > 0:
#     y = y**2
# if z > 0:
#     z = z**2
    
# print(x, y, z)  

# x = float (input(" x-sonni kiriting: "))
# y = float (input(" y-sonni kiriting: "))
# z = float (input(" z-sonni kiriting: "))
# if 1 <= x <= 3:
#    print(x)
# if 1 <= y <= 3:
#    print(y)
# if 1 <= z <= 3:
#    print(z)

# a = float (input(" 1-sonni kiriting: "))
# b = float (input(" 2-sonni kiriting: "))
# c = float (input(" 3-sonni kiriting: "))
# d = float (input(" 4-sonni kiriting: "))
# x = max(a, b, c, d)
# y = min(a, b, c, d)
# if a <= b <= c <= d:
#     print(x, x, x, x)
# else:
#     print(y, y, y, y) 
