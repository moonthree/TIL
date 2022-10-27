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

  divCard.classList.add('search-result__card')
  divText.classList.add('search-result__text')
  img.setAttribute('src', imgUrl)
  h2.innerText = artist
  p.innerText = albumName

  divText.appendChild(h2)
  divText.appendChild(p)

  divCard.appendChild(img)
  divCard.appendChild(divText)

  const divResult = document.querySelector('.search-result')
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
      // console.log(response[0].image[0].size)
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

// 검색
const searchBtn = document.querySelector('.search-box__button')
const searchInput = document.querySelector('.search-box__input')

searchBtn.addEventListener('click', function() {
  let searchWord = searchInput.value
  fetchAlbums(searchWord, 1, 10)
})