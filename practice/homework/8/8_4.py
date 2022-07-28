# 탑승객 수(passengers) 와 요금(fare)를 받는다.

class PublicTransport():
    passenger_cnt = 0
    total_fare = 0
    # 탑승객 수와 요금을 입력받아 초기화하는 메서드
    # def __init__~~~
    def __init__(self, passenger, fare):
        self.passenger = passenger
        self.fare = fare

    # 탑승 메서드
    # passenger 를 파라미터로 받음
    # 새로 탄 승객에 따라 총 요금에 추가
    def get_in(self, passenger):
        PublicTransport.passenger_cnt += passenger
        PublicTransport.total_fare += passenger * self.fare
        
    # 내리는 메서드
    # 승객 수만 감소
    def get_off(self, passenger):
        PublicTransport.passenger_cnt -= passenger

    # 현재 탑승중인 인원과 최종 수익을 출력
    def profit(self):
        pass
        print(f'현재 탑승중인 인원 : {PublicTransport.passenger_cnt}, 최종 수익 : {PublicTransport.total_fare}')

class Bus(PublicTransport):

    def __init__(self, limit, passenger, fare):
        self.limit = limit

        # 버스에서도 탑승객, 요금 인스턴스 변수 쓰고 싶다
        super().__init__(passenger, fare) 
    
    def test(self):
        print('self.limit = ', self.limit)
        print('self.passengers = ', self.passenger)
        print('self.fare = ', self.fare)
        print('self.total = ', self.total_fare)
    
    # override
    def get_in(self, passenger):
        if self.passenger + passenger > self.limit: 
            print('더이상 탑승할 수 없습니다.')
        else:
            self.passenger += passenger
            PublicTransport.passenger_cnt += passenger
            PublicTransport.total_fare += passenger * self.fare
            print(f'현재 탑승중인 인원 : {self.passenger}')

if __name__ == '__main__':
    # transport = PublicTransport(0, 100)
    # transport.get_in(20)
    # transport.get_in(10)
    # transport.get_in(40)
    # transport.get_off(30)

    bus = Bus(40, 0, 1200)
    bus.test()
    bus.get_in(20)
    bus.get_in(20)
    bus.get_in(30)
    bus.profit()

    
    #transport.profit() # 탑승인원 : 40 / 총 수익 : 7000