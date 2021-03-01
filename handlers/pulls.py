import requests

count_pages = {'per_page': '100'}
credentials = ('login', 'password')


def get_pulls(state):
    if state == "open" or state == "closed":
        url = f"https://api.github.com/repos/alenaPy/devops_lab/pulls?state={state}"
        response = requests.get(url, params=count_pages, auth=credentials)
        pull = response.json()
    elif state == "needs work" or state == "accepted":
        url = 'https://api.github.com/search/issues?q=is:pr%20'\
              f'label:\"{state}\"%20repo:alenaPy/devops_lab'
        response = requests.get(url, params=count_pages, auth=credentials)
        pull = response.json()['items']
    else:
        url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all'
        response = requests.get(url, params=count_pages, auth=credentials)
        pull = response.json()

    output = []
    for item in pull:
        output.append({
            'num': item['number'],
            'title': item['title'],
            'link': item['html_url']})
    return output
