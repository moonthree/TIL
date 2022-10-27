/* 
  아래에 코드를 작성해주세요.
*/
const KEY = ''

// 앨범 박스 html 만들기
const makeAlbum = (imgUrl, artist, albumName) => {
  const divCard = document.createElement('div')
  const img = document.createElement('img')
  const divText = document.createElement('div')
  const h2 = document.createElement('h2')
  const p = document.createElement('p')
  const divResult = document.querySelector('.search-result')

  divCard.classList.add('search-result__card')
  divText.classList.add('search-result__text')
  img.setAttribute('src', imgUrl)
  h2.innerText = artist
  p.innerText = albumName

  divText.appendChild(h2)
  divText.appendChild(p)

  divCard.appendChild(img)
  divCard.appendChild(divText)

  divResult.appendChild(divCard)
}

// 앨범 박스 만들기
function fetchAlbums (searchWord, page, limit) {
  axios({
    method : 'GET',
    url : `http://ws.audioscrobbler.com/2.0/?method=album.search&album=${searchWord}&api_key=${KEY}&limit=${limit}&page=${page}&format=json`,
  })
    .then((response) => {
      const albums = response.data.results.albummatches.album
      return albums
    })
    .then((response) => {
      // console.log(response[0].image[0])
      // console.log(response[0].image[0]['#text'])
      response.forEach((element) => {
        const imgUrl = element.image[2]['#text']
        const artist = element.artist
        const albumName = element.name
        makeAlbum(imgUrl, artist, albumName)
      })
    })
    .catch((error) => {
      console.log(error)
    })
}

//무한스크롤

const bottom = document.querySelector('.search-result--loadingList')

const options = {
  root: document.querySelector('.search-result--loadingList'), // .container class를 가진 엘리먼트를 root로 설정. null일 경우 브라우저 viewport
  rootMargin: '10px', // rootMargin을 '10px 10px 10px 10px'로 설정
  threshold: [0, 0.5, 1] // 타겟 엘리먼트가 교차영역에 진입했을 때, 교차영역에 타켓 엘리먼트의 50%가 있을 때, 교차 영역에 타켓 엘리먼트의 100%가 있을 때 observe가 반응한다.
}

// IntersectionObserver 생성
const io = new IntersectionObserver((entries, observer) => {
  // IntersectionObserverEntry 객체 리스트와 observer 본인(self)를 받음
  // 동작을 원하는 것 작성
  entries.forEach(entry => {
    // entry와 observer 출력
    entry.target.
    console.log('entry:', entry);
    console.log('observer:', observer);
  })
}, options)

// if (detectBottom() === true) {
//   io.observe()
// }


// 검색
const searchBtn = document.querySelector('.search-box__button')
const searchInput = document.querySelector('.search-box__input')

searchBtn.addEventListener('click', function() {
  let searchWord = searchInput.value
  fetchAlbums(searchWord, 1, 10)
  io.observe(bottom)
})