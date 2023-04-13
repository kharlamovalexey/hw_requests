import requests
import json
# url = 'https://httpbin.org'
# response =requests.get(url)
# print(response)

with open('all.json') as f:
    all_hero = json.load(f)

list_hero = ['Hulk', 'Captain America', 'Thanos']
hero_intelligence = {}
for hero in all_hero:
    if hero['name'] in list_hero:
        hero_intelligence[hero['name']] = hero['powerstats']['intelligence']
        
print(max(hero_intelligence, key=hero_intelligence.get))
