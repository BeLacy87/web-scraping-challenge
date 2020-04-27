import pandas as pd
import pymongo
import requests
import GetOldTweets3 as got

from bs4 import BeautifulSoup
from splinter import Browser


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)
    

def scrape_info():
    # #pulls headline and news
    # browser = init_browser()
    # url='https://mars.nasa.gov/news/'
    # browser.visit(url)
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # article = soup.find('li', class_='slide')
    # news_title=article.find('h3').text
    # news_p=article.find('div',class_='article_teaser_body').text
    # print(news_title,news_p)
    # browser.quit()

    # #pull featuered image ***need to make fluid***    
    # browser=init_browser()
    # url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # browser.visit(url)
    # #find button and click it
    # xpath = '//a[@class="button fancybox"]'
    # browser.find_by_xpath(xpath).click()
    # xpath = '//a[@class="fancybox-expand"]'
    # browser.find_by_xpath(xpath).click()
    # #find url for full size image from previous click
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # featured_image_url ='https://www.jpl.nasa.gov' + soup.find("img", class_="fancybox-image")["src"]
    # browser.quit()
    
    # #get weather tweet
    # username = '@MarsWxReport'
    # count = 1
    # # Creation of query object
    # tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
    #                                     .setMaxTweets(count)
    # # Creation of list that contains all tweets
    # tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # # Creating list of chosen tweet data
    # user_tweets = [[tweet.text] for tweet in tweets]
    # mars_weather=user_tweets[0][0]
    
    # #pull mars facts table
    # url='https://space-facts.com/mars/'
    # results = pd.read_html(url)
    # table=results[0]
    # table_code=table.to_html()

    #Mars hemispheres
    browser=init_browser()
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)    
    xpath = '//img[@class="thumb"]'
    browser.find_by_xpath(xpath).click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url_1 ='https://astrogeology.usgs.gov/' + soup.find("img", class_="wide-image")["src"]
    browser.quit()

    # Store data in a dictionary
    mars_data = {
        # "news_title": news_title,
        # "news_p": news_p,
        # "featured_image_url": featured_image_url,
        # "mars_weather" : mars_weather,
        # "table_code": table_code,
        "hemisphere_image_urls" :[
            {"title": "Cerberus Hemisphere", "img_url": img_url_1}]
            # {"title": "Schiaparelli Hemisphere", "img_url": img_url_2},
            # {"title": "Syrtis Major Hemisphere", "img_url": img_url_3},
            # {"title": "Valles Marineris Hemisphere", "img_url": img_url_4}]
    }

    # Close the browser after scraping
   

    # Return results
    return mars_data
