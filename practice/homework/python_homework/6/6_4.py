def blood(blood):
    count_blood = {}

    for i in blood:               # blood_types 리스트를 처음부터 꺼내서
        try: count_blood[i] += 1        # count_blood 빈 딕셔너리에 넣는다.
        except: count_blood[i] = 1      # 이때 count_blood에 이미 존재하면 try문이 실행되어 value에 +1을 하고 
                                        # count_blood에 없는 값이라면 except가 실행되어 value는 1로 저장된다.
    return count_blood

if __name__ == "__main__":
    blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
    print(blood(blood_types))