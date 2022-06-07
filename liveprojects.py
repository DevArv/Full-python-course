import requests

Username = "DevArv"
response = requests.get("https://api.github.com/orgs/DevArv/repos")
my_projects = response.json()
print(my_projects)

for project in my_projects:
    print(f"Project name: {project['name']} Project url: {project['repos_url']}")