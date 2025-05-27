from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_naukri_jobs(keyword):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    search_url = f"https://www.naukri.com/{keyword}-jobs"
    driver.get(search_url)
    time.sleep(5)

    jobs = []
    listings = driver.find_elements(By.CSS_SELECTOR, "article.jobTuple")
    for job in listings[:10]:
        try:
            title = job.find_element(By.CSS_SELECTOR, "a.title").text
            company = job.find_element(By.CSS_SELECTOR, "a.subTitle").text
            location = job.find_element(By.CSS_SELECTOR, "li.location span.locWdth").text
            url = job.find_element(By.CSS_SELECTOR, "a.title").get_attribute("href")

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "type": "Full Time",
                "url": url,
                "source": "Naukri"
            })
        except:
            continue
    driver.quit()
    return jobs
