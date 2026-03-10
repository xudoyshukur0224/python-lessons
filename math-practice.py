import math

# a = float(input("1-sonni kiriting:"))
# b = float(input("2-sonni kiriting:"))
# c = math.pow(a, 1 / 5)
# d = (a + b) * b
# e = 2 * b + a * b
# f = math.pow(a, 2 ) + math.pow(b, 2) + 2
# t = c  + math.pow( d / e, 1 / 4 ) * f 
# print( "%.2f" % t)

# a = int(input("1-sonni kiriting:"))
# b = int(input("2-sonni kiriting:"))
# c = int(input("3-sonni kiriting:"))
# x = float(input("4-sonni kiriting:"))
# z = 0.75
# d = 8.2 * math.pow(x, 2) + math.pow (math.fabs(math.pow(x, 3 ) + 3 * x ) + math.cos(x-2), 1/2)
# e = a / 4 + b / 3 + c / 2 + 1
# t = z + d / e 
# print("%.2f" % t) 

# a = int(input("1-sonni kiriting:"))
# b = int(input("2-sonni kiriting:"))
# c = int(input("3-sonni kiriting:"))
# d = int(input("4-sonni kiriting:"))
# x = float(input("5-sonni kiriting:"))
# f = a * math.pow(x, 2) + b * x + c 
# e = x * math.pow(a, 3) + math.pow(a, 2) +  math.pow(a, b - c )
# t = a * x +b 
# w = c * x + d + math.pow(2, c)
# p = f / e + math.cos(math.fabs(t / w))
# print("%.2f" % p)    

# 025-misol
import math

# a = int(input("1-sonni kiriting:"))
# x =float(input("2-sonni kiritng:"))
# b = math.sqrt(x - 1) + math.sqrt(x + 2) 
# c = math.log10(math.sqrt ( a * math.pow(x, 2) ) + 2)
# d = math.sqrt( math.sqrt(x  + 2) + math.sqrt(x + 24) + math.pow(x, 5))
# tt =( b + c) / d 
# print( "%.2f" % tt )

# a = int(input("1-sonni kiriting:"))
# x = float(input("2-sonni kiriting:"))
# y = float(input("3-sonni kiriting:"))
# d = math.exp( x * y) - x * math.sin  (a * x ) 
# f = math.pow (x, 2) + 2
# e = math.fabs(x) + 5 
# t = math.sqrt (math.log(math.pow(x, 2) + 2 ) + 5)
# w2 =math.sqrt(d - f / e )  + t 
# print("%.2f" % w2)

# a = int(input("1-sonni kiriting:"))
# x = float(input("2-sonni kiriting:"))
# b = x * math.sin(x /  2 + x/ 3 + x /  4)
# c = math.log10(math.pow(x, 2) -2 )+  math.pow(3 , a)
# d = math.cos(x + 3) * math.sin(x + 3) + 8
# bb1 = b + c / d
# print("%.2f" % bb1)

x = float(input("x ni kiriting:"))
y = float(input("y ni kiriting:"))
a = math.pow(x, 2) + 1
b =  x * y + math.pow(y, 2)
c = y + x * y  
d = math.fabs(x * y) + 5 
e = a / (math.pow(x, 2) + b / (math.pow(y, 2) + c / d ) )
f = 1 / (1 + math.cos(x) + 1 / math.sin(math.fabs(x)))
t11 = e + f 
print("%.2f" % t11)


