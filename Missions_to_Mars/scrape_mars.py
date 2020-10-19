#import dependencies
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser

#define your browser 
def init_browser():
     executable_path = {'executable_path': 'chromedriver.exe'}
     browser = Browser('chrome', **executable_path, headless=False)
     return browser


#Scrape Mars News Data
mars_data = {}
def scrape_news():
    browser = init_browser()
    url_1 = 'https://mars.nasa.gov/news'
    browser.visit(url_1)

    #HTML object
    html = browser.html
    soup = bs(html,'html.parser')

    #look for snippet
    article_title = soup.find('div',class_='list_text').find('div', class_='content_title').find('a').text
    article_paragraph = soup.find('div',class_='list_text').find('div', class_='article_teaser_body').text
    
    #print it
    return article_title
    

#Scrape Mars Images 
def scrape_image():
    browser = init_browser()
    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)
    
    #HTML object
    html = browser.html
    soup = bs(html,'html.parser')
    
    #Image URL Link
    main_url ='https://www.jpl.nasa.gov'
    image_url = soup.find('div', class_='carousel_container').find('article')['style'].replace(');','')[1:-1]

    #Create image url link
    image_url = main_url + image_url
    print(image_url)
    
    #print it
    return featured_img_url

#Scrape Hemisphere Data    
def scrape_hemi():
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
     #HTML object
    browser.visit(url)
    html = browser.html

    #shorten URL
    shorter_url = 'https://astrogeology.usgs.gov'
    
    #pull info
    browser.visit(url_4)
    html = browser.html
    soup = bs(html, 'html.parser')
    main_url = soup.find_all('div', class_='item')
    titles=[]
    hemisphere_img_urls=[]

    #loop through data to create URL
    for x in main_url:
    title = x.find('h3').text
    url = x.find('a')['href']
    hem_img_url = shorter_url + url
    
    #print(hem_img_url)
    browser.visit(hem_img_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    hem_imgage_origin = soup.find('div',class_='downloads')
    hem_imgage_url= hem_imgage_origin.find('a')['href']
    
    print(hemisphere_img_url)
    img_data = dict({'title':title, 'img_url':hemisphere_img_url})
    hemisphere_img_urls.append(img_data)
    

def scrape():
    article1 = scrape_new()
    title = article1[0]
    paragraph = article1[1]
    featured_image = scrape_featured()
    facts = scrape_facts()
    hemispheres = scrape_hemi()

    compressed_scrape = {'news_title':title,
                        'news_paragraph':paragraph,
                        'featured_img':featured_image,
                        'facts':facts,
                        'hemispheres':hemispheres}
    return compressed_scrape