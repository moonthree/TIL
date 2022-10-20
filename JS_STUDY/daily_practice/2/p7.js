const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  let now = K+1
  let move = 0
  let flag = 1
  while (now < N) {
    let battery = K
    while (1) {
      console.log(now)
      if (chargers.includes(now)) {
        move += 1
        break
      }
      if (battery === 0) {
        flag = 0
      }
      now -= 1
      battery -= 1
    }
    if (flag === 0) {
      break
    }
  }
  if (flag === 1) {
    console.log(move)
  } else {
    console.log(0)
  }

}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}