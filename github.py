import requests

def get_top_github_repos():
    #"""Get the top 10 starred repos on GitHub."""
    api_url = 'https://api.github.com/search/repositories'
    response = requests.get(api_url, params={'q': 'stars:>1'})

    if response.status_code != 200:
        print(f"Status Code: {response.status_code}, Response: {response.json()}")
        raise RuntimeError(f"An error occurred while fetching repos, status code: {response.status_code}")
    
    response_json = response.json()
    return response_json['items']

if __name__ == '__main__':
    repos = get_top_github_repos()
    for repo in repos:
        print(f"{repo['name']}: {repo['stargazers_count']}")
    # colors = {'red': 1, 'green': 2, 'blue': 3}
    # for key, value in colors.items():
    #     print(key, value)