import random

lowercase = "qwertyuiopasdfghjklzxcvbnm"
uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "0123456789"
special_characters = "~!@#$%^&*()_-+=?;:<>"

slimany = lowercase+uppercase+number+special_characters

random_password = "".join(random.sample(slimany, 10))

print(random_password)



