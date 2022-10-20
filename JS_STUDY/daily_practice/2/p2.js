/* 
1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
2. filter 메서드를 활용해 결혼한 사람들만 모아 married 상수에 할당하시오.
3. find 메서드를 활용해 이름이 Tom인 사람만 tom 상수에 할당하시오.
4. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
*/

const users = [
  { name: 'John', age: 31, isMarried: true, balance: 100, },
  { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
  { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
  { name: 'Robert', age: 27, isMarried: false, balance: 400, },
  { name: 'Tom', age: 35, isMarried: true, balance: 500, },
]

const one = users.forEach((element) => {
  console.log(element.name)
})

const married = users.filter((element) => {
  return element.isMarried === true
})
console.log(married)

const tom = users.find((element) => {
  return element.name === 'Tom'
})
console.log('------------4')
const newUsers = users.map((user) => {
  user.isAlive = true
  return user
})
console.log(newUsers)

const balance = users.map(a => a.balance);
const totalBalance = balance.reduce((a, b) => a + b)

const totalBalanc2  = users.reduce((total, user) => total + user.balance, 0)
console.log(totalBalance)
console.log(totalBalanc2)