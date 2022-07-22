import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

def recommendation(title):
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

    recommend_path = f'/movie/{search_responese_first}/recommendations'
    recommend_params = {
        'api_key' : os.environ.get('API_KEY'), 
        'language' : 'ko-KR',
        'page' : '1',
    }
    recommend_response = requests.get(base_url+recommend_path, params=recommend_params).json().get('results')
    recommend_titles = [d['title'] for d in recommend_response]

    return recommend_titles
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
