SELECT * 
FROM albums JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;

SELECT * 
FROM albums LEFT JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;
