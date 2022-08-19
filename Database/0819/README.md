### 1. 모든 테이블의 이름을 출력하세요.

```bash
sqlite> .header on
sqlite> .mode column
sqlite> .tables
albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track
```

### 2. 모든 테이블의 데이터를 확인해보세요.
| 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.

```bash
sqlite> .schema
CREATE TABLE IF NOT EXISTS "albums"
(
    [AlbumId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    FOREIGN KEY ([ArtistId]) REFERENCES "artists" ([ArtistId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE IF NOT EXISTS "artists"
(
    [ArtistId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(120)
);
CREATE TABLE IF NOT EXISTS "customers"
(
    [CustomerId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [FirstName] NVARCHAR(40)  NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [Company] NVARCHAR(80),
    [Address] NVARCHAR(70),
    [City] NVARCHAR(40),
    [State] NVARCHAR(40),
    [Country] NVARCHAR(40),
    [PostalCode] NVARCHAR(10),
    [Phone] NVARCHAR(24),
    [Fax] NVARCHAR(24),
    [Email] NVARCHAR(60)  NOT NULL,
    [SupportRepId] INTEGER,
    FOREIGN KEY ([SupportRepId]) REFERENCES "employees" ([EmployeeId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE IF NOT EXISTS "employees"
(
    [EmployeeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [FirstName] NVARCHAR(20)  NOT NULL,
    [Title] NVARCHAR(30),
    [ReportsTo] INTEGER,
    [BirthDate] DATETIME,
    [HireDate] DATETIME,
    [Address] NVARCHAR(70),
    [City] NVARCHAR(40),
    [State] NVARCHAR(40),
    [Country] NVARCHAR(40),
    [PostalCode] NVARCHAR(10),
    [Phone] NVARCHAR(24),
    [Fax] NVARCHAR(24),
    [Email] NVARCHAR(60),
    FOREIGN KEY ([ReportsTo]) REFERENCES "employees" ([EmployeeId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE IF NOT EXISTS "genres"
(
    [GenreId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(120)
);
CREATE TABLE IF NOT EXISTS "invoices"
(
    [InvoiceId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [CustomerId] INTEGER  NOT NULL,
    [InvoiceDate] DATETIME  NOT NULL,
    [BillingAddress] NVARCHAR(70),
    [BillingCity] NVARCHAR(40),
    [BillingState] NVARCHAR(40),
    [BillingCountry] NVARCHAR(40),
    [BillingPostalCode] NVARCHAR(10),
    [Total] NUMERIC(10,2)  NOT NULL,
    FOREIGN KEY ([CustomerId]) REFERENCES "customers" ([CustomerId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE IF NOT EXISTS "invoice_items"
(
    [InvoiceLineId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [InvoiceId] INTEGER  NOT NULL,
    [TrackId] INTEGER  NOT NULL,
    [UnitPrice] NUMERIC(10,2)  NOT NULL,
    [Quantity] INTEGER  NOT NULL,
    FOREIGN KEY ([InvoiceId]) REFERENCES "invoices" ([InvoiceId])
                ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES "tracks" ([TrackId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE IF NOT EXISTS "media_types"
(
    [MediaTypeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(120)
);
CREATE TABLE IF NOT EXISTS "playlists"
(
    [PlaylistId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(120)
);
CREATE TABLE IF NOT EXISTS "playlist_track"
(
    [PlaylistId] INTEGER  NOT NULL,
    [TrackId] INTEGER  NOT NULL,
    CONSTRAINT [PK_PlaylistTrack] PRIMARY KEY  ([PlaylistId], [TrackId]),
    FOREIGN KEY ([PlaylistId]) REFERENCES "playlists" ([PlaylistId])
                ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES "tracks" ([TrackId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE TABLE IF NOT EXISTS "tracks"
(
    [TrackId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(200)  NOT NULL,
    [AlbumId] INTEGER,
    [MediaTypeId] INTEGER  NOT NULL,
    [GenreId] INTEGER,
    [Composer] NVARCHAR(220),
    [Milliseconds] INTEGER  NOT NULL,
    [Bytes] INTEGER,
    [UnitPrice] NUMERIC(10,2)  NOT NULL,
    FOREIGN KEY ([AlbumId]) REFERENCES "albums" ([AlbumId])
                ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([GenreId]) REFERENCES "genres" ([GenreId])
                ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([MediaTypeId]) REFERENCES "media_types" ([MediaTypeId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE INDEX [IFK_AlbumArtistId] ON "albums" ([ArtistId]);
CREATE INDEX [IFK_CustomerSupportRepId] ON "customers" ([SupportRepId]);
CREATE INDEX [IFK_EmployeeReportsTo] ON "employees" ([ReportsTo]);
CREATE INDEX [IFK_InvoiceCustomerId] ON "invoices" ([CustomerId]);
CREATE INDEX [IFK_InvoiceLineInvoiceId] ON "invoice_items" ([InvoiceId]);
CREATE INDEX [IFK_InvoiceLineTrackId] ON "invoice_items" ([TrackId]);
CREATE INDEX [IFK_PlaylistTrackTrackId] ON "playlist_track" ([TrackId]);
CREATE INDEX [IFK_TrackAlbumId] ON "tracks" ([AlbumId]);
CREATE INDEX [IFK_TrackGenreId] ON "tracks" ([GenreId]);
CREATE INDEX [IFK_TrackMediaTypeId] ON "tracks" ([MediaTypeId]);
CREATE TABLE sqlite_stat1(tbl,idx,stat);
```

```sql
SELECT * FROM albums;
SELECT * FROM employees;
SELECT * FROM invoices;
SELECT * FROM playlists;
SELECT * FROM artists;
SELECT * FROM genres;
SELECT * FROM media_types;
SELECT * FROM tracks;
SELECT * FROM customers;
SELECT * FROM invoice_items;
SELECT * FROM playlist_track;
```

### 3. 앨범(albums) 테이블의 데이터를 출력하세요.
| 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.

```sql
SELECT * FROM albums ORDER BY Title DESC LIMIT 5;
```

```
AlbumId  Title                         ArtistId
-------  ----------------------------  --------
208      [1997] Black Light Syndrome   136
240      Zooropa                       150
267      Worlds                        202
334      Weill: The Seven Deadly Sins  264
8        Warner 25 Anos                6
```

### 4. 고객(customers) 테이블의 행 개수를 출력하세요.
| 단, 컬럼명을 `고객 수`로 출력하세요.

```sql
SELECT COUNT(*) AS "고객 수" FROM customers;
```

```
고객 수
----
59
```

### 5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.
| 단, 각각의 컬럼명을 `이름`, `성`으로 출력하고, `이름`을 기준으로 내림차순으로 5개까지 출력하세요.

```sql
SELECT FirstName AS "이름", LastName AS "성" FROM customers WHERE Country = 'USA' ORDER BY "이름" DESC LIMIT 5;
```

```
이름        성
--------  ----------
Victor    Stevens
Tim       Goyer
Richard   Cunningham
Patrick   Gray
Michelle  Brooks
```

### 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.
| 단, 컬럼명을 `송장수`로 출력하세요.

```sql
SELECT COUNT(*) AS "송장수" FROM invoices WHERE BillingPostalCode IS NOT NULL;
```

```
송장수
---
384
```

### 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.
| 단, `InvoiceDate`를 기준으로 내림차순으로 5개까지 출력하세요.

```sql
SELECT * FROM invoices WHERE BillingState IS NULL ORDER BY InvoiceDate DESC LIMIT 5;
```

```
InvoiceId  CustomerId  InvoiceDate          BillingAddress                            BillingCity   BillingState  BillingCountry  BillingPostalCode  Total     
---------  ----------  -------------------  ----------------------------------------  ------------  ------------  --------------  -----------------  -----     
412        58          2013-12-22 00:00:00  12,Community Centre                       Delhi                       India           110017             1.99      
411        44          2013-12-14 00:00:00  Porthaninkatu 9                           Helsinki                    Finland         00530              13.86     
410        35          2013-12-09 00:00:00  Rua dos Campeoes Europeus de Viena, 4350  Porto                       Portugal                           8.91      
404        6           2013-11-13 00:00:00  Rilska 3174/6                             Prague                      Czech Republic  14300              25.86     
403        56          2013-11-08 00:00:00  307 Macacha Guemes                        Buenos Aires                Argentina       1106               8.91      
```

### 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.
| `strftime`를 검색해서 활용해보세요.

```sql
SELECT COUNT(*) FROM invoices WHERE STRFTIME('%Y', InvoiceDate) = '2013';
```

```
COUNT(*)
--------
80
```

### 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.
| 단, 각각의 컬럼명을 `고객ID`, `이름`,`성`으로 출력하고, `고객ID`을 기준으로 오름차순으로 출력하세요.

```sql
SELECT CustomerId AS "고객ID", FirstName AS "이름", LastName AS "성" FROM customers WHERE SUBSTR(FirstName, 1, 1) = 'L' ORDER BY "고객ID" ASC;
```

```
고객ID  이름        성
----  --------  ---------
1     Luis      Goncalves
2     Leonie    Kohler
45    Ladislav  Kovacs
47    Lucas     Mancini
57    Luis      Rojas
```

### 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.
| 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.

```sql
SELECT COUNT(*) AS "고객 수", Country AS "나라" FROM customers GROUP BY Country ORDER BY "고객 수" DESC LIMIT 5;
```

```
고객 수  나라
----  -------
13    USA
8     Canada
5     France
5     Brazil
4     Germany
```

### 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.

```sql
SELECT ArtistID, COUNT(*) AS "앨범 수" FROM albums GROUP BY ArtistID ORDER BY "앨범 수" DESC LIMIT 1;
```

```
ArtistId  앨범 수
--------  ----
90        21
```

### 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요
| 단, 앨범 수를 기준으로 내림차순으로 출력하세요.

```sql 
SELECT ArtistID, COUNT(*) AS "앨범 수" FROM albums GROUP BY ArtistID HAVING COUNT(*) >= 10 ORDER BY "앨범 수" DESC;
```
```sqlite
-- 이게 되네...
SELECT ArtistID, COUNT(*) AS "앨범 수" FROM albums GROUP BY ArtistID HAVING "앨범 수" >= 10 ORDER BY "앨범 수" DESC;
```

```
ArtistId  앨범 수
--------  ----
90        21
22        14
58        11
50        10
150       10
```

### 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.
| 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.

```sql 
SELECT COUNT(*) AS "고객 수", Country, State FROM customers WHERE State IS NOT NULL GROUP BY Country, State ORDER BY "고객 수" DESC, Country DESC LIMIT 5;
```

```
고객 수  Country  State
----  -------  -----
3     USA      CA
3     Brazil   SP
2     Canada   ON
1     USA      WI
1     USA      WA
```

### 14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.
| 단, `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 

```sql 
SELECT CustomerID, 
       CASE
           WHEN Fax IS NULL THEN 'X'
           ELSE 'O'
       END AS "Fax 유/무"
FROM customers
ORDER BY CustomerID ASC
LIMIT 5;       
```

```
CustomerId  Fax 유/무
----------  -------
1           O
2           X
3           X
4           X
5           O
```

### 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.
| 단, 점원의 `LastName`, `FirstName`, `나이` 컬럼만 출력하고, `EmployeeId`를 기준으로 오름차순으로 출력하세요.

| cast(), strftime(), 오늘 날짜를 구하는 함수를 검색하고, 활용해보세요.

```sql 
SELECT LastName, 
       FirstName, 
       CAST(STRFTIME('%Y', CURRENT_TIMESTAMP, 'LOCALTIME') AS INT) - CAST(STRFTIME('%Y', BirthDate) AS INT) + 1 AS "나이"
FROM employees
ORDER BY EmployeeId ASC;
```

```
LastName  FirstName  나이
--------  ---------  --
Adams     Andrew     61
Edwards   Nancy      65
Peacock   Jane       50
Park      Margaret   76
Johnson   Steve      58
Mitchell  Michael    50
King      Robert     53
Callahan  Laura      55
```

### 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.
| artists 테이블과 albums 테이블의 `ArtistId` 활용하세요.

```sql 
SELECT Name
FROM artists
WHERE ArtistId = (SELECT ArtistID
                  FROM albums 
                  GROUP BY ArtistID 
                  ORDER BY COUNT(*) DESC
                  LIMIT 1);
```

```
Name
-----------
Iron Maiden
```

### 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.
| genres 테이블과 tracks 테이블의 `GenreId` 활용하세요.

```sql 
SELECT Name
FROM genres
WHERE GenreId = (SELECT GenreId
                 FROM tracks 
                 GROUP BY GenreId 
                 ORDER BY COUNT(*) ASC
                 LIMIT 1);
```

```
Name
-----
Opera
```