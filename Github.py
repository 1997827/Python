

from github import Github

g = Github("1997827","github@1997")

user = g.get_user('1997827')
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.get_commit(sha=sha).create_status(
    state="pending",
    target_url="https://github.com/1997827/Python",
    description="FooCI is building",
    context="ci/FooCI"
)
repo.create_file('/filename', 'commitmessage', 'content')