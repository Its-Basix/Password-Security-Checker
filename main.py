
print('Enter a Password for Testing: ')
password = input()

def fun_length(password):
    if length < 8:
        message.append("The Password is too short!")
    elif length <= 12:
        message.append("The Password's length is okay.")
        score += 1
    else:
        message.append("The Password's length is great!")
        score += 2
    return

def fun_strength(password):
    if any(c.islower() for c in password):
        score += 1
    else:
        message.append("Please add a lowercase character!")
    if any(c.isupper() for c in password):
        score += 1
    else:
        message.append("Please add an UpperCase character!")
    if any(c.isdigit() for c in password):
        score += 1
    else: 
        message.append("Please add some numbers")
    
    if any(not c.isalnum() for c in password):
        score += 1
    else: 
        message.append("Try Using some symbols.")

    return

def fun_common(password):
    common_passwords = ["password","password1","password123","123456","12345678","123456789","123123","111111","qwerty","qwerty123","abc123",
    "letmein","iloveyou","admin","welcome","monkey","dragon","sunshine","football","baseball","starwars","hello","guest","login","princess",
    "master","passw0rd","trustno1","654321" ]

    if password.lower() in common_passwords:
        message.append("This is a common password, Please select another one")
        score = 0
    return

def fun_checker(password):
    if score <= 3:
        result = "Weak Strength"
    elif score <= 5:
        result = "Medium Strength"
    else: 
        result = "Strong"
    return result

length = len(password)
score = 0
message = []
print("Score:", score)
print(fun_checker(password))
print("Feedback: ")
for msg in message:
    print("-", msg)
