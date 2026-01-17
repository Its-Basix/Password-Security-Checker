from math import log2

def fun_length(password):
    score = 0
    message = []
    length = len(password)
    if length < 8:
        message.append("The Password is too short!")
    elif length <= 12:
        message.append("The Password's length is okay.")
        score += 1
    else:
        message.append("The Password's length is great!")
        score += 2
    return score, message

def fun_strength(password):
    score = 0
    message = []
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

    return score, message

def fun_common(password):
    common_passwords = ["password","password1","password123","123456","12345678","123456789","123123","111111","qwerty","qwerty123","abc123",
    "letmein","iloveyou","admin","welcome","monkey","dragon","sunshine","football","baseball","starwars","hello","guest","login","princess",
    "master","passw0rd","trustno1","654321" ]
    score = 1
    message = []
    if password.lower() in common_passwords:
        message.append("This is a common password, Please select another one")
        score = 0
    return score , message

def fun_checker(score):
    if score <= 3:
        result = "Weak Strength"
    elif score <= 5:
        result = "Medium Strength"
    else: 
        result = "Strong"
    return result

def entropy_size(password):
    entropy = 0
    if any(c.islower() for c in password):
        entropy += 26
    if any(c.isupper() for c in password):
        entropy += 26
    if any(c.isdigit() for c in password):
        entropy += 10
    if any(not c.isalnum() for c in password):
        entropy += 32
    return entropy

def entropy_calculator(password):
    length = len(password)
    size = entropy_size(password)
    entropy = length * log2(size)
    return entropy

def entropy_feedback(entropy):
    message = []
    if entropy < 28:
        message.append("Very Weak Entropy")
    elif entropy < 36:
        message.append("Weak Entropy")
    elif entropy < 60:
        message.append("Reasonable Entropy")
    elif entropy < 128:
        message.append("Strong Entropy")
    else:
        message.append("Excessive Entropy")
    return message




def main():
    print('Enter a Password for Testing: ')
    password = input()
    length_score, length_message = fun_length(password)
    strength_score, strength_message = fun_strength(password)
    common_score, common_message = fun_common(password)
    score = length_score + strength_score
    if common_score == 0:
        score = 0
    message = length_message + strength_message + common_message
    print("Score:", score)
    print(fun_checker(score))
    print("Feedback: ")
    for msg in message:
        print("-", msg)
    print("\n")

    # Entropy
    entropy = entropy_calculator(password)
    entropy_message = entropy_feedback(entropy)
    print("The Entropy is: ", entropy)
    for msg in entropy_message:
        print("-", msg)
    


    pass

if __name__ == "__main__":
    main()

