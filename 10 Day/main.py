import os


clear = lambda: os.system("cls")
clear()


print("Ram Ji and Sita Ji - Hanuman Ji")


print()

def full_name(first_name, last_name):
    """
        first_name + last_name = full_name
    """
    
    print("Hello")
    
    if first_name == "" or last_name == "":
        return "Invalid Input"
    
    return f"{first_name} {last_name}"

f_name = full_name(first_name="Arunesh", last_name="kumar")
print(f_name)

full_name(first_name="Arunesh", last_name="kumar")

print()

f_name = input("First Name:\t")
l_name = input("Last Name:\t")

print(full_name(first_name=f_name, last_name=l_name))

full_name()