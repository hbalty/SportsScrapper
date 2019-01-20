from bs4 import BeautifulSoup
import requests
from source import Source

goalFr = Source('https://www.goal.com','fr', { 'isMain': 'true'})
goalEn = Source('https://www.goal.com','en', { 'isMain': 'true'})
goalAr = Source('https://www.goal.com','ar', { 'isMain': 'true'})

page = requests.get(goalFr.url+'/'+goalFr.language)
soup = BeautifulSoup(page.text, 'html.parser')

links = soup.find_all('a')

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list



linksList = unique(links)

def filterList(list):
    filtered_list = []
    for link in list:
        if (link.get('data-side') == 'front'):
            filtered_list.append(link)
    return filtered_list

def getImageLink(imageList):
    for img in imageList:
        if (img.get('src') is not None):
            return img.get('src') 

finalList = filterList(linksList)

testLink = finalList[1].get('href'); 
article = requests.get(goalFr.url+testLink)
articleSoup = BeautifulSoup(article.text,'html.parser')

articleTitle = articleSoup.find("div", {"class" : "article-headline"}).text
articleDate = articleSoup.find("span", {"data-dateformat" : "dateShort"}).text
articleImageDiv = articleSoup.find("div", {"class" : "picture article-image"}).find_all('img')
articleImage = getImageLink(articleImageDiv)
print(articleTitle)
print(articleDate)
print(articleImage)





