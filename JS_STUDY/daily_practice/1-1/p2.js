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

const array = 'level'.split('')
// console.log(array)
const palin = array.every((word, index, arr) => {
  return array[index] === array[array.length-index-1]
})
console.log(palin)
// 출력
// palindrome('level') => true
// palindrome('hi') => false