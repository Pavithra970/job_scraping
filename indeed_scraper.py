from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

def fetch_indeed_jobs(keyword):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    search_url = f"https://www.indeed.com/jobs?q={keyword.replace(' ', '+')}&l="
    driver.get(search_url)
    time.sleep(5)

    jobs = []
    job_cards = driver.find_elements(By.CSS_SELECTOR, "a.tapItem")

    for card in job_cards[:10]:
        try:
            title = card.find_element(By.CSS_SELECTOR, "h2.jobTitle > span").text.strip()
        except:
            title = None

        try:
            company = card.find_element(By.CSS_SELECTOR, "span.companyName").text.strip()
        except:
            company = None

        try:
            location = card.find_element(By.CSS_SELECTOR, "div.companyLocation").text.strip()
        except:
            location = None

        try:
            job_url = card.get_attribute("href")
        except:
            job_url = None

        if title and company and location and job_url:
            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "type": "Full Time",
                "url": job_url,
                "source": "Indeed"
            })

    driver.quit()
    return jobs
