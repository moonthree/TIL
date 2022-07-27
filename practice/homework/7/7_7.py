class collatz():
    cnt = 0
    # 생성자
    # def __init__(self, 매개변수):
    #     self.인스턴스 변수 = 매개변수
    def __init__(self, number):
        self.number = number
     
    # def 함수이름(self):
    #     로직
    def func(self):        
        result = self.number
        while result != 1:
            if collatz.cnt == 500:
                return -1
            if result % 2 == 0 :
                result = result / 2
            else:
                result = result * 3 + 1
            collatz.cnt += 1
        return collatz.cnt
    

if __name__ == '__main__':
    number = int(input())
    number_instance = collatz(number)
    print(number_instance.func())
