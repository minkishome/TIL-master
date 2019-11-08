const likeButtons = document.querySelectorAll('.js-like-button');
likeButtons.forEach((likeButton) => {
    likeButton.addEventListener('click', function (event) {
            const URL = `/insta/${event.target.dataset.id}/like/`;
            axios.defaults.xsrffCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            axios.get(URL)
                .then((res) => {
                        if (res.data.liked) {
                            event.target.classList.remove('far');
                            event.target.classList.add('fas')
                        
                        }
                        else {
                            event.target.classList.remove('fas');
                            event.target.classList.add('far')
                        }
                    
                })
    })
})