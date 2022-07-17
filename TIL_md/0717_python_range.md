# range

### range 함수 : 연속된 숫자(정수를) 만들어 줌

| range(n) | 0 이상 n 미만인 수를 차례로 나열하는 수열 |
| --- | --- |
| range(a, b) | a 이상 b 미만인 수를 차례로 나열하는 수열 |
| range(a, b, step) | a 이상 b 미만인 수를 step 간격으로 나열하는 수열 |

### 1. range(n)

- range(5) = 0, 1, 2, 3, 4

### 2. range(a, b)

- range(1, 5) = 1, 2, 3, 4

### 3. range(a, b, step)

- range(0, 10, 2) = 0, 2, 4 ,6, 8
- range(10, 0, -2) = 10, 8, 6, 4, 2
- step으로 음수를 지정할 수 있다.