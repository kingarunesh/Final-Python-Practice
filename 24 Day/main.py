#SECTION :      Old Method

# file = open("first.txt")
# print(file.read())
# file.close()



#SECTION :      new method

#NOTE :         Read File
with open("first.txt", mode="r") as file:
    print(file.read())


#NOTE :         Write File
with open("first.txt", mode="w") as file:
    file.write("First Text.")

#!      file not exit, creating auto new file
with open("a.txt", mode="w") as file:
    file.write("New File created...")


#NOTE :         Append Text
data = ["second", "third", "fourth", "fivth"]

with open("first.txt", mode="a") as file:
    for text in data:
        file.write(f"\n{text} Text.")

#!      file not exit, creating auto new file
with open("b.txt", mode="a") as file:
    file.write("New File created...")