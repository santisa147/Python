text = "python is easy and python is powerful"
words_text = text.split()
repeat_words = {word: words_text.count(word) for word in words_text if words_text.count(word) > 0}
print(repeat_words)

numbers = [1,2,2,3,4,4,5]
nbr = []

for num in numbers:
    if num not in nbr:
        nbr.append(num)
print(nbr)
#findMax
numbers = [10, 3, 25, 7]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
        
print(max_num)       

def check_password(password):
    if len(password) < 8:
        return "Invalid"
    elif not any(char.isdigit() for char in password):
        return "Invalid"
    else:
        return "Valid"
    
print(check_password("pass1234"))
print(check_password("password"))


users = [
    {"name": "Juan", "age": 17},
    {"name": "Ana", "age": 22},
    {"name": "Pedro", "age": 15},
]
older_than_18 = [user for user in users if user["age"] > 18]
print(older_than_18)