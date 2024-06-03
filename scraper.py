import requests
from bs4 import BeautifulSoup
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

headers_list = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"},
    # Add more headers if needed
]

def get_price_using_requests(url):
    headers = random.choice(headers_list)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        whole_price = soup.find('span', {'class': 'a-price-whole'})
        fraction_price = soup.find('span', {'class': 'a-price-fraction'})

        if whole_price and fraction_price:
            price = f"{whole_price.text.strip()}.{fraction_price.text.strip()}"
            return price
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def get_price_using_selenium(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        time.sleep(2)  # Adjust sleep time as necessary
        whole_price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
        fraction_price = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
        
        if whole_price and fraction_price:
            price = f"{whole_price.text.strip()}.{fraction_price.text.strip()}"
            return price
        else:
            return None
    except Exception as e:
        return None
    finally:
        driver.quit()

def scrape_prices(urls):
    prices = {}
    for url in urls:
        price = get_price_using_requests(url)
        if not price:
            price = get_price_using_selenium(url)
        if not price:
            price = "Price not found"
        prices[url] = price
        time.sleep(random.uniform(1, 3))  # Add delay between requests
    return prices
