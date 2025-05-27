# Multi-Site Job Aggregator

A Python-based web scraper and Streamlit app to aggregate job listings from multiple job portals like Indeed, RemoteOK, Remotive, and Naukri. This project demonstrates web scraping using Selenium with stealth techniques to reduce detection and presents results in an interactive Streamlit interface.

---

## Features

- Scrapes top job listings based on keyword search from multiple sites.
- Uses Selenium with stealth to avoid anti-bot detection.
- Displays job title, company, location, job type, and URL.
- Aggregates jobs from Indeed, RemoteOK, Remotive, and Naukri (scrapers can be extended).
- Simple and clean Streamlit web interface for job search and display.

---

## Installation

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/link_scraper.git
    cd link_scraper
    ```

2. Create and activate a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate       # Linux/Mac
    venv\Scripts\activate          # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```



---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py

file structure:
**link_scraper/
├── app.py                     # Main Streamlit web app
├── job_scraper.py            # Aggregator function to get jobs from all sites
├── remoteok_scraper.py       # Scraper for RemoteOK (requests-based)
├── remotive_scraper.py       # Scraper for Remotive (API-based)
├── naukri_scraper.py         # Scraper for Naukri (Selenium-based)
├── indeed_scraper.py         # Scraper for Indeed (Selenium-based)
├── utils/
│   ├── stealth_driver.py     # Shared stealth setup (undetected_chromedriver)
├── requirements.txt          # Dependencies list
└── README.md                 # Project description and usage
