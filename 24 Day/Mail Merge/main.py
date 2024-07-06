placeholder = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    
    
with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()
    
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(placeholder, stripped_name)
        
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)