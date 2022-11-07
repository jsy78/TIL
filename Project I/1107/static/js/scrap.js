const bookmarkBtn = document.querySelector('#bookmark-btn')

bookmarkBtn.addEventListener('click', function (event) {
    const articleId = event.currentTarget.dataset.articleId
    axios({
        method: "GET",
        url: `/articles/${articleId}/bookmark/`
    })
        .then(response => {
            if (response.data.is_saved) {
                const bookmarkIcon = document.querySelector('#bookmark-icon')
                const bookmarkCount = document.querySelector('#bookmark-count')
                bookmarkIcon.classList.add('bi-bookmark-fill')
                bookmarkIcon.classList.remove('bi-bookmark')
                bookmarkCount.innerText = response.data.save_count
            }
            else {
                const bookmarkIcon = document.querySelector('#bookmark-icon')
                const bookmarkCount = document.querySelector('#bookmark-count')
                bookmarkIcon.classList.add('bi-bookmark')
                bookmarkIcon.classList.remove('bi-bookmark-fill')
                bookmarkCount.innerText = response.data.save_count
            }
        })
        .catch(error => {
            console.log(error)
        })
})