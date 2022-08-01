def solution(N):
    if N == 0:
        return 0
    else:
        return solution(N//10) + (N%10)

if __name__ == "__main__":
    print(solution(987))