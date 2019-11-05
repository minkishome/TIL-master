//1. 선언형
function a (x, y) {
    return x + y
}


//2. 할당형
const b = function (x,y) {
    return x + y
};

//3. arrow function (할당형)

const c = (x,y) => {
    return x + y
};
//3-1 짧게: 함수 블록에 코드가 return 문 한 줄이라면!
const d = (x, y) => x + y; //lambda형태랑 비슷
//3-2 짧게 : 함수의 인자가 단 하나일때
const e = x => {
    return x ** 2
}
const f = () => { //없으면 _로 쓰기도 함
    return false
}
const g =  _ => {
    return false
}

const square = function (x) {
    return x ** 2
}

const square2 = x => x ** 2