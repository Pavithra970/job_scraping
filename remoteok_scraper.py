import requests

def fetch_remoteok_jobs(keyword):
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    jobs = []
    if response.status_code == 200:
        data = response.json()[1:]  # skip metadata
        for job in data:
            if keyword.lower() in job.get("position", "").lower():
                jobs.append({
                    "title": job.get("position"),
                    "company": job.get("company"),
                    "location": job.get("location", "Remote"),
                    "type": job.get("tags", ["Unknown"])[0],
                    "url": job.get("url"),
                    "source": "RemoteOK"
                })
    return jobs
