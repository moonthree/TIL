const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']


const playGame = (p1_choice, p2_choice) => {
  if (p1_choice === p2_choice) {
    console.log(0)
  } else if (p1_choice === 'rock') {
    if (p2_choice === 'scissors') {
      console.log(1)
    } else {
      console.log(2)
    }
  } else if (p1_choice === 'scissors') {
    if (p2_choice === 'rock') {
      console.log(2)
    } else {
      console.log(1)
    }
  } else if (p1_choice === 'paper') {
    if (p2_choice === 'rock') {
      console.log(1)
    } else {
      console.log(2)
    }
  }
}

for (let i = 0; i < 10 ; i++) {
  playGame(p1[i], p2[i])
}

// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2
