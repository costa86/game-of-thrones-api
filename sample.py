from re import A
import re


# def create_comment_id(size=6):
#     upper_letters = string.ascii_uppercase
#     digits = string.digits
#     id = "".join(random.choice(upper_letters + digits) for i in range(size))
#     return id 
a = "t"



def hi(a):
    try:
        b = int(a)
        if b not in range(1,9):
            return "no"
    except:
        return "inv"

print(hi(a))