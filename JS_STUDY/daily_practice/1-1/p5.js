const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

// console.log(participantNums[0].filter(num => 3 === num).length)

for (let i = 0 ; i < participantNums.length ; i++) {
  for (let j = 0 ; j < participantNums[i].length ; j++) {
    if (participantNums[i].filter(num => participantNums[i][j] === num).length === 1) {
      console.log(participantNums[i][j])
      break
    }
  }
}
console.log('-----------')
console.log('-----------')
console.log('-----------')
const answer = participantNums.forEach((tc) => {
  let arr = new Array(101).fill(0)
  tc.forEach((num) => {
    arr[num] += 1
  })
  arr.find((num, index) => {
    if (num === 1){
      console.log(index)
    }
  })
})

// console.log(answer)