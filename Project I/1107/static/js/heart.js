const likeBtn = document.querySelector('#like-btn')

likeBtn.addEventListener('click', function (event) {
    const articleId = event.currentTarget.dataset.articleId
    axios({
        method: "GET",
        url: `/articles/${articleId}/likes/`
    })
        .then(response => {
            if (response.data.is_liked) {
                const heartIcon = document.querySelector('#heart-icon')
                const likeCount = document.querySelector('#like-count')
                heartIcon.classList.add('bi-heart-fill')
                heartIcon.classList.remove('bi-heart')
                likeCount.innerText = response.data.like_count
            }
            else {
                const heartIcon = document.querySelector('#heart-icon')
                const likeCount = document.querySelector('#like-count')
                heartIcon.classList.add('bi-heart')
                heartIcon.classList.remove('bi-heart-fill')
                likeCount.innerText = response.data.like_count
            }
        })
        .catch(error => {
            console.log(error.response)
        })
})