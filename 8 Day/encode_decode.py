import os

clear = lambda: os.system("cls")
clear()


#SECTION :      Project Code Start

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

print("welcome to 'encode' and 'decode' python script.")

flag = True

while flag:
    encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\t")
    message = input("Type your message:\t")
    shift = int(input("Type the shift number:"))

    def fun(message, shift, operation_type):
        result = ""
        
        for i in message:
            if operation_type == "encode":
                result += alphabets[alphabets.index(i) + shift]
            elif operation_type == "decode":
                result += alphabets[alphabets.index(i) - shift]
    
        print(result)
        
    fun(message=message, shift=shift, operation_type=encode_decode)
    
    want_continue = input("Type 'y' if you want to go again. Otherwise type 'n': ")
    if want_continue == "n":
        flag = False