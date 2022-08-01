class Doggy:
    nums_of_dogs = 0
    birth_of_dogs = 0
    
    # 생성자
    # def __init__(self, 매개변수):
    #     self.인스턴스 변수 = 매개변수
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.nums_of_dogs += 1
        Doggy.birth_of_dogs += 1
    
    # def 함수이름(self):
    #     로직
    def bark(self):
        return f'{self.species} {self.name}가 짖었다. 효과는 굉장했다.'

    # 소멸자
    def __del__(self):
        Doggy.nums_of_dogs -= 1
    
    @classmethod
    def get_status(cls):
        return f'태어난 개 : {cls.birth_of_dogs}마리, 현재 있는 개 : {cls.nums_of_dogs}마리'

    
dog1 = Doggy('골드', '골든 리트리버')
dog2 = Doggy('허슼', '허스키')
dog3 = Doggy('황구', '시고르자브종')

del dog2
print(dog3.bark())
print(Doggy.get_status())