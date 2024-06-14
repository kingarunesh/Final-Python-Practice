import os


clear = lambda: os.system("cls")
clear()


print("🙏 Sita Ram 🙏")

print()


a = 1

def fun():
    global a
    a = 2
    print(a)

print(a)
fun()
print(a)

print()

b = 1
print(b)

if True:
    b = 2
    print(b)

print(b)