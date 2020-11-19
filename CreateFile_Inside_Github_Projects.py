

from github import Github

g = Github("username","password")

user = g.get_user('username')
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.get_commit(sha=sha).create_status(
    state="pending",
    target_url="https://github.com/username/projectname",
    description="create file",
    context="create"
)
repo.create_file('/filename', 'commitmessage', 'content')
