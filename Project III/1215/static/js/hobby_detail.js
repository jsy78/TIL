const requestUserId = document.querySelector('#request-user-id').value
const pk = document.querySelector('#hobby_id').value
dayjs.extend(window.dayjs_plugin_relativeTime)
dayjs.extend(window.dayjs_plugin_utc)
dayjs.extend(window.dayjs_plugin_timezone)
dayjs.locale('ko')
const commentInput = document.querySelector('#commentinput')
const commentInputOff = document.querySelector('#commentinputoff')
const commentCount = document.querySelector('#comment-count')
// 댓글 리스트
const commentList = document.querySelector('#comment-list')
// 댓글 리스트 - 오프캔버스
const commentListOff = document.querySelector('#comment-list-off')
// 댓글 작성 폼
const mainCommentForm = document.querySelector('#comment-form')
const mainCommentFormOff = document.querySelector('#comment-form-off')
// 댓글 생성 함수
function submitComment(event) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    event.preventDefault();
    const commentForm = event.target
    if (event.target.dataset.action == 'comment-form') {
    axios({
        method: 'post',
        url: `/hobby/${pk}/comment_create`,
        headers: { 'X-CSRFToken': csrftoken},
        data: new FormData(commentForm)
    })
    .then(response => {
      // detail 페이지 댓글 제한 7개
        commentList.innerHTML = ""
        for (let i=0; i < response.data.comments_data.length; i++){
            let isLike = ""
            if (i == 7){
              break;
            }
            if (response.data.comments_data[i].is_like === true) {
              isLike = "heart"
            } else {
              isLike = "heart-outline"
            }
            commentList.insertAdjacentHTML('beforeend', `<hr>
              <div class="d-flex justify-content-between">
              <div class="comment-elem" >
                  <img class="comment-image" src="${ response.data.comments_data[i].image }" alt="">
                <div>
                  <p>${ response.data.comments_data[i].user }</p>
                  <p>${ response.data.comments_data[i].content }</p>
                  <div>
                    <p class="text-muted" style="font-size:12px"><span>${dayjs.utc(response.data.comments_data[i].created_at).local().fromNow()}</span> <span>좋아요 <span id="comment-${response.data.comments_data[i].pk}-likecnt">${response.data.comments_data[i].likeCount}</span>개</span> 
                    <span data-action="reComment" data-comment-id="${response.data.comments_data[i].pk}" style="cursor:pointer;">답글달기</span>
                    <ion-icon data-action='getDelete' type="button" data-bs-toggle="modal" data-bs-target="#comment-delete" data-comment-id="${response.data.comments_data[i].pk}" data-user="${ response.data.comments_data[i].user_pk }" name="ellipsis-horizontal"></ion-icon>
                    </p>
                  </div>
                </div>
              </div>
              <div>
              <ion-icon data-action="like" id="comment-${response.data.comments_data[i].pk}-likebtn" class="comment-like-btn" data-comment-id="${response.data.comments_data[i].pk}" style="color:#E84545" name=${isLike}></ion-icon>
              </div>
              </div>
              <div id="recomment-form-${response.data.comments_data[i].pk}" class="recomment-elem">
              <img class="comment-image" src="${ response.data.comments_data[i].image }" alt="">
              <form id="comment-form" data-hobby-id="${pk}" action=""
                method="POST" class="w-100" data-action="comment-form">
                <input id="commentinput" name="content" class="comment-control" type="text" placeholder="답글 달기...">
                <input class="d-none" type="submit" value="제출">
                <input type="hidden" name="parent" value="${response.data.comments_data[i].pk}">
              </form>
            </div>`)
            for (let j=0; j < response.data.comments_data[i].recomments.length ; j++){
              let isLike = ""
              if (response.data.comments_data[i].recomments[j].is_like === true) {
                isLike = "heart"
              } else {
                isLike = "heart-outline"
              }
              commentList.insertAdjacentHTML('beforeend', `<hr>
              <div class="d-flex justify-content-between ms-5">
              <div class="comment-elem" >
                  <img class="comment-image" src="${ response.data.comments_data[i].recomments[j].image }" alt="">
                <div>
                  <p>${ response.data.comments_data[i].recomments[j].user }</p>
                  <p>${ response.data.comments_data[i].recomments[j].content }</p>
                  <div>
                    <p class="text-muted" style="font-size:12px"><span>${dayjs.utc(response.data.comments_data[i].recomments[j].created_at).local().fromNow()}</span> <span>좋아요 <span id="comment-${response.data.comments_data[i].recomments[j].pk}-likecnt">${response.data.comments_data[i].recomments[j].likeCount}</span>개</span> 
                    <ion-icon data-action='getDelete' type="button" data-bs-toggle="modal" data-bs-target="#comment-delete" data-comment-id="${response.data.comments_data[i].recomments[j].pk}" data-user="${ response.data.comments_data[i].recomments[j].user_pk }" name="ellipsis-horizontal"></ion-icon>
                    </p>
                  </div>
                </div>
              </div>
              <div>
              <ion-icon data-action="like" id="comment-${response.data.comments_data[i].recomments[j].pk}-likebtn" class="comment-like-btn" data-comment-id="${response.data.comments_data[i].recomments[j].pk}" style="color:#E84545" name=${isLike}></ion-icon>
              </div>
              </div>`
              )};
            };
        commentInput.value = ""
        commentInputOff.value = ""
        commentCount.innerText = response.data.comments_len

        
        // 오프캔버스 더보기로 모든 댓글 구현
        commentListOff.textContent = ""
        for (let i=0; i < response.data.comments_data.length; i++){
          let isLike = ""
          if (response.data.comments_data[i].is_like === true) {
            isLike = "heart"
          } else {
            isLike = "heart-outline"
          }
          commentListOff.insertAdjacentHTML('beforeend', `<hr>
            <div class="d-flex justify-content-between">
            <div class="comment-elem" >
                <img class="comment-image" src="${ response.data.comments_data[i].image }" alt="">
              <div>
                <p>${ response.data.comments_data[i].user }</p>
                <p>${ response.data.comments_data[i].content }</p>
                <div>
                  <p class="text-muted" style="font-size:12px"><span>${dayjs.utc(response.data.comments_data[i].created_at).local().fromNow()}</span> <span>좋아요 <span id="comment-${response.data.comments_data[i].pk}-likecnt-off">${response.data.comments_data[i].likeCount}</span>개</span> 
                  <span data-action="reComment" data-comment-id="${response.data.comments_data[i].pk}" style="cursor:pointer;">답글달기</span>
                  <ion-icon data-action='getDelete' type="button" data-bs-toggle="modal" data-bs-target="#comment-delete" data-comment-id="${response.data.comments_data[i].pk}" data-user="${ response.data.comments_data[i].user_pk }" name="ellipsis-horizontal"></ion-icon>
                  </p>
                </div>
              </div>
            </div>
            <div>
            <ion-icon data-action="like" id="comment-${response.data.comments_data[i].pk}-likebtn-off" class="comment-like-btn" data-comment-id="${response.data.comments_data[i].pk}" style="color:#E84545" name=${isLike}></ion-icon>
            </div>
            </div>
            <div id="recomment-form-${response.data.comments_data[i].pk}-off" class="recomment-elem">
            <img class="comment-image" src="${ response.data.comments_data[i].image }" alt="">
            <form id="comment-form" data-hobby-id="${pk}" action=""
              method="POST" class="w-100" data-action="comment-form">
              <input id="commentinput" name="content" class="comment-control" type="text" placeholder="답글 달기...">
              <input class="d-none" type="submit" value="제출">
              <input type="hidden" name="parent" value="${response.data.comments_data[i].pk}">
            </form>
          </div>`)
          for (let j=0; j < response.data.comments_data[i].recomments.length ; j++){
            let isLike = ""
            if (response.data.comments_data[i].recomments[j].is_like === true) {
              isLike = "heart"
            } else {
              isLike = "heart-outline"
            }
            commentListOff.insertAdjacentHTML('beforeend', `<hr>
            <div class="d-flex justify-content-between ms-5">
            <div class="comment-elem" >
                <img class="comment-image" src="${ response.data.comments_data[i].recomments[j].image }" alt="">
              <div>
                <p>${ response.data.comments_data[i].recomments[j].user }</p>
                <p>${ response.data.comments_data[i].recomments[j].content }</p>
                <div>
                  <p class="text-muted" style="font-size:12px"><span>${dayjs.utc(response.data.comments_data[i].recomments[j].created_at).local().fromNow()}</span> <span>좋아요 <span id="comment-${response.data.comments_data[i].recomments[j].pk}-likecnt-off">${response.data.comments_data[i].recomments[j].likeCount}</span>개</span> 
                  <ion-icon data-action='getDelete' type="button" data-bs-toggle="modal" data-bs-target="#comment-delete" data-comment-id="${response.data.comments_data[i].recomments[j].pk}" data-user="${ response.data.comments_data[i].recomments[j].user_pk }" name="ellipsis-horizontal"></ion-icon>
                  </p>
                </div>
              </div>
            </div>
            <div>
            <ion-icon data-action="like" id="comment-${response.data.comments_data[i].recomments[j].pk}-likebtn-off" class="comment-like-btn" data-comment-id="${response.data.comments_data[i].recomments[j].pk}" style="color:#E84545" name=${isLike}></ion-icon>
            </div>
            </div>`
            )};
          };

    })

}};



const likeBtn = document.querySelector('.hobby-like-btn');
const likeList = document.querySelector('#like-list-off');
const likeBox = document.querySelector('#no-like-box');
function likeHobby(e) {
  const hobbyPk = e.dataset.hobbyId
  axios({
    method: 'get',
    url: `/hobby/${hobbyPk}/like_hobby`,
  })
  .then(response => {
    const likeCount = document.querySelector('#like-count')
    likeCount.innerText = response.data.likeCount
    if (response.data.is_like === true ) {
      if (response.data.likeCount === 1){
        likeList.textContent = ""
      }
      likeBtn.setAttribute('name', 'heart')
      likeList.insertAdjacentHTML('afterbegin', `<a id="like-user-${response.data.user_pk}" href="/accounts/detail/${response.data.user_pk}">
      <li class="d-flex justify-content-between">
        <div class="d-flex">
          <img class="member-image" src="${response.data.image}" alt="">
          <p class="m-3">
            <span style="font-size:20px; font-weight:600;">${response.data.nickname}</span><br>
            <span class="text-muted" style="overflow:hidden">멤버 소개글</span>
          </p>
        </div>
      </li>
    </a>`)
    } else {
      likeBtn.setAttribute('name', 'heart-outline')
      const likeUserElem = document.querySelector(`#like-user-${response.data.user_pk}`)
      likeUserElem.remove()
      if (response.data.likeCount === 0) {
        likeList.insertAdjacentHTML('afterbegin', `<div id="no-like-box" class="text-center mt-5">
        <p>
          <ion-icon name="people" size="large"></ion-icon>
        </p>
        <h5>아직 좋아요가 없습니다.</h5>
        <p class="text-muted">소셜링을 홍보해 보세요!</p>
      </div>`)
      }
    }

  })
};

function likeComment(e) {
  const commentPk = e.target.dataset.commentId;
  const likeBtnComment = document.querySelector(`#comment-${commentPk}-likebtn`);
  const likeBtnCommentOff = document.querySelector(`#comment-${commentPk}-likebtn-off`);
  if (e.target.dataset.action == 'like'){
    axios({
      method: 'get',
      url: `/hobby/${commentPk}/like_comment`,
    })
    .then(response => {
      if (response.data.is_like === true ) {
        try { likeBtnComment.setAttribute('name', 'heart') } catch(error) {};
        likeBtnCommentOff.setAttribute('name', 'heart')
      } else {
        try { likeBtnComment.setAttribute('name', 'heart-outline') } catch(error) {};
        likeBtnCommentOff.setAttribute('name', 'heart-outline')
      };
      try {
        const likeCntComment = document.querySelector(`#comment-${commentPk}-likecnt`)
        likeCntComment.innerText = response.data.likeCount
      } catch(error) {};
      const likeCntCommentOff = document.querySelector(`#comment-${commentPk}-likecnt-off`)
      likeCntCommentOff.innerText = response.data.likeCount
    })
  
  };
  };


function getDeleteComment(e) {
  if (e.target.dataset.action == 'getDelete') {
    const btnDiv = document.querySelector('.modal-body')
    if (requestUserId == e.target.dataset.user) {
      btnDiv.innerHTML = `<button onclick="deleteComment(this)" data-bs-dismiss="modal" data-comment-id="${e.target.dataset.commentId}" id="comment-delete-btn" class="mt-3 submit_btn slide_button" type="button">댓글 삭제하기</button>`
    } else {
      btnDiv.innerHTML = `<button onclick="commentReport()" id="comment-report-btn" data-bs-dismiss="modal" class="mt-3 submit_btn slide_button" type="button">댓글 신고하기</button>`
    }};
};

function getReComment(e) {
  const recommentForm = document.querySelector(`#recomment-form-${e.target.dataset.commentId}`)
  if (e.target.dataset.action == 'reComment') {
    recommentForm.classList.toggle('recomment-elem')
    recommentForm.classList.toggle('recomment-elem-active')
  }
}
function getReCommentOff(e) {
  const recommentFormOff = document.querySelector(`#recomment-form-${e.target.dataset.commentId}-off`)
  if (e.target.dataset.action == 'reComment') {
    recommentFormOff.classList.toggle('recomment-elem')
    recommentFormOff.classList.toggle('recomment-elem-active')
  }
}
function commentReport() {
  swal("신고가 완료되었습니다.", `감사합니다.`, "success");
}

function deleteComment(e) {
  const comment_pk = e.dataset.commentId;

  axios({
      method: 'get',
      url: `/hobby/${comment_pk}/comment_delete`,
  })
  .then(response => {
    // detail 페이지 댓글 제한 7개
    commentList.innerHTML = ""
    for (let i=0; i < response.data.comments_data.length; i++){
        let isLike = ""
        if (i == 7){
          break;
        }
        if (response.data.comments_data[i].is_like === true) {
          isLike = "heart"
        } else {
          isLike = "heart-outline"
        }
        commentList.insertAdjacentHTML('beforeend', `<hr>
          <div class="d-flex justify-content-between">
          <div class="comment-elem" >
              <img class="comment-image" src="${ response.data.comments_data[i].image }" alt="">
            <div>
              <p>${ response.data.comments_data[i].user }</p>
              <p>${ response.data.comments_data[i].content }</p>
              <div>
                <p class="text-muted" style="font-size:12px"><span>${dayjs.utc(response.data.comments_data[i].created_at).local().fromNow()}</span> <span>좋아요 <span id="comment-${response.data.comments_data[i].pk}-likecnt">${response.data.comments_data[i].likeCount}</span>개</span> 
                <span data-action="reComment" data-comment-id="${response.data.comments_data[i].pk}" style="cursor:pointer;">답글달기</span>
                <ion-icon data-action='getDelete' type="button" data-bs-toggle="modal" data-bs-target="#comment-delete" data-comment-id="${response.data.comments_data[i].pk}" data-user="${ response.data.comments_data[i].user_pk }" name="ellipsis-horizontal"></ion-icon>
                </p>
              </div>
            </div>
          </div>
          <div>
          <ion-icon data-action="like" id="comment-${response.data.comments_data[i].pk}-likebtn" class="comment-like-btn" data-comment-id="${response.data.comments_data[i].pk}" style="color:#E84545" name=${isLike}></ion-icon>
          </div>
          </div>
          <div id="recomment-form-${response.data.comments_data[i].pk}" class="recomment-elem">
          <img class="comment-image" src="${ response.data.comments_data[i].image }" alt="">
          <form id="comment-form" data-hobby-id="${pk}" action=""
            method="POST" class="w-100" data-action="comment-form">
            <input id="commentinput" name="content" class="comment-control" type="text" placeholder="답글 달기...">
            <input class="d-none" type="submit" value="제출">
            <input type="hidden" name="parent" value="${response.data.comments_data[i].pk}">
          </form>
        </div>`)
        for (let j=0; j < response.data.comments_data[i].recomments.length ; j++){
          let isLike = ""
          if (response.data.comments_data[i].recomments[j].is_like === true) {
            isLike = "heart"
          } else {
            isLike = "heart-outline"
          }
          commentList.insertAdjacentHTML('beforeend', `<hr>
          <div class="d-flex justify-content-between ms-5">
          <div class="comment-elem" >
              <img class="comment-image" src="${ response.data.comments_data[i].recomments[j].image }" alt="">
            <div>
              <p>${ response.data.comments_data[i].recomments[j].user }</p>
              <p>${ response.data.comments_data[i].recomments[j].content }</p>
              <div>
                <p class="text-muted" style="font-size:12px"><span>${dayjs.utc(response.data.comments_data[i].recomments[j].created_at).local().fromNow()}</span> <span>좋아요 <span id="comment-${response.data.comments_data[i].recomments[j].pk}-likecnt">${response.data.comments_data[i].recomments[j].likeCount}</span>개</span> 
                <ion-icon data-action='getDelete' type="button" data-bs-toggle="modal" data-bs-target="#comment-delete" data-comment-id="${response.data.comments_data[i].recomments[j].pk}" data-user="${ response.data.comments_data[i].recomments[j].user_pk }" name="ellipsis-horizontal"></ion-icon>
                </p>
              </div>
            </div>
          </div>
          <div>
          <ion-icon data-action="like" id="comment-${response.data.comments_data[i].recomments[j].pk}-likebtn" class="comment-like-btn" data-comment-id="${response.data.comments_data[i].recomments[j].pk}" style="color:#E84545" name=${isLike}></ion-icon>
          </div>
          </div>`
          )};
        };
    commentInput.value = ""
    commentCount.innerText = response.data.comments_len

    
    // 오프캔버스 더보기로 모든 댓글 구현
    commentListOff.textContent = ""
    for (let i=0; i < response.data.comments_data.length; i++){
      let isLike = ""
      if (response.data.comments_data[i].is_like === true) {
        isLike = "heart"
      } else {
        isLike = "heart-outline"
      }
      commentListOff.insertAdjacentHTML('beforeend', `<hr>
        <div class="d-flex justify-content-between">
        <div class="comment-elem" >
            <img class="comment-image" src="${ response.data.comments_data[i].image }" alt="">
          <div>
            <p>${ response.data.comments_data[i].user }</p>
            <p>${ response.data.comments_data[i].content }</p>
            <div>
              <p class="text-muted" style="font-size:12px"><span>${dayjs.utc(response.data.comments_data[i].created_at).local().fromNow()}</span> <span>좋아요 <span id="comment-${response.data.comments_data[i].pk}-likecnt-off">${response.data.comments_data[i].likeCount}</span>개</span> 
              <span data-action="reComment" data-comment-id="${response.data.comments_data[i].pk}" style="cursor:pointer;">답글달기</span>
              <ion-icon data-action='getDelete' type="button" data-bs-toggle="modal" data-bs-target="#comment-delete" data-comment-id="${response.data.comments_data[i].pk}" data-user="${ response.data.comments_data[i].user_pk }" name="ellipsis-horizontal"></ion-icon>
              </p>
            </div>
          </div>
        </div>
        <div>
        <ion-icon data-action="like" id="comment-${response.data.comments_data[i].pk}-likebtn-off" class="comment-like-btn" data-comment-id="${response.data.comments_data[i].pk}" style="color:#E84545" name=${isLike}></ion-icon>
        </div>
        </div>
        <div id="recomment-form-${response.data.comments_data[i].pk}-off" class="recomment-elem">
        <img class="comment-image" src="${ response.data.comments_data[i].image }" alt="">
        <form id="comment-form" data-hobby-id="${pk}" action=""
          method="POST" class="w-100" data-action="comment-form">
          <input id="commentinput" name="content" class="comment-control" type="text" placeholder="답글 달기...">
          <input class="d-none" type="submit" value="제출">
          <input type="hidden" name="parent" value="${response.data.comments_data[i].pk}">
        </form>
      </div>`)
      for (let j=0; j < response.data.comments_data[i].recomments.length ; j++){
        let isLike = ""
        if (response.data.comments_data[i].recomments[j].is_like === true) {
          isLike = "heart"
        } else {
          isLike = "heart-outline"
        }
        commentListOff.insertAdjacentHTML('beforeend', `<hr>
        <div class="d-flex justify-content-between ms-5">
        <div class="comment-elem" >
            <img class="comment-image" src="${ response.data.comments_data[i].recomments[j].image }" alt="">
          <div>
            <p>${ response.data.comments_data[i].recomments[j].user }</p>
            <p>${ response.data.comments_data[i].recomments[j].content }</p>
            <div>
              <p class="text-muted" style="font-size:12px"><span>${dayjs.utc(response.data.comments_data[i].recomments[j].created_at).local().fromNow()}</span> <span>좋아요 <span id="comment-${response.data.comments_data[i].recomments[j].pk}-likecnt-off">${response.data.comments_data[i].recomments[j].likeCount}</span>개</span> 
              <ion-icon data-action='getDelete' type="button" data-bs-toggle="modal" data-bs-target="#comment-delete" data-comment-id="${response.data.comments_data[i].recomments[j].pk}" data-user="${ response.data.comments_data[i].recomments[j].user_pk }" name="ellipsis-horizontal"></ion-icon>
              </p>
            </div>
          </div>
        </div>
        <div>
        <ion-icon data-action="like" id="comment-${response.data.comments_data[i].recomments[j].pk}-likebtn-off" class="comment-like-btn" data-comment-id="${response.data.comments_data[i].recomments[j].pk}" style="color:#E84545" name=${isLike}></ion-icon>
        </div>
        </div>`
        )};
      };
  })
};

// 폼에 이벤트 추가
mainCommentForm.addEventListener('submit', submitComment);
mainCommentFormOff.addEventListener('submit', submitComment);
commentList.addEventListener('submit', submitComment);
commentListOff.addEventListener('submit', submitComment);
// 하트 아이콘 좋아요 이벤트 추가
commentList.addEventListener('click', likeComment);
// ... 아이콘 삭제모달 이벤트 추가
commentList.addEventListener('click', getDeleteComment);
// 대댓글 인풋 이벤트
commentList.addEventListener('click', getReComment);
// 오프캔버스에도 이벤트 추가
commentListOff.addEventListener('click', likeComment);
commentListOff.addEventListener('click', getDeleteComment);
commentListOff.addEventListener('click', getReCommentOff);

// 삭제
const hobbyDelete = document.querySelector('#hobby-delete-btn')
try{
  hobbyDelete.addEventListener('click', gethobbyDelete)
function gethobbyDelete(event) {
  event.preventDefault()
  swal({
    title: "정말로 삭제하시겠습니까?",
    text: "삭제 후에는 소셜링의 복구가 불가능 합니다.",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {
      axios({
        method: 'get',
        url: `/hobby/${pk}/delete_hobby`
      })
      swal("소셜링이 삭제되었습니다.", {
        icon: "success",
        buttons: true,
      })
      .then((redirectbtn) => {
        if (redirectbtn) {
          window.location.replace('/')
        }
      });
    } else {
      swal("소셜링 삭제가 취소되었습니다.");
    }
  });
}
} catch {
  const hobbyCall = document.querySelector('#hobby-call-btn')
  hobbyCall.addEventListener('click', gethobbyCall)
  function gethobbyCall(event) {
    event.preventDefault()
    swal({
      title: "정말로 소셜링에 참여하시겠습니까?",
      text: "호스트의 승인 후에 참여가 완료됩니다.",
      icon: "warning",
      dangerMode: true,
      buttons: true,
      reverseButtons: false,
    })
    .then((willCall) => {
      if (willCall) {
        axios({
          method: 'get',
          url: `/hobby/${pk}/call`
        })
        .then(response => {
          if (response.data.res) {
            swal("신청이 완료되었습니다.", {
              icon: "success",
              buttons: true,
            })
            .then((redirectbtn) => {
              if (redirectbtn) {
                window.location.replace(`/hobby/${pk}`)
              }
            });
          } else {
            swal("이미 신청한 소셜링입니다.", {
              icon: "warning",
              buttons: true,
            });
          }
          
        })
        
      } else {
        swal("소셜링 신청이 취소되었습니다.");
      }
    });
  }
}

// 신청


