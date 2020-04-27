from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)
    

def scrape_info():
    browser = init_browser()





    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather" : mars_weather,
        "table_code": table_code
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return costa_data
