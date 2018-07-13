import requests
import json

URLs = [
    
    'https://api.github.com/repositories',
    'https://api.github.com/repositories?since=367',
    'https://api.github.com/repositories?since=867',
    'https://api.github.com/repositories?since=1494',
    'https://api.github.com/repositories?since=1954',
    'https://api.github.com/repositories?since=2433',
    'https://api.github.com/repositories?since=2838',
    'https://api.github.com/repositories?since=3314',
    'https://api.github.com/repositories?since=3751',
    'https://api.github.com/repositories?since=4303',
    'https://api.github.com/repositories?since=4756',
    'https://api.github.com/repositories?since=5181',
    'https://api.github.com/repositories?since=5671',
    'https://api.github.com/repositories?since=6186',
    'https://api.github.com/repositories?since=6864',
    'https://api.github.com/repositories?since=7800',
    'https://api.github.com/repositories?since=8800',
    'https://api.github.com/repositories?since=9800',
    'https://api.github.com/repositories?since=10800',
    'https://api.github.com/repositories?since=11800',
    'https://api.github.com/repositories?since=12800',
    'https://api.github.com/repositories?since=13800',
    'https://api.github.com/repositories?since=14800',
    'https://api.github.com/repositories?since=15800',
    'https://api.github.com/repositories?since=16800',
    'https://api.github.com/repositories?since=17800',
    'https://api.github.com/repositories?since=18800',
    'https://api.github.com/repositories?since=19800',
    'https://api.github.com/repositories?since=20800',
    'https://api.github.com/repositories?since=21800',
    'https://api.github.com/repositories?since=22800',
    'https://api.github.com/repositories?since=23800',
    'https://api.github.com/repositories?since=24800',
    'https://api.github.com/repositories?since=25800'
    
]

all_repos = []
for url in URLs:
    all_repos += requests.get(url).json() 

with open('resultnn3.json', 'w' ) as fp:
    json.dump(all_repos, fp, indent=2)
