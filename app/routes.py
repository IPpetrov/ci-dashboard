from flask import Blueprint, render_template
from .utils import check_status

main = Blueprint('main', __name__)

# Define your projects here
projects = [
    {"name": "Cloud Resume", "url": "https://www.ip-petrov.com/"},
    {"name": "Jira Helper", "url": "https://jira-109573300692.europe-west3.run.app/"}
]

@main.route("/")
def index():
    statuses = [check_status(p["url"]) for p in projects]
    return render_template("index.html", projects=zip(projects, statuses))
