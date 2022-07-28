class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        age = 2022 - year + 1
        return cls(name, age)
    
    def get_info(self):
        print(f'이름 : {self.name} / 나이 : {self.age}')

    def check_age(self):
        if self.age > 19:
            return True
        else:
            return False


person1 = Person('아이유', 20)
person2 = Person.details('이찬혁', 2004)

person1.get_info()
person2.get_info()
print(person1.check_age())
print(person2.check_age())