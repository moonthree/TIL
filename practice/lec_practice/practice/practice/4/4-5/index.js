// 코드를 작성해 주세요
const scissorsBtn = document.querySelector('#scissors-button')
const rockBtn = document.querySelector('#rock-button')
const paperBtn = document.querySelector('#paper-button')

const player1Img = document.querySelector('#player1-img')
const player2Img = document.querySelector('#player2-img')

const p1Score = document.querySelector('.countA') 
const p2Score = document.querySelector('.countB')

const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')

let player1 = 0
let player2 = 0
let winner = 0

const imgArray = ['./img/scissors.png', './img/rock.png', './img/paper.png']
let nowImg = 0

// 컴퓨터 이미지 돌리기
const chageImg = function changeImage() {
  if (nowImg < imgArray.length) {
    // console.log(nowImg)
    player2Img.setAttribute('src', `${imgArray[nowImg]}`)
    nowImg += 1
  } else {
    nowImg = 0
  }
}

// 컴퓨터 랜덤 선택
const player2Choice = () => {
  let choice = parseInt(Math.random() * 3)
  console.log('choice : ', choice)
  player2 = choice
  player2Img.setAttribute('src', `${imgArray[choice]}`)
}
modal.addEventListener('click', function() {
  if (modal.style.display === 'block') {
    modal.style.display = 'none'
  }
})

//가위바위보
const rsf = () => {
  if (player1 === player2) {
    p2Score.innerText = p2Score.innerText
    winner = 0
  } else if (player1 === 0 && player2 === 1) { // 찌 묵
    p2Score.innerText = parseInt(p2Score.innerText) + 1
    winner = 2
  } else if (player1 === 0 && player2 === 2) { // 찌 빠
    p1Score.innerText = parseInt(p1Score.innerText) + 1
    winner = 1
  } else if (player1 === 1 && player2 === 0) { // 묵 찌
    p1Score.innerText = parseInt(p1Score.innerText) + 1
    winner = 1
  } else if (player1 === 1 && player2 === 2) { // 묵 빠
    p2Score.innerText = parseInt(p2Score.innerText) + 1
    winner = 2
  } else if (player1 === 2 && player2 === 0) { // 빠 찌
    p2Score.innerText = parseInt(p2Score.innerText) + 1
    winner = 2
  } else if (player1 === 2 && player2 === 0) { // 빠 묵
    p1Score.innerText = parseInt(p1Score.innerText) + 1
    winner = 1
  }
}

// 모달 열기
const modalOpen = () => {
  modal.style.display = 'block'
  if (winner === 0) {
    modalContent.innerText = '비김'
  } else if (winner === 1) {
    modalContent.innerText = '플레이어1이 이겼습니다.'
  } else if (winner === 2) {
    modalContent.innerText = '플레이어2가 이겼습니다.'
  }
}

// 버튼 비활성화
const btnDisabled = () => {
  scissorsBtn.disabled = true
  rockBtn.disabled = true
  paperBtn.disabled = true
}

// 버튼 활성화
const btnActivated = () => {
  scissorsBtn.disabled = false
  rockBtn.disabled = false
  paperBtn.disabled = false
}

scissorsBtn.addEventListener('click', function() {
  // 플레이어 선택, 이미지 바꾸기
  player1 = 0
  player1Img.setAttribute('src', './img/scissors.png')

  // 버튼 비활성화
  btnDisabled()

  // 컴퓨터 이미지 바꾸기, 종료
  const chage = setInterval(chageImg, 100)
  setTimeout(() => clearInterval(chage), 1000)

  // 플레이어2 선택
  setTimeout(() => player2Choice(), 1000)

  // 가위바위보
  setTimeout(() => rsf(), 1000)

  // 모달창 오픈
  setTimeout(() => modalOpen(), 1000) 

  // 버튼 활성화
  setTimeout(() => btnActivated(), 2000)
  
})

rockBtn.addEventListener('click', function() {
  player1 = 1
  player1Img.setAttribute('src', './img/rock.png')

  // 버튼 비활성화
  btnDisabled()

  // 컴퓨터 이미지 바꾸기, 종료
  const chage = setInterval(chageImg, 100)
  setTimeout(() => clearInterval(chage), 1000)

  // 플레이어2 선택
  setTimeout(() => player2Choice(), 1000)

  // 가위바위보
  setTimeout(() => rsf(), 1000)

  // 모달창 오픈
  setTimeout(() => modalOpen(), 1000) 

  // 버튼 활성화
  setTimeout(() => btnActivated(), 2000)
})

paperBtn.addEventListener('click', function() {
  player1 = 2
  player1Img.setAttribute('src', './img/paper.png')

  // 버튼 비활성화
  btnDisabled()

  // 컴퓨터 이미지 바꾸기, 종료
  const chage = setInterval(chageImg, 100)
  setTimeout(() => clearInterval(chage), 1000)

  // 플레이어2 선택
  setTimeout(() => player2Choice(), 1000)

  // 가위바위보
  setTimeout(() => rsf(), 1000)

  // 모달창 오픈
  setTimeout(() => modalOpen(), 1000) 

  // 버튼 활성화
  setTimeout(() => btnActivated(), 2000)
})