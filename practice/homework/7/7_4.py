from cgitb import reset
from unittest import result


class Fee():
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance


    # 렌탈 비용 계산
    def get_total_rental(self):
        return self.time * 1200


    # 보험료 계산
    def get_total_insurance(self):
        return int(self.time//30 + 1) * 525

    
    # 주행 요금 계산
    def get_total_drive(self):
        result = 0
        if self.distance > 100:
            result += 100*170
            result += (self.distance-100) * 85
        else:
            result = self.distance*100

        return result
        
        

    def get_fee(self):
        result = self.get_total_rental() + self.get_total_insurance() + self.get_total_drive()
        return result


if __name__ == '__main__':
    time, distance = map(int, input('렌탈비용과 주행거리를 띄워쓰기로 구분하여 입력하세요 : ').split())
    fee_instance = Fee(time, distance)
    print(fee_instance.get_fee())