class Person:     
    count = 0
    def __init__(self, name, mbti):   # 인스턴스 변수 정의 // self는 자동으로 생략
        self.name = name        # 인스턴스 변수 - 각자 사용하는 변수
        self.mbti = mbti
        Person.count += 1

person1 = Person('지민', 'istp')
person2 = Person('태민', 'estp')

print(Person.count)             # 2