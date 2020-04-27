import pandas as pd
import pymongo
import requests

from bs4 import BeautifulSoup
from splinter import Browser


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)
    

def scrape_info():
    #pulls headline and news
    browser = init_browser()
    url='https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find('li', class_='slide')
    news_title=article.find('h3').text
    news_p=article.find('div',class_='article_teaser_body').text
    print(news_title,news_p)
    browser.quit()



    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        # "featured_image_url": featured_image_url,
        # "mars_weather" : mars_weather,
        # "table_code": table_code
    }

    # Close the browser after scraping
   

    # Return results
    return mars_data
