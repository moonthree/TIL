class Person:
    name = 'lee'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()           # lee p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수 'lee'가 출력됨

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()           # lee
p2.name = 'kim'     # p2의 name에 인스턴스 변수 정의함
p2.talk()           # kim   # p2의 name에 인스턴스 변수가 정의되어 있으니 바로 인스턴스 변수 출력

print(Person.name)  # lee
print(p1.name)      # lee  Person의 클래스 변수 name의 값이 kim으로 변경된 것이 아닌
print(p2.name)      # kim  p2 인스턴스의 이름 공간에 name이 kim으로 저장된 것이므로
                    #      Person.name과 p1.name은 lee가 출력됨