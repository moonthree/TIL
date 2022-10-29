function solution(s)
{
    let wordArr = s.split('')
    while (1) {
        let flag = 0
        let newWordArr = ''
        for (let i = 1; i < wordArr.length; i++) {
            if (wordArr[0] !== wordArr[1]) {
                newWordArr += wordArr[0]
            }
            if (flag === 0) {
                if (wordArr[i] === wordArr[i+1]) {
                    flag += 1
                    i += 2
                } else {
                    newWordArr += wordArr[i]
                }   
            } else {
                newWordArr += wordArr[i]
                
            }
        }
        // console.log(newWordArr)
        wordArr = newWordArr.split('')
        // console.log(wordArr)
        if (flag === 0) {
            break
        }
    }
    
}

solution('baabaa')