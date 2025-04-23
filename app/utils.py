from flask import current_app
import requests

def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        return "Online" if response.status_code == 200 else "Error"
    except Exception:
        return "Unreachable"

from flask import current_app

from flask import current_app

def get_latest_github_action_status(owner, repo, branch="main", count=3):
    cache_key = f"github_status:{owner}:{repo}:{branch}"
    cached = current_app.cache.get(cache_key)
    if cached is not None:
        if isinstance(cached, dict):
            cached["cached"] = True
        return cached

    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs?branch={branch}&per_page={count}"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        result = {"error": "GitHub API rate limit exceeded", "cached": False}
        current_app.cache.set(cache_key, result, timeout=900)
        return result

    if response.status_code != 200:
        result = {"error": f"GitHub API error: {response.status_code}", "cached": False}
        current_app.cache.set(cache_key, result, timeout=300)
        return result

    data = response.json()
    if not data.get("workflow_runs"):
        result = {"runs": [], "cached": False}
        current_app.cache.set(cache_key, result, timeout=300)
        return result

    runs = []
    for run in data["workflow_runs"]:
        commit_message = run.get("head_commit", {}).get("message", "No commit message")
        runs.append({
            "status": run["status"],
            "conclusion": run["conclusion"],
            "updated_at": run["updated_at"],
            "html_url": run["html_url"],
            "commit_message": commit_message
        })

    result = {"runs": runs, "cached": False}
    current_app.cache.set(cache_key, result, timeout=300)
    return result
