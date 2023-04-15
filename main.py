import requests
import os
import datetime as dt
from pprint import pprint 

# №1
def get_intelligence_hero(list_heroes = ['Hulk', 'Captain America', 'Thanos']):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)

    if response.status_code == 200:
        all_heroes = response.json()
        heroes_intelligence = {}
        for hero in all_heroes:
            if hero['name'] in list_heroes:   
                heroes_intelligence[hero.get('name')] = hero.get('powerstats').get('intelligence')
        return max(heroes_intelligence, key=heroes_intelligence.get)
    else:
        return 'Error request!'
    
# №2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, yadisk_file_path, file):
        href = self.get_upload_link(yadisk_file_path).get("href", "")
        response = requests.put(url=href, data=open(file, 'r'))

        if response.status_code == 201:
            print("File uploded!")
        return response.status_code

    def get_upload_link(self, yadisk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": yadisk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    
print(get_intelligence_hero())


token =''
yaUploader = YaUploader(token)
data = yaUploader.upload('test.txt', os.path.join(os.getcwd(), 'upload', 'test.txt'))
print(data)

#№3
fromdate = int((dt.datetime.now() - dt.timedelta(days=2)).timestamp())
todate = int(dt.datetime.now().timestamp())

def get_stackoverflow_questions(dt_start, dt_end):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': fromdate, 'todate': todate, 'tags': 'Python', 'site': 'stackoverflow'}
    response = requests.get(url=url, params=params)

    if response.status_code == 200:
       for item in response.json().get('items'):        
           print(item['title'])
    else:
        print(f'error request! {response.status_code}')

get_stackoverflow_questions(fromdate, todate)
