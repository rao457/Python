from plotly.graph_objs import Bar
from plotly import offline
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print("Status Code: ", r.status_code)
response_dict = r.json()
print(f"Total Repositories: {response_dict['total_count']}")
repo_dicts = response_dict['items']
repositories,stars = [], []
for repo_dict in repo_dicts:
    repositories.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
data = [{
    'type':'bar',
    'x' : repositories,
    'y' : stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
            },
    'opacity': 0.6,
}]
my_layout ={
    'title' : 'Python most famous repositories',
    'xaxis' : {'title': 'Repository'},
    'yaxis' : {'title' : 'Stars'}
}
fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename= 'python_repos.html')
# print(f'Most Starred Repositories: {len(repo_dicts)}')
# repo_dict = repo_dicts[0]
# print(f'\nKeys: {len(repo_dict.keys())}')
# for key in sorted(repo_dict.keys()):
#     print(key)
# print('Selected Information about first repository.')
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Last Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")