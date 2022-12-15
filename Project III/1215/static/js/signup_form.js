const slide = document.querySelector(".slide");
const prevBtn = document.querySelector(".slide_prev_button");
const nextBtn = document.querySelector(".slide_next_button");
const slideItems = document.querySelectorAll(".slide_item");
const maxSlide = slideItems.length;
const submit_Btn = document.querySelector("#submit_btn")

let currSlide = 1;

nextBtn.addEventListener("click", () => {
  currSlide++;
  let slideWidth = slide.clientWidth;

  if (currSlide >= maxSlide) {
    nextBtn.style.display = "none";
    submit_Btn.style.display = "block";
  } else {
    nextBtn.style.display = "block";
  }

  if (currSlide <= maxSlide) {
    const offset = slideWidth * (currSlide - 1);
    slideItems.forEach((i) => {
      i.setAttribute("style", `left: ${ - offset}px`);
    });
    // 슬라이드 이동 시 현재 활성화된 pagination 변경
  } else {
    currSlide--;
  }
});
// 버튼 엘리먼트에 클릭 이벤트 추가하기
prevBtn.addEventListener("click", () => {
  // 이전 버튼 누를 경우 현재 슬라이드를 변경
  currSlide--;
  let slideWidth = slide.clientWidth;

  if (currSlide <= maxSlide) {
    nextBtn.style.display = "block";
    submit_Btn.style.display = "none";
  }
  // 1번째 슬라이드 이하로 넘어가지 않게 하기 위해서
  if (currSlide > 0) {
    // 슬라이드를 이동시키기 위한 offset 계산
    const offset = slideWidth * (currSlide - 1);
    // 각 슬라이드 아이템의 left에 offset 적용
    slideItems.forEach((i) => {
      i.setAttribute("style", `left: ${ - offset}px`);
    });
  } else {
    currSlide++;
  }
});

