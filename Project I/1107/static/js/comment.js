const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

function replyForm() {
  const replyBtns = document.querySelectorAll('.reply-btn')
  replyBtns.forEach((replyBtn) => {
    replyBtn.addEventListener('click', function (event) {
      console.log(event.target.dataset)
      const commentId = event.currentTarget.dataset.commentId
      document.querySelector(`#reply-create-${commentId}`).classList.toggle('d-none')
      document.querySelector(`#reply-create-${commentId}`).classList.toggle('d-block')
    })
  })
}

function commentDelete() {
  const commentDeleteForms = document.querySelectorAll('.comment-delete-form')
  commentDeleteForms.forEach((commentDeleteForm) => {
    commentDeleteForm.addEventListener('submit', function (event) {
      event.preventDefault()
      const articleId = event.currentTarget.dataset.articleId
      const commentId = event.currentTarget.dataset.commentId
      axios({
        method: 'POST',
        url: `/articles/${articleId}/comments/${commentId}/delete/`,
        headers: { 'X-CSRFToken': csrftoken }
      })
      .then(response => {
        console.log(response)
        const comments = response.data.comments
        const commentsArea = document.querySelector('#comments-area')

        while (commentsArea.hasChildNodes()) {
          commentsArea.removeChild(commentsArea.firstChild)
        }

        commentsArea.insertAdjacentHTML('beforeend',
          `
          <h5>${response.data.comments_count}개의 댓글</h5>
          <hr class="mb-0">
          <ul id="comments-list" class="list-group list-group-flush rounded-2">
          </ul>
           `
        )
        for (let i = 0; i < comments.length; i++) {
          if (comments[i].parent == null) {
            document.querySelector('#comments-list').insertAdjacentHTML('beforeend', 
              `
              <li id="comment-${comments[i].pk}" class="list-group-item bg-light p-0">
                <div id="comment-${comments[i].pk}-user" class="d-flex justify-content-between align-items-center">
                </div>
              </li>
              `
            )
            if (response.data.request_username == comments[i].username) {
              document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
                `
                <a class="card-text m-2 comment-user" href="/accounts/mypage/">${comments[i].username}</a>
                <p class="card-text text-muted">${comments[i].created_at}</p>
                `
              )
            }
            else {
              document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
                `
                <a class="card-text m-2 comment-user" href="/accounts/profile/${comments[i].username}/">${comments[i].username}</a>
                <p class="card-text text-muted">${comments[i].created_at}</p>
                `
              )
            }
            document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
              `
              <div class="d-flex justify-content-between m-2">
                <p>${comments[i].content}</p>
                <div id="btn-${comments[i].pk}" class="d-flex align-items-baseline">
                </div>
              </div>
              `
            )
            if (response.data.request_username == comments[i].username) {
              document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend',
                `
                <form class="comment-delete-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                  <button class="btn btn-sm p-0 border-0 text-danger text-decoration-none me-2" type="submit"><i class="bi bi-x-square"></i></button>
                </form>
                `
              )
            }
            if (response.data.request_is_authenticated) {
              document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
                `
                <button class="btn btn-sm p-0 border-0 text-secondary text-decoration-none me-2 reply-btn" data-comment-id="${comments[i].pk}" type="button"><i class="bi bi-arrow-down-right"></i></button>
                `
              )
              document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend',
                `
                <div id="reply-create-${comments[i].pk}" class="d-none">
                  <form class="reply-create-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                    <div class="d-flex justify-content-between">
                      <div class="flex-fill me-2">
                        <div class="mb-3">
                          <input type="text" name="content" placeholder="대댓글을 남겨보세요 💬" class="form-control" required="" id="id_content">
                        </div>
                      </div>
                      <div>
                        <input class="btn btn-search" type="submit" value="작성">
                      </div>
                    </div>
                  </form>
                </div>
                `
              )
            }
          }
          else {
            document.querySelector(`#comment-${comments[i].parent}`).insertAdjacentHTML('beforeend', 
              `
              <ul id="reply-list-${comments[i].parent}" class="list-group list-group-flush rounded-2">
                <div id="reply-${comments[i].pk}" class="d-flex">
                  <a href="#comment-${comments[i].parent}" class="m-2"><i class="bi bi-arrow-return-right"></i></a>
                </div>
              </ul>
              `
            )
            document.querySelector(`#reply-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
              `
              <li id="comment-${comments[i].pk}" class="list-group-item bg-light p-0 border-0 flex-fill">
                <div id="comment-${comments[i].pk}-user" class="d-flex justify-content-between align-items-center">
                </div>
              </li>
              `
            )
            if (response.data.request_username == comments[i].username) {
              document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
                `
                <a class="card-text m-2 comment-user" href="/accounts/mypage/">${comments[i].username}</a>
                <p class="card-text text-muted">${comments[i].created_at}</p>
                `
              )
            }
            else {
              document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
                `
                <a class="card-text m-2 comment-user" href="/accounts/profile/${comments[i].username}/">${comments[i].username}</a>
                <p class="card-text text-muted">${comments[i].created_at}</p>
                `
              )
            }
            document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
              `
              <div class="d-flex justify-content-between m-2">
                <p>${comments[i].content}</p>
                <div id="btn-${comments[i].pk}" class="d-flex align-items-baseline">
                </div>
              </div>
              `
            )
            if (response.data.request_username == comments[i].username) {
              document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend',
                `
                <form class="comment-delete-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                  <button class="btn btn-sm p-0 border-0 text-danger text-decoration-none me-2" type="submit"><i class="bi bi-x-square"></i></button>
                </form>
                `
              )
            }
            if (response.data.request_is_authenticated) {
              document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
                `
                <button class="btn btn-sm p-0 border-0 text-secondary text-decoration-none me-2 reply-btn" data-comment-id="${comments[i].pk}" type="button"><i class="bi bi-arrow-down-right"></i></button>
                `
              )
              document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend',
                `
                <div id="reply-create-${comments[i].pk}" class="d-none">
                  <form class="reply-create-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                    <div class="d-flex justify-content-between">
                      <div class="flex-fill me-2">
                        <div class="mb-3">
                          <input type="text" name="content" placeholder="대댓글을 남겨보세요 💬" class="form-control" required="" id="id_content">
                        </div>
                      </div>
                      <div>
                        <input class="btn btn-search" type="submit" value="작성">
                      </div>
                    </div>
                  </form>
                </div>
                `
              )
            }
          }
        }  
      })
      .then(response => {
        replyForm()
        commentDelete()
        replyCreate()
      })
      .catch(error => {
        console.log(error.response)
      })
    })
  })
}

function replyCreate() {
  const replyCreateForms = document.querySelectorAll('.reply-create-form')
  replyCreateForms.forEach((replyCreateForm) => {
    replyCreateForm.addEventListener('submit', function (event) {
      event.preventDefault()
      const articleId = event.currentTarget.dataset.articleId
      const commentId = event.currentTarget.dataset.commentId
      axios({
        method: 'POST',
        url: `/articles/${articleId}/comments/${commentId}/reply/`,
        headers: { 'X-CSRFToken': csrftoken },
        data: new FormData(replyCreateForm) // 폼에 있는 정보를 data로 넘겨줄 수 있도록 변환
      })
      .then(response => {
        console.log(response)
        const comments = response.data.comments
        const commentsArea = document.querySelector('#comments-area')

        while (commentsArea.hasChildNodes()) {
          commentsArea.removeChild(commentsArea.firstChild)
        }

        commentsArea.insertAdjacentHTML('beforeend',
          `
          <h5>${response.data.comments_count}개의 댓글</h5>
          <hr class="mb-0">
          <ul id="comments-list" class="list-group list-group-flush rounded-2">
          </ul>
           `
        )
        for (let i = 0; i < comments.length; i++) {
          if (comments[i].parent == null) {
            document.querySelector('#comments-list').insertAdjacentHTML('beforeend', 
              `
              <li id="comment-${comments[i].pk}" class="list-group-item bg-light p-0">
                <div id="comment-${comments[i].pk}-user" class="d-flex justify-content-between align-items-center">
                </div>
              </li>
              `
            )
            if (response.data.request_username == comments[i].username) {
              document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
                `
                <a class="card-text m-2 comment-user" href="/accounts/mypage/">${comments[i].username}</a>
                <p class="card-text text-muted">${comments[i].created_at}</p>
                `
              )
            }
            else {
              document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
                `
                <a class="card-text m-2 comment-user" href="/accounts/profile/${comments[i].username}/">${comments[i].username}</a>
                <p class="card-text text-muted">${comments[i].created_at}</p>
                `
              )
            }
            document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
              `
              <div class="d-flex justify-content-between m-2">
                <p>${comments[i].content}</p>
                <div id="btn-${comments[i].pk}" class="d-flex align-items-baseline">
                </div>
              </div>
              `
            )
            if (response.data.request_username == comments[i].username) {
              document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend',
                `
                <form class="comment-delete-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                  <button class="btn btn-sm p-0 border-0 text-danger text-decoration-none me-2" type="submit"><i class="bi bi-x-square"></i></button>
                </form>
                `
              )
            }
            if (response.data.request_is_authenticated) {
              document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
                `
                <button class="btn btn-sm p-0 border-0 text-secondary text-decoration-none me-2 reply-btn" data-comment-id="${comments[i].pk}" type="button"><i class="bi bi-arrow-down-right"></i></button>
                `
              )
              document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend',
                `
                <div id="reply-create-${comments[i].pk}" class="d-none">
                  <form class="reply-create-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                    <div class="d-flex justify-content-between">
                      <div class="flex-fill me-2">
                        <div class="mb-3">
                          <input type="text" name="content" placeholder="대댓글을 남겨보세요 💬" class="form-control" required="" id="id_content">
                        </div>
                      </div>
                      <div>
                        <input class="btn btn-search" type="submit" value="작성">
                      </div>
                    </div>
                  </form>
                </div>
                `
              )
            }
          }
          else {
            document.querySelector(`#comment-${comments[i].parent}`).insertAdjacentHTML('beforeend', 
              `
              <ul id="reply-list-${comments[i].parent}" class="list-group list-group-flush rounded-2">
                <div id="reply-${comments[i].pk}" class="d-flex">
                  <a href="#comment-${comments[i].parent}" class="m-2"><i class="bi bi-arrow-return-right"></i></a>
                </div>
              </ul>
              `
            )
            document.querySelector(`#reply-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
              `
              <li id="comment-${comments[i].pk}" class="list-group-item bg-light p-0 border-0 flex-fill">
                <div id="comment-${comments[i].pk}-user" class="d-flex justify-content-between align-items-center">
                </div>
              </li>
              `
            )
            if (response.data.request_username == comments[i].username) {
              document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
                `
                <a class="card-text m-2 comment-user" href="/accounts/mypage/">${comments[i].username}</a>
                <p class="card-text text-muted">${comments[i].created_at}</p>
                `
              )
            }
            else {
              document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
                `
                <a class="card-text m-2 comment-user" href="/accounts/profile/${comments[i].username}/">${comments[i].username}</a>
                <p class="card-text text-muted">${comments[i].created_at}</p>
                `
              )
            }
            document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
              `
              <div class="d-flex justify-content-between m-2">
                <p>${comments[i].content}</p>
                <div id="btn-${comments[i].pk}" class="d-flex align-items-baseline">
                </div>
              </div>
              `
            )
            if (response.data.request_username == comments[i].username) {
              document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend',
                `
                <form class="comment-delete-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                  <button class="btn btn-sm p-0 border-0 text-danger text-decoration-none me-2" type="submit"><i class="bi bi-x-square"></i></button>
                </form>
                `
              )
            }
            if (response.data.request_is_authenticated) {
              document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
                `
                <button class="btn btn-sm p-0 border-0 text-secondary text-decoration-none me-2 reply-btn" data-comment-id="${comments[i].pk}" type="button"><i class="bi bi-arrow-down-right"></i></button>
                `
              )
              document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend',
                `
                <div id="reply-create-${comments[i].pk}" class="d-none">
                  <form class="reply-create-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                    <div class="d-flex justify-content-between">
                      <div class="flex-fill me-2">
                        <div class="mb-3">
                          <input type="text" name="content" placeholder="대댓글을 남겨보세요 💬" class="form-control" required="" id="id_content">
                        </div>
                      </div>
                      <div>
                        <input class="btn btn-search" type="submit" value="작성">
                      </div>
                    </div>
                  </form>
                </div>
                `
              )
            }
          }
        }
        replyCreateForm.reset()  
      })
      .then(response => {
        replyForm()
        commentDelete()
        replyCreate()
      })
      .catch(error => {
        console.log(error.response)
      })
    })
  })
}

function commentCreate() {
  const commentCreateForm = document.querySelector('#comment-create-form')
  commentCreateForm.addEventListener('submit', function (event) {
    event.preventDefault()
    const articleId = event.currentTarget.dataset.articleId
    axios({
      method: 'POST',
      url: `/articles/${articleId}/comments/`,
      headers: { 'X-CSRFToken': csrftoken },
      data: new FormData(commentCreateForm) // 폼에 있는 정보를 data로 넘겨줄 수 있도록 변환
    })
    .then(response => {
      console.log(response)
      const comments = response.data.comments
      const commentsArea = document.querySelector('#comments-area')

      while (commentsArea.hasChildNodes()) {
        commentsArea.removeChild(commentsArea.firstChild)
      }

      commentsArea.insertAdjacentHTML('beforeend',
        `
        <h5>${response.data.comments_count}개의 댓글</h5>
        <hr class="mb-0">
        <ul id="comments-list" class="list-group list-group-flush rounded-2">
        </ul>
         `
      )
      for (let i = 0; i < comments.length; i++) {
        if (comments[i].parent == null) {
          document.querySelector('#comments-list').insertAdjacentHTML('beforeend', 
            `
            <li id="comment-${comments[i].pk}" class="list-group-item bg-light p-0">
              <div id="comment-${comments[i].pk}-user" class="d-flex justify-content-between align-items-center">
              </div>
            </li>
            `
          )
          if (response.data.request_username == comments[i].username) {
            document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
              `
              <a class="card-text m-2 comment-user" href="/accounts/mypage/">${comments[i].username}</a>
              <p class="card-text text-muted">${comments[i].created_at}</p>
              `
            )
          }
          else {
            document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
              `
              <a class="card-text m-2 comment-user" href="/accounts/profile/${comments[i].username}/">${comments[i].username}</a>
              <p class="card-text text-muted">${comments[i].created_at}</p>
              `
            )
          }
          document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
            `
            <div class="d-flex justify-content-between m-2">
              <p>${comments[i].content}</p>
              <div id="btn-${comments[i].pk}" class="d-flex align-items-baseline">
              </div>
            </div>
            `
          )
          if (response.data.request_username == comments[i].username) {
            document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend',
              `
              <form class="comment-delete-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                <button class="btn btn-sm p-0 border-0 text-danger text-decoration-none me-2" type="submit"><i class="bi bi-x-square"></i></button>
              </form>
              `
            )
          }
          if (response.data.request_is_authenticated) {
            document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
              `
              <button class="btn btn-sm p-0 border-0 text-secondary text-decoration-none me-2 reply-btn" data-comment-id="${comments[i].pk}" type="button"><i class="bi bi-arrow-down-right"></i></button>
              `
            )
            document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend',
              `
              <div id="reply-create-${comments[i].pk}" class="d-none">
                <form class="reply-create-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                  <div class="d-flex justify-content-between">
                    <div class="flex-fill me-2">
                      <div class="mb-3">
                        <input type="text" name="content" placeholder="대댓글을 남겨보세요 💬" class="form-control" required="" id="id_content">
                      </div>
                    </div>
                    <div>
                      <input class="btn btn-search" type="submit" value="작성">
                    </div>
                  </div>
                </form>
              </div>
              `
            )
          }
        }
        else {
          document.querySelector(`#comment-${comments[i].parent}`).insertAdjacentHTML('beforeend', 
            `
            <ul id="reply-list-${comments[i].parent}" class="list-group list-group-flush rounded-2">
              <div id="reply-${comments[i].pk}" class="d-flex">
                <a href="#comment-${comments[i].parent}" class="m-2"><i class="bi bi-arrow-return-right"></i></a>
              </div>
            </ul>
            `
          )
          document.querySelector(`#reply-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
            `
            <li id="comment-${comments[i].pk}" class="list-group-item bg-light p-0 border-0 flex-fill">
              <div id="comment-${comments[i].pk}-user" class="d-flex justify-content-between align-items-center">
              </div>
            </li>
            `
          )
          if (response.data.request_username == comments[i].username) {
            document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
              `
              <a class="card-text m-2 comment-user" href="/accounts/mypage/">${comments[i].username}</a>
              <p class="card-text text-muted">${comments[i].created_at}</p>
              `
            )
          }
          else {
            document.querySelector(`#comment-${comments[i].pk}-user`).insertAdjacentHTML('beforeend', 
              `
              <a class="card-text m-2 comment-user" href="/accounts/profile/${comments[i].username}/">${comments[i].username}</a>
              <p class="card-text text-muted">${comments[i].created_at}</p>
              `
            )
          }
          document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
            `
            <div class="d-flex justify-content-between m-2">
              <p>${comments[i].content}</p>
              <div id="btn-${comments[i].pk}" class="d-flex align-items-baseline">
              </div>
            </div>
            `
          )
          if (response.data.request_username == comments[i].username) {
            document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend',
              `
              <form class="comment-delete-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                <button class="btn btn-sm p-0 border-0 text-danger text-decoration-none me-2" type="submit"><i class="bi bi-x-square"></i></button>
              </form>
              `
            )
          }
          if (response.data.request_is_authenticated) {
            document.querySelector(`#btn-${comments[i].pk}`).insertAdjacentHTML('beforeend', 
              `
              <button class="btn btn-sm p-0 border-0 text-secondary text-decoration-none me-2 reply-btn" data-comment-id="${comments[i].pk}" type="button"><i class="bi bi-arrow-down-right"></i></button>
              `
            )
            document.querySelector(`#comment-${comments[i].pk}`).insertAdjacentHTML('beforeend',
              `
              <div id="reply-create-${comments[i].pk}" class="d-none">
                <form class="reply-create-form" data-article-id="${response.data.article_pk}" data-comment-id="${comments[i].pk}">
                  <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                  <div class="d-flex justify-content-between">
                    <div class="flex-fill me-2">
                      <div class="mb-3">
                        <input type="text" name="content" placeholder="대댓글을 남겨보세요 💬" class="form-control" required="" id="id_content">
                      </div>
                    </div>
                    <div>
                      <input class="btn btn-search" type="submit" value="작성">
                    </div>
                  </div>
                </form>
              </div>
              `
            )
          }
        }
      }
      commentCreateForm.reset()  
    })
    .then(response => {
      replyForm()
      commentDelete()
      replyCreate()
    })
    .catch(error => {
      console.log(error.response)
    })
  })
}
replyForm()
commentDelete()
replyCreate()
commentCreate()