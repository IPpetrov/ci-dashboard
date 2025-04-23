from flask import Blueprint, render_template

main = Blueprint('main', __name__)

projects = [
    {
        "name": "Cloud Resume",
        "url": "https://www.ip-petrov.com/",
        "gh_owner": "IPpetrov",
        "gh_repo": "cloud-resume"
    },
    {
        "name": "Jira Helper",
        "url": "https://jira-109573300692.europe-west3.run.app/",
        "gh_owner": "IPpetrov",
        "gh_repo": "jira"
    }
]


@main.route("/")
def index():
    from app.utils import check_status, get_latest_github_action_status

    statuses = [check_status(p["url"]) for p in projects]
    github_statuses = [
        get_latest_github_action_status(p["gh_owner"], p["gh_repo"])
        for p in projects
    ]

    return render_template("index.html", projects=zip(projects, statuses, github_statuses))

