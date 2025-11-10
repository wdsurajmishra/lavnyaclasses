msg = """
This is a id card generator project.
"""
print(msg)

def generate_id_card(name, age, role):
    id_card = f"""
    -------------------------
            ID CARD
    -------------------------
    Name : {name}
    Age  : {age}
    Role : {role}
    -------------------------
    """
    return id_card

my_details = {
    "name":"",
    "age":"",
    "role":""
}

my_details["name"] = input("Enter Your Name: ").strip()
my_details["age"] = input("Enter Your Age: ").strip()   
my_details["role"] = input("Enter Your Role: ").strip()

print(generate_id_card(my_details["name"], my_details["age"], my_details["role"]))