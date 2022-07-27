def count_vowels(str_a):
    cnt = 0
    # cnt += str_a.count('a')    
    # cnt += str_a.count('e')
    # cnt += str_a.count('i')
    # cnt += str_a.count('o')
    # cnt += str_a.count('u')

    vowels = 'aeiou'
    for vowel in vowels:
        cnt += str_a.count(vowel)
    
    return cnt
    #for i in range(len(str_a)):
        
if __name__ == "__main__":
    print(count_vowels('apple'))
    print(count_vowels('banana'))