import json
from pprint import pprint


def movie_info(movie, genres):
    result = {}
    genre_id_name = {}

    for d in genres :
        genre_id_name[d['id']] = d['name']

    genre_name = []
    for id in movie['genre_ids'] :
        genre_name.append(genre_id_name[id])
    movie['genre_names'] = genre_name
      
    result['genre_names'] = movie['genre_names']
    result['id'] = movie['id']
    result['overview'] = movie['overview']
    result['title'] = movie['title']
    result['vote_average'] = movie['vote_average']

    return result
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movie.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))