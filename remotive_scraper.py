import requests

def fetch_remotive_jobs(keyword):
    url = f"https://remotive.io/api/remote-jobs?search={keyword}"
    response = requests.get(url, timeout=10)
    jobs = []
    if response.status_code == 200:
        data = response.json()["jobs"]
        for job in data:
            jobs.append({
                "title": job["title"],
                "company": job["company_name"],
                "location": job["candidate_required_location"],
                "type": job["job_type"],
                "url": job["url"],
                "source": "Remotive"
            })
    return jobs
