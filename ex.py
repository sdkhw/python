x = 1
for i in range(5):
    x /= 6

print(x)

z = x * 100
print(z) # 0.01286 
x= x * 52000000 # 6687

print(x)


y = 52000000 * 0.01 # 1 %
print("1 % ", y)


# s = "True"
# b = s.lower() == "true"   # True

# print(b)


from distutils.util import strtobool

s = "True"
b = bool(strtobool(s))   # True


163

