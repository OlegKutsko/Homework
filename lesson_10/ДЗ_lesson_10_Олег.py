import datetime

class User:
    def __init__(self, name, surname, age, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self. profession = profession

    @property
    def email(self):
        return f'{self.name + "." + self.surname + "@email.com"}'

    @property
    def birth_year(self):
        return datetime.datetime.today().year - int(self.age)


    def create_doctor(self):
        global User_1
        User_1 = User(name='' , surname='', age='', country='', gender='', profession="Doctor")
        return print(User_1)


    def create_policeman(self):
        User_2 = User(name='' , surname='', age='', country='', gender='', profession="Policeman")
        return print(User_2)


    def create_teacher(self):
        User_3 = User(name='', surname='', age='', country='', gender='', profession="Teacher")
        return print(User_3)

