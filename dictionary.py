# data types (ma'lumot turlari)
# string, int, float, bool, dictionary
# Dictionery - lug'at
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "yellow",
    "price": 45000
} 
print(car)
print(type(car))

user = {
    "fullname" : "Xudoyshukur Baxtiyorov", # kalit (key) : qiymat (value)
    "email" : "xudoywukur6@gmail.com",
    "age" : 15,
    "is_student": False,
    "favourite_books": ['Atomic habits', "O'tgan kunlar", 'Dunyoni ishlari']

}
# key-value pair(kalit-qiymat juftligi)
# 1. Valuelarni olish (key orqali)
print(user['fullname'])
print(user['favourite_books'] )
print(user['age'])  
 
for book in user['favourite_books']:
    print(book) 

# 2. Yangi key-value qo'shish
user['is_married'] = False
user['hobbies'] = ['reading a book', 'watching a football match', 'playing computer games'] 
print(user)

# 3. Value o'zgartirish
user['age'] = 15
user['email'] = "xudoywukur6@gmail.com"
print(user)

# 4. Bo'sh lug'at(Empty dictionary)
talaba_1 = {}

talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursdagi student")

# 5. Key-value juftligini o'chirish
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)

# 6. get() metodi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
phone = telefonlar.get('vali') # vali kalit so'zining qiymatini olish
print(f"Alining telefoni: {phone}")
print(telefonlar.get('vali'))
print(telefonlar.get('akmal')) # mavjud bo'lmagan kalit so'z uchun None qaytaradi 