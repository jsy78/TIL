import json
from pprint import pprint


def movie_info(movie):
    result = {}    
    result['genre_ids'] = movie['genre_ids']
    result['id'] = movie['id']
    result['overview'] = movie['overview']
    result['title'] = movie['title']
    result['vote_average'] = movie['vote_average']

    return result
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    pprint(movie_info(movie))