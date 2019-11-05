// 14 arrayHelperMethods
// PPOINT!! => 함수의 인자로 함수가 들어간다
console.log('#1------')
// ES5
console.log('ES5---')
var colors = ['red', 'blue', 'green'];
for (var i=0; i < colors.length; i++) {
    console.log(colors[i]);
}
// ES6+
console.log('ES6+---')
function logger(x) {
    console.log(x)
}
// forEach 가 끝나고 아무것도 return 하지 않는다.
// return 이 없어
colors.forEach(logger)  // colors 에서 요소 하나하나를 꺼내와서 logger 에 넣어 주는 것이 forEach
colors.forEach(function (x) {
    console.log(x)
}) 
console.log('#2------')
// ES5
console.log('ES5---')
const numbers = [1, 2, 3];
const doubledNumbers = [];
for (let i=0; i < numbers.length; i++) {
    doubledNumbers.push(numbers[i*2]);
}
console.log(doubledNumbers);
// ES6+
// map: 각각의 요소를 처리한 값을 return 한다
numbers.map(function(number) {
    return number * 2;
})
const tripleNumbers = numbers.map((number) => {
    return number * 3;
})
console.log(tripleNumbers);
// filter
// ES5
const products = [
    {name: 'apple', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'tomato', type: 'fruit'},
    {name: 'cucumber', type: 'vegetable'},
]
const fruits = []
for (const product of products) {
    if (product.type === 'fruit') {  // if 문과 비교해서 if 충족 할 때만 push
        fruits.push(product);
    }
};
console.log(fruits)
// ES6+
// filter: 조건을 충족시키는 애들만 남긴다
const vegetables = products.filter((product) => {
    return product.type === 'vegetable';  // return 이 true 일 때만 push
})
console.log(vegetables)