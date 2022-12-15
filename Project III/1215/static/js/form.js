const slide = document.querySelector(".slide");
let slideWidth = slide.clientWidth;
const prevBtn = document.querySelector(".slide_prev_button");
const nextBtn = document.querySelector(".slide_next_button");
const submitBtn = document.querySelector(".submit_btn")
const slideItems = document.querySelectorAll(".slide_item");
const maxSlide = slideItems.length;
let currSlide = 1;
const pagination = document.querySelector(".slide_pagination");
const progress = document.querySelector('#progress_bar');
progress.setAttribute('style', `width:${(currSlide/maxSlide)*100}%`);
const radio_1 = document.querySelector("#social_label");
const radio_2 = document.querySelector("#club_label");
// 엔터 submit prevent
document.myform.addEventListener("submit", event => {
  event.preventDefault()
  if (event.code === "Enter") {
  event.preventDefault()};
});
// 다음 버튼 이벤트
nextBtn.addEventListener("click", () => {
  currSlide++;
  if (currSlide < maxSlide) {
    progress.setAttribute('style', `width:${(currSlide/maxSlide)*100}%`)
    const offset = slideWidth * (currSlide - 1);
    slideItems.forEach((i) => {
      i.setAttribute("style", `left: ${-offset}px`);
    });
  } else if (currSlide == maxSlide) {
    nextBtn.classList.add('d-none')
    submitBtn.classList.remove('d-none')
    progress.setAttribute('style', `width:${(currSlide/maxSlide)*100}%`)
    const offset = slideWidth * (currSlide - 1);
    slideItems.forEach((i) => {
      i.setAttribute("style", `left: ${-offset}px`);
    });
  } else {
    currSlide--;
  }
});
// 이전 버튼 이벤트
prevBtn.addEventListener("click", () => {
  currSlide--;
  if (currSlide > 0) {
    nextBtn.classList.remove('d-none')
    submitBtn.classList.add('d-none')
    progress.setAttribute('style', `width:${(currSlide/maxSlide)*100}%`)
    const offset = slideWidth * (currSlide - 1);
    slideItems.forEach((i) => {
      i.setAttribute("style", `left: ${-offset}px`);
    });
  } else {
    window.history.back() // 1페이지에서 이전을 눌렀을 경우 뒤로가기
  }
});
// 창 크기 리사이징
window.addEventListener("resize", () => {
  slideWidth = slide.clientWidth;
});
// 소셜링, 클럽 소셜링 선택
radio_1.addEventListener("click", () => {
  radio_1.classList.add('radio-active')
  radio_2.classList.remove('radio-active')
});
radio_2.addEventListener("click", () => {
  radio_2.classList.add('radio-active')
  radio_1.classList.remove('radio-active')
});
// 태그 이벤트 _ 다른 카테고리 선택시 현재 선택된 태그 해제
const tags = document.querySelectorAll('div.accordion-body > .tag-btn');
const tag_input = document.querySelector('#tag')
var n_tag = null;
[].forEach.call(tags, function(tag){
	tag.addEventListener("click", () => {
    for (let j=0; j<(tags.length); j++){
      tags[j].classList.remove('tag-btn-active')
    }
  tag.classList.add('tag-btn-active')
  n_tag = tag;
  tag_input.value = tag.value
  }); 
}); 
// 카테고리 이벤트 _ 카테고리 선택
const categories = document.querySelectorAll('.categories');
[].forEach.call(categories, function(category){ 
	category.addEventListener("click", () => {
    for (let j=0; j<(categories.length); j++){
      categories[j].classList.remove('radio-active')
    }
    category.classList.add('active')
    n_tag.classList.remove('tag-btn-active')
    tag_input.value = ''
  });
});

function changeinner(event) {
  n_tag.innerText = event.parentNode.parentNode.querySelector('#tag').value
}
// 이미지 미리보기
const label = document.querySelector('.image-control')
function setThumbnail(event) {
  var reader = new FileReader();
  reader.onload = function(event) {
    document.createElement("img");
    label.style.backgroundImage = `url(${event.target.result})`;
  };

  reader.readAsDataURL(event.target.files[0]);
}
const imageInput = document.querySelector('#image')
imageInput.addEventListener('change', setThumbnail )

// Date/ Time picker

// 온라인, 오프라인 버튼 active
const offlinebtn = document.querySelector('#offline-btn');
const onlinebtn = document.querySelector('#online-btn');
const addrcheck = document.querySelector('#address_type');
const addrbox = document.querySelector('#offline-box');
const address = document.querySelector('#address')

offlinebtn.addEventListener('click', () => {
  offlinebtn.classList.toggle('addr-btn-active');
  onlinebtn.classList.remove('addr-btn-active');
  addrbox.classList.toggle('d-none');
  addrcheck.checked = false
});
onlinebtn.addEventListener('click', () => {
  onlinebtn.classList.toggle('addr-btn-active');
  offlinebtn.classList.remove('addr-btn-active');
  addrbox.classList.add('d-none');
  addrcheck.checked = true
  address.value = '온라인'
});

// 키워드로 검색하기
const keysearch = document.querySelector('#keysearch');
const addrdiv = document.querySelector('#addrlist');
const offbuttonaddr = document.querySelector('#offbuttonaddr');
const testBtn = document.querySelector('#testbtn');
const addrBody = document.querySelector('#addrbody');
var places = new kakao.maps.services.Places();

var callback = function(result, status, pagination) {
    console.log(result.length)
    const nextPagination = function () {
      // 속성 값으로 다음 페이지가 있는지 확인하고
      if (pagination.hasNextPage) {
          pagination.nextPage()
          console.log('nextpage')
      }
    }
    testBtn.onclick = nextPagination
    if (status === kakao.maps.services.Status.OK && pagination.current == 1) {
      console.log(pagination.current)
      arr = []
      for (let i = 0; i < (result.length); i++) {
        arr += `<li class="m-3 addrelem" data-bs-dismiss="offcanvas" aria-label="Close"><p class="addr_title">${result[i].place_name}</p><p class="addr_addr">${result[i].address_name}</p></li><hr>`
      };
      addrdiv.innerHTML = arr
      const addrelems = document.querySelectorAll('.addrelem');

      [].forEach.call(addrelems, function(elem) {
        elem.addEventListener('click', () => {
          offbuttonaddr.innerText = elem.firstChild.innerText
          address.value = elem.firstChild.innerText
        })
      });
    } else if (status === kakao.maps.services.Status.OK) {
      console.log(pagination.current)
      arr = []
      for (let i = 0; i < (result.length); i++) {
        arr += `<li class="m-3 addrelem" data-bs-dismiss="offcanvas" aria-label="Close"><p class="addr_title">${result[i].place_name}</p><p class="addr_addr">${result[i].address_name}</p></li><hr>`
      };
      addrdiv.insertAdjacentHTML('beforeend', arr)
      const addrelems = document.querySelectorAll('.addrelem');

      [].forEach.call(addrelems, function(elem) {
        elem.addEventListener('click', () => {
          offbuttonaddr.innerText = elem.firstChild.innerText
          address.value = elem.firstChild.innerText
        })
      });
    }

};
keysearch.addEventListener('keyup', () => {
  places.keywordSearch(`${keysearch.value}`, callback, {size: 6});
})

// 제한인원 설정하기
let limit = 3
const limit_minus = document.querySelector('#remove-circle');
const limit_plus = document.querySelector('#add-circle');
const limit_n = document.querySelector('#limit_n')
const limit_input = document.querySelector('#limit')
limit_minus.addEventListener('click', () => {
  if (limit > 3) {
    limit--
    limit_n.innerText = limit
    limit_input.value = limit
  } else {
    swal('최소 인원은 3명 입니다.', {
      icon: 'info',
    })
  }
});
limit_plus.addEventListener('click', () => {
  if (limit < 15) {
    limit++
    limit_n.innerText = limit
    limit_input.value = limit
  } else {
    swal('최대 인원은 15명 입니다.', {
      icon: 'info',
    })
  }
});

// 참가비 설정하기
const entry_fee = document.querySelector('#entryfee-btn');
const free_fee = document.querySelector('#entryfree-btn');
const fee_box = document.querySelector('#entry_box');
const fee_input = document.querySelector('#entry_fee')

entry_fee.addEventListener('click', () => {
  entry_fee.classList.toggle('addr-btn-active');
  free_fee.classList.remove('addr-btn-active');
  fee_box.classList.toggle('d-none');
});
free_fee.addEventListener('click', () => {
  free_fee.classList.toggle('addr-btn-active');
  entry_fee.classList.remove('addr-btn-active');
  fee_box.classList.add('d-none');
  fee_input.value = ''
});

//  유효성 검사 & 글자수 카운터
const titleInput = document.querySelector('#title')
const meetingDay = document.querySelector('#meeting_day')
const errorMessage = document.querySelector('.error-message')
const inputTags = document.querySelector('#tag')
const inputTitle = document.querySelector('#title')
// 카운터 span
const counterTags = document.querySelector('#control-input-tags')
inputTags.addEventListener('input', function(){
  counterTags.innerText = inputTags.value.length + '/10';
});
const counterTitle = document.querySelector('#control-input-title')
inputTitle.addEventListener('input', function(){
  counterTitle.innerText = inputTitle.value.length + '/80';
});

submitBtn.addEventListener('click', checkvalid)
function checkvalid(e) {
  let arr = []
  e.preventDefault()
  if (tag_input.value === "") {
    arr.push('주제 선택')};
  if (titleInput.value === "") {
    arr.push('제목')};
  if (meetingDay.value === "") {
    arr.push('소셜링 일시')};
  if (address.value === "") {
    arr.push('장소 선택')};
  if (arr.length != 0) {
    let temp = ""
    for (let i = 0; i < arr.length; i++){
      if (i === (arr.length-1)) {
        temp += arr[i]
      } else {
        temp += arr[i]+', '
      }
    }
    errorMessage.innerText = temp + '(은)는 필수 입력사항입니다.'
    swal("필수 사항을 입력해주세요!", `${temp}(은)는 필수 입력사항입니다.`, "error");
  } else {
    errorMessage.innerText = ""
    document.myform.submit();
  }
}