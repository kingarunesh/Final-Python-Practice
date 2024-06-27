import os


clear = lambda: os.system("cls")
clear()

#####################################################################################


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("Constructor is calling...")
    
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
        


user_1 = User(user_id="001", username="kingarunesh")

print(user_1.id)
print(user_1.username)
print(user_1.followers)



user_2 = User(user_id="002", username="aohan")
user_2.followers = 19

print(user_2.id)
print(user_2.username)
print(user_2.followers)

print()

user_1.follow(user=user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)