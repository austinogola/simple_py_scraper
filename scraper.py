from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

def web_scrape(url,xpath):
    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver=webdriver.Chrome(chrome_options=options,executable_path=ChromeDriverManager().install())
    driver.get(url)

    # soup=BeautifulSoup(driver.page_source,"html_parser")

    # return soup

    titles=driver.find_elements(By.TAG_NAME,xpath)

    tt=[item.text for item in titles]

    return tt


# nedd=web_scrape('https://www.scrapethissite.com/pages/simple/','h3')