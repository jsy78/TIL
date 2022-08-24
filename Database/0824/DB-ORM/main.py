import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

# 3.
import datetime
Director.objects.create(name='봉준호', debut=datetime.date(1993, 1, 1), country='KOR')
Director.objects.create(name='김한민', debut=datetime.date(1999, 1, 1), country='KOR')
Director.objects.create(name='최동훈', debut=datetime.date(2004, 1, 1), country='KOR')
Director.objects.create(name='이정재', debut=datetime.date(2022, 1, 1), country='KOR')
Director.objects.create(name='이경규', debut=datetime.date(1992, 1, 1), country='KOR')
Director.objects.create(name='한재림', debut=datetime.date(2005, 1, 1), country='KOR')
Director.objects.create(name='Joseph Kosinski', debut=datetime.date(1999, 1, 1), country='KOR')
Director.objects.create(name='김철수', debut=datetime.date(2022, 1, 1), country='KOR')

# 4.
genre = Genre()
genre.title = '액션'
genre.save()
genre = Genre()
genre.title = '드라마'
genre.save()
genre = Genre()
genre.title = '사극'
genre.save()
genre = Genre()
genre.title = '범죄'
genre.save()
genre = Genre()
genre.title = '스릴러'
genre.save()
genre = Genre()
genre.title = 'SF'
genre.save()
genre = Genre()
genre.title = '무협'
genre.save()
genre = Genre()
genre.title = '첩보'
genre.save()
genre = Genre()
genre.title = '재난'
genre.save()

# 5.
directors = Director.objects.all()
for director in directors :
    print(f'{director.name} {director.debut} {director.country}')

# 6. 
director = Director.objects.get(id=1)
print(f'{director.name} {director.debut} {director.country}')

# 7.
director = Director.objects.get(country='USA')
print(f'{director.name} {director.debut} {director.country}')

# 9.
director = Director.objects.get(name='Joseph Kosinski')
director.country = 'USA'
director.save()
print(f'{director.name} {director.debut} {director.country}')

# 10.
director = Director.objects.get(country='KOR')
print(f'{director.name} {director.debut} {director.country}')

# 12.
directors = Director.objects.filter(country='KOR')
for director in directors :
    print(f'{director.name} {director.debut} {director.country}')

# 14.
director = Director.objects.get(name='김철수')
director.delete()
