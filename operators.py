num1 = 10
num2 = 5

# print(num1 + num2) 

num3 = num1 % num2

print("Output is ", num3)


# Assignment operator

num4 = 5
# num5 = num4 + 1/
num4 += 1
# print(num4)

# Comparison Operators

# print(num1 > num2)

my_name = "Prince"

# is_valid  = my_name == "prince" 
# is_valid  = my_name != "prince" 
# print(is_valid)

name = "Prince"
course = "ADCA"

# is_valid_student = name == "Prince" and course.lower() == "adca"
# print(is_valid_student)

# is_valid_student = name == "prince" or course.lower() == "adca"
# print(is_valid_student)/

# Identity Operators

is_krm_by_krm = name is "Prince"

# if is_krm_by_krm:
#     print("Shi chl rha hai") # jab true rahega 
# else:
#     print("Kram by kram bataiye")    

# Membership Operators



# print(is_krishna_availble)


my_email = "suraj@gmail.com"
is_valid_email = "@" in my_email and "." in my_email
print(is_valid_email)
my_tuple = ("SHivam", "Avinash")
students = ["Shivam", "Avinash", "Krishna", "Prince"]
is_krishna_availble = "Krishna Yadav" in students

int_num = 2
int_num = float(int_num)
print(int_num)