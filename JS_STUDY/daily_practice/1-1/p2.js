const palindrome = function (str) {
  if (str.split('').reverse().join('') !== str){
    return false
  } else {
    return true
  }
}

const arr = ['level', 'hi']
for (let i = 0 ; i < arr.length ; i++){
  console.log(palindrome(arr[i]))
}
// 출력
// palindrome('level') => true
// palindrome('hi') => false