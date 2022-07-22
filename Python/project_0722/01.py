import requests
import os
from dotenv import load_dotenv

load_dotenv()

def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : os.environ.get('API_KEY'), 
        'language' : 'ko-KR',
        'page' : '1'
    }
    
    response = requests.get(base_url+path, params=params).json().get('results')
    return len(response)

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
