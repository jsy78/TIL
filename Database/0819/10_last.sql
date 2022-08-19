-- AC/DC의 모든 앨범
-- AC/DC (artists)
-- 앨범(albums)

-- 앨범 검색하려고 했는데..
-- 아티스는 id로 저장되어있네요.
-- AC/DC는 아는데 ID를 모르네요?

-- ID 조회
SELECT ArtistId 
FROM artists
WHERE Name = 'Nirvana';

-- 서브쿼리
SELECT * 
FROM albums
WHERE ArtistId = (SELECT ArtistId 
FROM artists
WHERE Name = 'Nirvana');