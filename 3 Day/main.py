height = int(input("Enter you'r height in cm:\t"))


bill = 0


# if height > 120:
if height >= 120:
# if height <= 120:
# if height < 120:
# if height != 120:
    print("You can ride rollercoster")
    
    age = int(input("Enter you'r age:\t"))
    
    if age < 12:
        bill += 5
    elif age <= 18:
        bill += 7
    else:
        bill += 12
    
    want_photo = input("do you want click photo?\t")
    
    if want_photo == "y":
        bill += 3
else:
    print("Please, wait till you'r height minimum 120 cm")
    

if bill > 0:
    print(f"Bill: ${bill}")