# step 1 - take user birthday input
# step 2 - calculate the total days lived

from datetime import datetime


def calculate_days_lived(birthday_str):
    # Convert the birthday string to a datetime object
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

    # Get the current date
    current_date = datetime.now()

    # Calculate the difference in days
    days_lived = (current_date - birthday).days

    return days_lived

def calculate_left_days(birthday_str, life_expectancy=60):
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
    current_date = datetime.now()
    age_in_days = (current_date - birthday).days
    total_life_days = life_expectancy * 365
    days_left = total_life_days - age_in_days
    return days_left

def total_day_left_for_next_birthday(birthday_str):
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
    current_date = datetime.now()
    
    # Calculate next birthday
    next_birthday_year = current_date.year
    if (current_date.month, current_date.day) > (birthday.month, birthday.day):
        next_birthday_year += 1
    
    next_birthday = birthday.replace(year=next_birthday_year)
    
    # Calculate days left until next birthday
    days_left = (next_birthday - current_date).days
    
    return days_left


user_birthday = input("Enter your birthday (YYYY-MM-DD): ")
# days = calculate_days_lived(user_birthday)
# total = calculate_left_days(user_birthday)
# print(f"You have lived for {days} days.")
# print(f"You have {total} days left to live based on a life expectancy of 60 years.")

days_until_birthday = total_day_left_for_next_birthday(user_birthday)
print(f"Days left until your next birthday: {days_until_birthday + 1} days.")