import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

def credits(title):
    base_url = 'https://api.themoviedb.org/3'
    search_path = '/search/movie'
    search_params = {
        'api_key' : os.environ.get('API_KEY'), 
        'language' : 'ko-KR',
        'page' : '1',
        'query' : title,
        'include_adult' : False
    }

    search_response = requests.get(base_url+search_path, params=search_params).json().get('results')
    if len(search_response) == 0 :
        return None
    
    search_responese_first = search_response.pop(0).get('id')

    credit_path = f'/movie/{search_responese_first}/credits'
    credit_params = {
        'api_key' : os.environ.get('API_KEY'), 
        'language' : 'ko-KR',
    }
    credit_response = requests.get(base_url+credit_path, params=credit_params).json()
    
    credit_cast = credit_response.get('cast')
    credit_crew = credit_response.get('crew')

    cast_list = [d['name'] for d in credit_cast if d['cast_id'] < 10]
    crew_list = [d['name'] for d in credit_crew if d['department'] == 'Directing']

    return {'cast' : cast_list, 'crew' : crew_list}
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
