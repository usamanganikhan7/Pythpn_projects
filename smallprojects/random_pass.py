import string
import random


s1 = string.ascii_lowercase

s2 = string.ascii_uppercase

s3 = string.digits

s4 = string.punctuation


pass_len = int(input("Enter the password length :"))

s = []

s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))


# print(s)


random.shuffle(s)

# print(s)


print("Your Password is ---> " ,"".join(s[0:pass_len]))