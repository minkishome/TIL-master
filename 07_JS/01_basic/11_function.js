/* python
    def adder_1(x,y):
        return x+y
*/


function adder1(x, y){   // 선언식 ; 필요없음
    return x + y;
}

/* python에서는 안됨
    adder2 = (x,y): return x + y
 */

 const adder2 = function(x, y) { //할당식 ; 붙는다
     return x + y
 }

 /* Python Lambda 표현식
    adder3 = lambda x, y : x + y

 */

// ES6+
// 1. function 을 지운다.
// 2. ()와 {} 사이에 => 를 넣는다.
const adder3 = (x,y) =>{
    return x + y;
};


// This is Comment

function concat(str1, str2){
    return `${str1} - ${str2}`;
};

function CheckLongStr(string){
    if (string.length > 10) {
        return true
    }
    else {
        return false
    }
}

if (CheckLongStr(concat('Happy', 'Hacking'))){
    console.log('Long STring')
}
else{
    console.log('Short String')
}