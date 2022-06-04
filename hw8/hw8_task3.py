import requests
import time
from datetime import datetime, timedelta
from pprint import pprint


difdate = datetime.now() - timedelta(days=2)
fromdate = str(int(time.mktime(difdate.timetuple())))
todate = str(int(time.mktime(datetime.now().timetuple())))
page_counter = 1
url = 'https://api.stackexchange.com/2.3/questions'
# Параметрируем запрос с использованием кастомного фильтра,
# выдающего общее количество вопросов.
params = {'fromdate' : fromdate, 'todate' : todate, 'order' : 'desc',
'sort' : 'activity',  'tagged' : 'Python', 'site' : 'stackoverflow',
'pagesize' : '100', 'page' : str(page_counter), 'filter' : '!-)8(vv2Ibd0Q'}
response = requests.get(url, params=params)
pprint(response.json())
# Проверяем необходимость в дополнительных запросах.
has_more = response.json().get('has_more')
while has_more:
    time.sleep(0.25)
    page_counter +=1
    params['page'] = str(page_counter)
    response = requests.get(url, params=params)
    pprint(response.json())
    has_more = response.json().get('has_more')

print(f'На сайте stackoverflow {response.json().get("total")} вопросов \
с {time.ctime(float(fromdate))} по {time.ctime(float(todate))} по тэгу Python')