#딕셔너리 실습
# def a() : 기초
def a():
    dict_a = {'key1':'item1', 'key2':'item2'}
    print(dict_a) # {'key1': 'item1', 'key2': 'item2'}

    print(dict_a['key2']) # item2

    print(dict_a.keys())  # dict_keys(['key1', 'key2'])
    
    a = list(map(str, dict_a.keys()))
    print(a)        # ['key1', 'key2']
    print(a[0])     # key1
    print(a[1])     # key2
    
    b = list(map(str, dict_a.values()))
    print(b)        # ['item1', 'item2']
    print(b[0])     # item1
    print(b[1])     # item2

    c = list(map(str, dict_a.items()))
    print(c)        # ["('key1', 'item1')", "('key2', 'item2')"]
    print(c[0])     # ('key1', 'item1')
    print(c[1])     # ('key2', 'item2')
    print(type(c[0]))  # <class 'str'>

    print(type(dict_a)) # <class 'dict'>
#a()

# def b() : 딕셔너리의 키에 대한 반복 추출
def b() :
    dict_b = {'F': 3, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 8}
    for key in dict_b:
        print(key, dict_b[key])
        '''
        F 3
        A 1
        B 2
        C 3
        D 4
        E 8
        '''
    # F A B C D E 순서가 아닌 A B C D E F 순으로 
    # collections의 OrderedDict을 이용해서 키 순서대로 정렬하였다. 여기서 키의 크기순으로 정렬되는 것이다.
    from collections import OrderedDict
    ordered_dict = OrderedDict(sorted(dict_b.items()))
    print(type(ordered_dict))
    for key in ordered_dict.items():
        print(key)
    '''
    <class 'collections.OrderedDict'>
    ('A', 1)
    ('B', 2)
    ('C', 3)
    ('D', 4)
    ('E', 8)
    ('F', 3)
    '''
    # 딕셔너리의 키와 값을 동시에 참조하여 추출
    for key in dict_b.items():
        print(key, dict_b)
    '''
    ('F', 3) {'F': 3, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 8}
    ('A', 1) {'F': 3, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 8}
    ('B', 2) {'F': 3, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 8}
    ('C', 3) {'F': 3, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 8}
    ('D', 4) {'F': 3, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 8}
    ('E', 8) {'F': 3, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 8}
    '''
#b()

# def c() : 사전형 자료구조
def c():
    dict_c = {'id': 'microfun', 'name': 'song'}