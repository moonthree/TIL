function slowRequest(callBack) {
  console.log('1. 오래 걸리는 작업 시작 ...')
  setTimeout(function () {  
    callBack()
  }, 3000)
}

function myCallBack() {
  console.log('2. 콜백함수 실행됨')
}

slowRequest(myCallBack)
console.log('3. 다른 작업 실행')

// 출력결과
// 1. 오래걸리는 작업 시작
// 3. 다른 작업 실행
// 2. 콜백함수 실행됨