for (let i = 0; i < 5; i++) {
  for (let j = 0; j <= i; j++){
    process.stdout.write('*');
  }
  console.log('')
}

let star = ''
for (let i = 0; i < 5; i++) {
  star += '*'
  console.log(star)
}