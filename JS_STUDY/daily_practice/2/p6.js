for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 4-i; j++) {
    process.stdout.write(' ')
  }
  for (let j = 0; j <= i; j++) {
    process.stdout.write('*')
  }
  for (let j = 0; j < i; j++) {
    process.stdout.write('*')
  }
  console.log()
}




for (let i = 0; i < 5; i++) {
  let star = ''
  for (let j = 0; j < 4-i; j++) {
    star += ' '
  }
  for (let j = 0; j <= i; j++) {
    star += '*'
  }
  for (let j = 0; j < i; j++) {
    star += '*'
  }
  console.log(star)
}