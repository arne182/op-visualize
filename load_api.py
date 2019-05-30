import requests

def get_events(YOUR_API_TOKEN=""):
    headers = {"Authorization": "Bearer " + YOUR_API_TOKEN}
    r = requests.get("https://sentry.io/api/0/projects/arne182/python/events/", headers=headers)
    return r.json()