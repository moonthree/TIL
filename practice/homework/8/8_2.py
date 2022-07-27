class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(self, name, year):
        self.name = name
        self.year = year
        self.age = 2022 - self.year

    def check_age(self):
        if self.age > 19:
            return True
        else:
            return False


person1 = Person('아이유', 20)
person2 = Person.details('이찬혁', 17)

print(person1.check_age())

    