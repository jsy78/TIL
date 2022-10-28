# GitHub 병합 충돌 처리 가이드

```
❗ 병합 충돌이 발생하는 원인
병합 충돌은 동일한 파일의 동일한 줄의 코드를 다르게 작성했을 때 발생합니다.
(코드를 똑같이 작성했을 때에는 충돌이 발생하지 않음.)
```

```
❓ 아래 이미지의 충돌 상황
1. A 개발자가 articles 앱을 만들고, settings.py / urls.py을 수정한 후 master 브랜치에 병합
2. B 개발자가 accounts 앱을 만들고, settings.py / urls.py을 수정한 후 master 브랜치로 PR 생성
3. A, B 개발자가 동시에 수정한 settings.py / urls.py에서 병합 충돌(merge conflict) 발생
```

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled.png)

```
1️⃣ 충돌 해결을 위해 Resolve conflicts 버튼 클릭
```

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%201.png)

```
2️⃣ 각 파일에서 충돌(conflict)가 발생한 코드 뭉치 해결
충돌이 난 부분에서 필요한 코드만 남기고, 수정 삭제합니다.
```

`settings.py`

- 수정 전
  
    ‘account’, 와 ‘articles’, 가 충돌난 상태
    

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%202.png)

- 수정 후
  
    두 줄 모두 필요해서 구분선(`<<<<<<` , `======` , `>>>>>`)만 삭제
    

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%203.png)

`urls.py`

- 수정 전
  
    두 path가 충돌난 상태
    

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%204.png)

- 수정 후
  
    두 path 보존 / 각 path 마지막에 쉼표(`,`) 추가 /  구분선 삭제
    

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%205.png)

```
3️⃣ 모든 파일 충돌 해결 완료 확인 후 `Mark as resolved` 클릭
```

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%206.png)

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%207.png)

```
4️⃣ 파일 확인 후 `Commit Merge` 클릭
```

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%208.png)

```
5️⃣ 병합 진행
```

![Untitled](./GitHub%20병합%20충돌%20처리%20가이드/Untitled%209.png)