// 1. input 태그 안의 값(value)을 잡는다.

// console.log(input);

// 2. button 에 'click'이 일어났을 때, input 에 ENTER키를 쳤을때, 이벤트 리스너를 단다.
// [무엇].addEventListener([언제], [어떻게])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
// const inputCount = document.querySelector('#js-image-count').value;
const resultArea = document.querySelector('#js-result-area');




button.addEventListener('click', () => {
    const inputValue = inputArea.value
    resultArea.innerHTML += inputValue
    searchAndPush(inputValue)

});


inputArea.addEventListener('keypress', (event) => {
    if (event.which === 13) {
        const inputValue = inputArea.value
        searchAndPush(inputValue)
    }
    // const inputValue = inputArea.value;
    // console.log(inputArea)  이 두줄을 활용해 한글자가 쳐질때 마다 반응하고 이걸로 자동완성에 활용
});


// 3. Giphy API에서 넘겨준 DATA를 index.html에서 보여준다.


const searchAndPush = (keyWord) => {
    
    const API_KEY = '8PzwNP1bviWfTGwwnF75wFCh5GTgbIz2'
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyWord}&limit=25&offset=0&rating=G&lang=ko`

    const AJAX = new XMLHttpRequest(); // 요청 준비
    AJAX.open('GET', url); // 요청 세팅
    AJAX.send(); //요청 보내기

    AJAX.addEventListener('load', (answer) => {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        const dataset = giphyData.data;

        resultArea.innerHTML = null;
        for (const data of dataset) {
            pushToDOM(data.images.fixed_height.url)
        }

    });

    const pushToDOM = (imageUrl) => {
        const imageTag = document.createElement('img');
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-image';
        imageTag.classList.add('container-image');
        
        resultArea.appendChild(imageTag);

        
    }
}




// const sendAjaxReq = () => {
//     const AJAX = new XMLHttpRequest(); // 요청 준비
//     AJAX.open('GET', url); // 요청 세팅
//     AJAX.send(); //요청 보내기

//     AJAX.addEventListener('load', (answer) => {
//         const res = answer.target.response;
//         const giphyData = JSON.parse(res)
//         console.log(giphyData);
//     });

// };