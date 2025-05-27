import pandas as pd
from remoteok_scraper import fetch_remoteok_jobs
from remotive_scraper import fetch_remotive_jobs
from naukri_scraper import fetch_naukri_jobs
from indeed_scraper import fetch_indeed_jobs

def get_all_jobs(keyword):
    jobs = []
    try:
        jobs += fetch_indeed_jobs(keyword)
    except Exception as e:
        print("[Indeed Error]", e)
    try:
        jobs += fetch_remoteok_jobs(keyword)
    except Exception as e:
        print("[RemoteOK Error]", e)
    try:
        jobs += fetch_remotive_jobs(keyword)
    except Exception as e:
        print("[Remotive Error]", e)
    try:
        jobs += fetch_naukri_jobs(keyword)
    except Exception as e:
        print("[Naukri Error]", e)
    
    return pd.DataFrame(jobs)
