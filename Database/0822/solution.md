```sql
SELECT * 
FROM albums JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;

SELECT * 
FROM albums LEFT JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;
```

### . playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT * FROM playlist_track A
ORDER BY A.PlaylistId DESC
LIMIT 5;
```

### . tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT * FROM tracks B
ORDER BY B.TrackId
LIMIT 5;
```

### . 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT A.PlaylistId, B.Name FROM playlist_track A
INNER JOIN tracks B
ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId DESC
LIMIT 10;
```
-- 18	Now's The Time
-- 17	The Zoo
-- 17	Flying High Again
-- 17	Crazy Train
-- 17	I Don't Know
-- 17	Looks That Kill
-- 17	Live To Win
-- 17	Ace Of Spades
-- 17	Creeping Death
-- 17	For Whom The Bell Tolls
​
### . `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼만 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.PlaylistId, B.Name FROM playlist_track A
INNER JOIN tracks B
ON A.TrackId = B.TrackId
WHERE A.PlaylistId = 10
ORDER BY B.Name DESC
LIMIT 5;
```
-- 10	Women's Appreciation
-- 10	White Rabbit
-- 10	Whatever the Case May Be
-- 10	What Kate Did
-- 10	War of the Gods, Pt. 2
​
### . tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT count(*) FROM tracks A
INNER JOIN artists B
ON A.Composer = B.Name;
```
-- 402
​
### . tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT count(*) FROM tracks A
LEFT JOIN artists B
ON A.Composer = B.Name;
```
-- 3503
​
### . `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
```

### . invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼만 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId FROM invoice_items
ORDER BY InvoiceId 
LIMIT 5;
```
-- 1	1
-- 2	1
-- 3	2
-- 4	2
-- 5	2
​
### . invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼만 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId, CustomerId FROM invoices
ORDER BY InvoiceId 
LIMIT 5;
```
-- 1	2
-- 2	4
-- 3	8
-- 4	14
-- 5	23
​
### . 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼만 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT A.InvoiceLineId, B.InvoiceId FROM invoice_items A
INNER JOIN invoices B
ON A.InvoiceId = B.InvoiceId
ORDER BY B.InvoiceId DESC
LIMIT 5;
```
-- 2240	412
-- 2226	411
-- 2227	411
-- 2228	411
-- 2229	411
​
​
### . 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼만 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT A.InvoiceId, B.CustomerId FROM invoices A
INNER JOIN customers B
ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;
```
-- 412	58
-- 411	44
-- 410	35
-- 409	29
-- 408	25
​
### . 각 invoices_item에 해당하는 invoice, customer 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼만  `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT A.InvoiceLineId, A.InvoiceId, C.CustomerId 
FROM invoice_items A
    INNER JOIN invoices B
        ON A.InvoiceId = B.InvoiceId
    INNER JOIN customers C
        ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;
```
-- 2240	412	58
-- 2239	411	44
-- 2238	411	44
-- 2237	411	44
-- 2236	411	44
​
### . 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼만 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT C.CustomerId, count(*) FROM invoice_items A
INNER JOIN (
    SELECT * FROM invoices A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
) C
ON A.InvoiceId = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;
```
-- 1	38
-- 2	38
-- 3	38
-- 4	38
-- 5	38