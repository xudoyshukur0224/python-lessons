# def add_numbers(a, b):
#     print(a + b)

# add_numbers(5, 10) # 15
# add_numbers(3, 7) # 10

# Qiymatni qaytaruvchi funksiya
# return - funksiya ichida natija qaytarish uchun ishlatiladi
# def add_numbers(x, m):
#     return x + m  

# print(add_numbers(15, 15)) # 30
# result = add_numbers(20, 30) 
# print(result) # 50

# print("""hey, how are you?""")   
# print("a" * 3 )  # aaa
# print("m" + 5 ) 
# TypeError: can only concatenate str (not "int") to str
# print("a" / 5 ) 
# TypeError: can only concatenate str (not "int") to str

# son = int(input("Son kiriting: "))
# if son % 2 == 0:
#     print("Bu son juft son")
# else:
#     print("Bu son toq son") 

# def isEven(number):
#     if number % 2 == 0:
#         return "Juft"
#     else:
#         return "Toq"

# print(isEven(4)) # Juft
# print(isEven(7)) # Toq 

# Ternary operatori yordamida qisqaroq yozish 
# def isEven(number):
#     return "Juft" if number % 2 == 0 else "Toq"
# print(isEven(4)) # Juft
# print(isEven(7)) # Toq   

# age = int(input("Yoshingizni kiriting: "))

# print("Siz, endi kattasiz") if age >= 18 else print("Siz, hali yoshsiz") 

# Unli harflar (a, e, i, o, u)
# Example: "salom" => 2 ta unli harf bor (a, o)
# "python" => 1 ta unli harf bor (o)
# "bbb" => 0 ta unli harf yoq

vowels = "aeiou"
def count_vowels(word):
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

print(count_vowels("sAlom")) # 2
print(count_vowels("python")) # 1
print(count_vowels("bbb")) # 0 