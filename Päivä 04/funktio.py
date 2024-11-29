# def greet(name, age):
#     print('Moi', name)
#     print('Sinun ikasi on', age)

# greet('Christian', 50)
# greet('Simo', 25)
# #greet(20, 'Anna')
# #greet()

# def laske_summa(luku1, luku2):
#     return luku1 + luku2

# laske_summa(3, 5)
# print(laske_summa(1, 2))

def A():
    global i
    i = 3
    print(i)
    l[0] = 10
    print(l)

l = [1, 2, 3]
i = 5
A()
print(i)
print(l)