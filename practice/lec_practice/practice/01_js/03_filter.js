const products = [
  { name: 'cucumber', type: 'vegetable' },
  { name: 'banana', type: 'fruit' },
  { name: 'carrot', type: 'vegetable' },
  { name: 'apple', type: 'fruit' },
]

const fruitFilter = function (product) {
  return product.type === 'fruit'
}

const newAarry = products.filter(fruitFilter)

console.log(newArry)


// 2.

const newAarr2y = products.filter(function (product) {
  return product.type === 'fruit'
})

// 3. 
const newArry = products.filter((product) => {
  return product.type === 'fruit'
})
