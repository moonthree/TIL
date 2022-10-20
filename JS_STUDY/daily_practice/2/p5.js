function findQueens(n) {
	// 이곳에 작성합니다.
  let row = new Array(n).fill(0)
  
  function is_promising(x) {
    for (let i = 0; i < x; i++) {
      if (row[x] === row[i] || Math.abs(row[x] = row[i]) === Math.abs(x - i)) {
        return false
      }
    }
    return true
  }

  function n_queens(x) {
    let answer = 0
    if (x === n) {
      answer += 1
      return answer
    } else {
      for (let i = 0; i < n; i++) {
        row[x] = i
        if (is_promising(x) == true) {
          n_queens(x+1)
        }
      }
    }
  }
  console.log(n_queens(0))
  return n_queens(0)
}

console.log(findQueens(4)) // 2
console.log(typeof findQueens(4))