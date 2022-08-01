class Alone:
    
    # 생성자
    # def __init__(self, 매개변수):
    #     self.인스턴스 변수 = 매개변수
    def __init__(self, participants):
        self.participants = participants

    # def 함수이름(self):
    #     로직
    def search_alone(self):
        for i in self.participants:
            cnt = 0
            for j in self.participants:
                if i == j:
                    cnt += 1
            if cnt == 1:
                return i


#if __name__ == '__main__':
if __name__ == '__main__':
    participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
    instance_participantes = Alone(participants)
    print(instance_participantes.search_alone())