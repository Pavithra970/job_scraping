# utils/stealth_driver.py

import undetected_chromedriver as uc
from fake_useragent import UserAgent

def setup_stealth_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--headless=new")  # Optional: remove to see browser
    user_agent = UserAgent().random
    options.add_argument(f"user-agent={user_agent}")
    driver = uc.Chrome(options=options)
    return driver
