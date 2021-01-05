import requests
import base64
from github import Github
from pprint import pprint
import plotly.graph_objects as go 

myname = "andrewmeehan"
password = "ec22fb8a3efed11b7213b1e580cd1ce258b31481"
#username = "esjmb"
username = "torvalds"
g = Github(myname, password)
#url = f"https://api.github.com/users/{username}"
#userdata = requests.get(url).json()
user = g.get_user(username)

dates = []
stars = []
forks = []
names = []
totalCommits = []
lastPush = []
language = []
for repo in user.get_repos():
	dates.append(repo.created_at)
	stars.append(repo.stargazers_count)
	forks.append(repo.forks)
	names.append(repo.full_name)
	totalCommits.append(repo.get_commits().totalCount)
	lastPush.append(repo.pushed_at)
	language.append(repo.language)
		

fig0 = go.Figure(
    data=[go.Bar(y=dates, x=names, text=dates, textposition='outside')],
    layout_title_text="Dates of Repo Creation",
)

fig1 = go.Figure(
    data=[go.Bar(y=stars, x=names, text=stars, textposition='outside')],
    layout_title_text="Stars per repo"
)
fig2 = go.Figure(
    data=[go.Bar(y=lastPush, x=names, text=lastPush, textposition='outside')],
    layout_title_text="Dates of last push"
)
fig3 = go.Figure(
    data=[go.Bar(y=totalCommits, x=names, text=totalCommits, textposition='outside')],
    layout_title_text="No. of total commits"
)

fig4 = go.Figure(
    data=[go.Bar(y=language, x=names, text=language, textposition='outside')],
    layout_title_text="Languages used"
)

fig5 = go.Figure(
    data=[go.Bar(y=forks, x=names, text=forks, textposition='outside')],
    layout_title_text="Forks per repo"
)
fig0.show()
fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()
