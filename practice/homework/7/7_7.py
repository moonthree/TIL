class collatz():
    cnt = 0
    # 생성자
    # def __init__(self, 매개변수):
    #     self.인스턴스 변수 = 매개변수
    def __init__(self, number):
        self.number = number
     
    # def 함수이름(self):
    #     로직

# 함수 하나로 처리
    # def func(self):        
    #     result = self.number
    #     while result != 1:
    #         if collatz.cnt == 500:
    #             return -1
    #         if result % 2 == 0 :
    #             result = result / 2
    #         else:
    #             result = result * 3 + 1
    #         collatz.cnt += 1
    #     return collatz.cnt

# 분리
    # 짝수 계산    
    def even_n(self):
        self.number = self.number / 2
        collatz.cnt += 1
        return self.number
    
    # 홀수 계산
    def odd_n(self):
        self.number = self.number * 3 +1
        collatz.cnt += 1
        return self.number

    # 판단
    def judge(self):        
        while self.number != 1:
            if collatz.cnt == 500:
                return -1
            if self.number % 2 == 0 :
                collatz.even_n(self)
            else:
                collatz.odd_n(self)
        return collatz.cnt

if __name__ == '__main__':
    number = int(input())
    number_instance = collatz(number)
    print(number_instance.judge())
