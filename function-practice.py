# Amaliyot
# 1. Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def tugilgan_yil_hisoblang(ism, yosh):
#     """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"""
#     yil = 2026 - yosh
#     print(f"{ ism }  { yil } - yilda tug'ilgan")

# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# tugilgan_yil_hisoblang(ism, yosh) 

# 2. Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kvadrat_kub_hisobla(son):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     kvadrat = son ** 2
#     kub = son ** 3
#     print(f"{ son } ning kvadrati: { kvadrat }, kubi: { kub }") 

# son = float(input("Son kiriting: "))
# kvadrat_kub_hisobla(son)

# 3. Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

# def juft_toq_hisobla(son):

#     if son % 2 == 0:
#         print(f"{ son } juft son")
#     else:
#         print(f"{ son } toq son")

# son = int(input("Son kiriting: "))
# juft_toq_hisobla(son) 

# 4. Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def kattasini_top(son1, son2):

#     if son1 > son2:
#         print(f"{ son1 } katta")
#     elif son2 > son1:
#         print(f"{ son2 } katta")
#     else:
#         print("Sonlar teng")    

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))    
# kattasini_top(son1, son2) 


# 5. Foydalanuvchidan x va y sonlarini olib, x ni y  darajasini hisoblab, natijani konsolga chiqaruvchi funksiya yozing.
# def daraja_hisobla(x, y):
#     natija = x ** y
#     print(f"{ x } ning { y } darajasi: { natija }")

# x = float(input("x ni kiriting: "))
# y = float(input("y ni kiriting: "))
# daraja_hisobla(x, y) 


# 6.  Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja_hisobla(x, y=2):
#     natija = x ** y
#     print(f"{ x } ning { y } darajasi: { natija }")

# x = float(input("x ni kiriting: "))
# daraja_hisobla(x)  

# 7. Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
# def bolinish_tekshir(son):
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{ son } { i } ga qoldiqsiz bo'linadi")
#         else:
#             print(f"{ son } { i } ga qoldiqsiz bo'linmaydi")

# son = int(input("Son kiriting: "))
# bolinish_tekshir(son) 

  