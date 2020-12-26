import json

import requests

token = "write_access_token"
user = "github_user"
password = "github_password"
repos_url = 'https://api.github.com/user/repos'

# 1st
# login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(user,token))


# 2nd
# headers = {'Authorization': 'token ' + token}
# login = requests.get('https://api.github.com/user', headers=headers)


# 3rd
repo = 'some_repo_rakesh'
description = 'Created with api raka testing '

payload = {'name': repo, 'description': description, 'auto_init': 'true'}

login = requests.post('https://api.github.com/' + 'user/repos', auth=(user, token), data=json.dumps(payload))

print("res 1 : ", login.json())

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (user, token)

# get the list of repos belonging to me
repos = json.loads(gh_session.get(repos_url).text)

# print the repo names
for repo in repos:
    print(repo['name'])

# r = requests.get('https://api.github.com/user', auth=(user , password))
# print("result : ", r.status_code)
