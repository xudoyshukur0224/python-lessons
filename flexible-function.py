# def sum_list(lst):
#     s = 0
#     for number in lst:
#         s += number

#     return s
# sum_list([15, -5, 0, 8, 7])
# print(sum_list([15, -5, 0, 8, 7]))



# flexible (moslashuvchan) function
# *args, **kwargs
# def summa(*sonlar):
#     print(sonlar)
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son

#     return yigindi
# print(summa(8, 9, 12, -5, 89, 100))


# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)

# my_function("Hello", "Emil", "Tobias", "Linus")

# def summa(x,y, *sonlar):
#    return x + y + sum(sonlar)

# print(summa( 1, 7, 1, -5, -2))


# **kwargs usuli
# def avto_info(kompaniya, model, **malumotlar):
#     print(malumotlar)
#     print(type(malumotlar))
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar

# print(avto_info("GM Uzbekistan", "Onix", rang = 'qora', yil = 2025))
# print(avto_info = avto_info("Kia", "K5", rang='qizil', narh=35000))

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# Amaliyot
# 1. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# def multiple(*numbers):
#     result = 1
#     for number in numbers:
#         result *= number

#     return result
# print(multiple(5, 52 ,63, 12, 5))


# # 2.
# def talabalar(ism,familiya, **malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familiya'] = familiya
#     return malumotlar
# print(talabalar())


         
def find_max(*numbers):
    if len(numbers) == 0:
        return None
    
    max_son = numbers[0]
    for son in numbers:
        if son > max_son:             
            max_son = son
    
    return max_son

                             
print(find_max(4, 8, 2, 10, 6))   
print(find_max(-5, -2, -10))      
print(find_max())

