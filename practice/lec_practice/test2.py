class Circle():
    pi = 3.14           # 클래스 변수 정의

    def __init__(self, r):
        self.r = r      # 인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi)        # 3.14
print(c1.pi)            # 3.14
print(c2.pi)            # 3.14

Circle.pi = 5           # 클래스 변수 변경
print(Circle.pi)        # 5
print(c1.pi)            # 5
print(c2.pi)            # 5

c2.pi = 5               # 인스턴스 변수 변경
c1.a = 6
print(Circle.pi)        # 3.14 (클래스 변수)
print(c1.pi)            # 3.14 (클래스 변수)
print(c1.a)
print(c2.pi)            # 5 (새로운 인스턴스 변수가 생성됨)
print(c2.pi * c2.r)