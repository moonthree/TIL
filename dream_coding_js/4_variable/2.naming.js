// 주석을 달면 됨
/**
 * 여러줄 주석이 됨
 * 자음줄로 자동으로 넘아감
 */

/** 변수 규칙!
 * 라틴문자(0-9, a-z, A-Z), _
 * 대소문자를 구분함
 * 추천: camelCase (likeThis)
 * 한국어 X
 * 예약어 X
 * 숫자로 시작 X
 * 특수문자 X (_, $ 두가지는 예외)
 * 이모지 X
 * 여러개의 변수를 1, 2, 3 숫자로 구분 X -> 최대한 의미있게, 구체적으로 작성
 */



// 나쁜예제
let number = 20;
let audio1;
let audio2;

// 좋은예제
let myAge = 20;
let backgroundAudio;
let windAudio;

// 꿀팀
let audioBackground
let audioWind