import random

class Students():
    # 1. 초기화 메서드 작성
    # = 생성자 작성
    def __init__(self, student):
        self.student = student

    # 2. 학생들 인자에서 인자 n 명 만큼 랜덤으로 추출하여 return 하는 pick 함수 작성
    # 참고 - random.sample 함수를 검색해보세요.
    def pick(self, n):
        return random.sample(self.student, n)

    # 3. 랜덤으로 2명(명단의 수가 홀수면 한 팀은 3명) 매칭하여 리스트로 반환하는 함수 match_pair 작성
    def match_pair(self):
        pair_list = []
        while len(self.student) > 0:
            # 3명보다 적거나 같으면 니들끼리 짝 해라
            if len(self.student) <= 3:
                pair_list.append(self.student)
                break
            else:
                picked = self.pick(2)
                pair_list.append(picked)
                self.student.remove(picked[0])
                self.student.remove(picked[1])
        return pair_list

if __name__ == '__main__':
    students_list = ['김싸피', '금해피', '테스트', '철수킴', '박영희']
    students = Students(students_list)
    print(students.match_pair())
