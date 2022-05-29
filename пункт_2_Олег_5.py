from random import randint
def format_numbers(phone_number:str)-> str:
    return '+{0}{1}{2}({3}{4}){5}{6}{7}-{8}{9}-{10}{11}'.format(*[i for i in phone_number if i.isdigit()][0:])


print(format_numbers(phone_number=str([randint(0, 9) for i in range(12)])))