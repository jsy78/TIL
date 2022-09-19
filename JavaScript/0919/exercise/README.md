# 웹 09 - JS 03

Date: 2022년 9월 19일

## 수업 내용 복습

> 🔥 JS 문법을 익혀봅니다.

## MDN 문서를 활용한 문법 학습

- 이벤트
    - [https://developer.mozilla.org/ko/docs/Web/API/EventTarget/addEventListener](https://developer.mozilla.org/ko/docs/Web/API/EventTarget/addEventListener)
    - [https://developer.mozilla.org/ko/docs/Web/Events](https://developer.mozilla.org/ko/docs/Web/Events)
    - [https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Build_your_own_function](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Build_your_own_function)
- (심화) 애니메이션 - CSS
    - [https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Animations/Using_CSS_animations](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Animations/Using_CSS_animations)
    - [https://web.dev/learn/css/animations/](https://web.dev/learn/css/animations/)
    - [https://web.dev/learn/css/transitions/](https://web.dev/learn/css/transitions/)
    

## 실습


- `02_input.html` input에 작성된 내용을 그대로 출력하기
- `04_modal.html` 모달 직접 만들어보기
- `05_carousel.html` 이전(previous) 버튼 만들기
- 비밀번호 및 비밀번호 일치 여부 확인하기
    - 조건
        - 비밀번호는 8자리 이상이어야 합니다.
        - 비밀번호는 비밀번호와 비밀번호 확인 값이 일치해야 합니다.
    - 일치하지 않는 경우 `alert` 를 통해 메시지를 전달합니다.
    
    ```html
    <form action="">
      <input type="password" name="password" id="password">
      <input type="password" name="password_confirmation" id="password_confirmation">
    </form>
    ```