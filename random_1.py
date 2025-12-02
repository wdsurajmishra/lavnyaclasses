import random

# def generate_alphanumeric_string(length=5):
#     characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     return ''.join(random.choice(characters) for _ in range(length))


# print(generate_alphanumeric_string())

# my_choice = random.choice([1,2,3,4,5,6])
# print(my_choice)



def check_result(user_choice):
    game_choices = ['Tiger', 'Dragon']
    
    if user_choice not in game_choices:
        return "Invalid choice. Please choose either 'Tiger' or 'Dragon'."

    computer_choice = random.choice(game_choices)

    if user_choice == computer_choice:
        return "You Win"
    else:
        return "You Lose"
    
user_choice = input("Choose Tiger or Dragon: ")     
print(check_result(user_choice))