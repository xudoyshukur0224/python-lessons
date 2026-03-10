# String methods 
# ism = "James"
# familiya ="Lebron"
# ism_sharif = f"{ism} {familiya}"
#upper
# print(ism_sharif.upper())
# print("Adminjon".upper())
# print(ism_sharif.lower())
# print("Admin Janoblari".lower())
# print(ism_sharif) #James Lebron
# ism_sharif = ism_sharif.upper()
# print(ism_sharif) #JAMES LEBRON 
# title() va capitalize()
# print('donald trump'.title())
# print(ism_sharif.capitalize())
# print('vladamir putin'.capitalize())
# print(ism_sharif.title())

# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman") 
# print(meva)
# meva = meva.strip()
# print(meva)

# input()
# username1 = 'norboyeva001'
# print("Kumushxonning instagram nickname:" +  username1)
# username2 = input("Iltimos, github username kiriting:")
# print(f"Sizning github usernameingiz: {username2}")

# firstname = input("Ismingizni  kiriting: ")
# lastname = input("Familiyangizni kiritng: ")
# print(f"Sizning ism famimliyangiz: {firstname} {lastname}")

#  kocha = input("Ko'changizni kiriting:")
#  mahalla = input("Mahallangizni kiritng:")
#  tuman = input("Tumaningizni kiriting:")
#  viloyat = input ("Viloyatingizni kiriting:")
#  print(f"{kocha} kochasi, {mahalla} mahalllasi, {tuman}, tumani, {viloyat} viloyati ")

# #   print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
# #        tuman + " tumani,\n" + viloyat + " viloyati")

# manzil = (kocha + " ko'chasi," + mahalla + " mahallasi," +  tuman + " tumani," + viloyat + " viloyati")
     
# print(manzil.title())
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.strip())

#Amaliyot
# son = int(input('Iltimos, son kiriting'))
# xabar1 = str(son) + " ning kvadrati " + str(son ** 2) + " ga teng"
# xabar2 = str(son) + " ning kvadrati " + str(son ** 3) + " ga teng"
# print(xabar1)
# print(xabar2)

# age = int(input("Yoshingizni kiriting:"))
# yil = 2025- age
# xabar = f"Siz {yil} yilda tug'lgansiz"
# print(xabar)

# a= float(input("Birinchi sonni kiriting:"))
# c = float(input("Ikkinchi sonni kiriting:"))
# print(f"{ a } + { c } = { a + c }")
# print(f"{ a } - { c } = { a - c }")
# print(f"{ a } * { c } = { a * c }")
# print(f"{ a } / { c } = { a / c }")

#Amaliyot
# a = int(input("Birinchi tomonni kiriting:"))
# b = int(input("Ikkinchi tomonni kiritng:"))
# c = int(input("Uchinchi tomonni kiriting:"))
# p = (a+b+c)/2
# s = p*(p-a)*(p-b)*(p-c)
# xabar = f"Uchburchakning tomonlari {a}, {b}, {c} yuzi {s ** 0.5} ga teng"
# print(xabar)


# 1-doiraning radiusi: 3
# 2-doiraning radiusi: 7
# 3-doiraning radiusi: 1
# formula: s = math.pi * r ** 2
# Natija: Radiusi 3ga

import math
# r1 = int(input("1-doiraning radiusini kiriting:"))
# r2 = int(input("2-doiraning radiusini kiriting:"))
# r3 = int(input("3-doiraning radiusini kiriting:"))
# s1 = math.pi * r1 ** 2
# s2 = math.pi * r2 ** 2
# s3 = math.pi * r3 ** 2 
# print(f"Radiusi {r1} ga teng doiraning yuzi: {s1} ga teng")
# print(f"Radiusi {r2} ga teng doiraning yuzi: {s2} ga teng")
# print(f"Radiusi {r3} ga teng doiraning yuzi: {s3} ga teng")