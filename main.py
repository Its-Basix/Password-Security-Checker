print('Enter a Password for Testing: ')
password = input()

length = len(password)

score = 0
message = []

if length < 8:
    message.append("The Password is too short!")
elif length <= 12:
    message.append("The Password's length is okay.")
    score += 1
else:
    message.append("The Password's length is great!")
    score += 2

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


print(score)
print(message)