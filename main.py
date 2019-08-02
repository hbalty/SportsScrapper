# coding: utf8

from bs4 import BeautifulSoup
import requests
from source import Source

goalFr = Source('http://www.football.fr','fr', { 'isMain': 'true', 'title_selector' : 'link',
 'has_title_attr' : True,
 'link_selector' : 'link',
 'picture_selector': 'img-lazy', 
 'excerpt_selector' : 'excerpt'})


print goalFr.url

maxiFootFr = Source('http://www.maxifoot.fr','fr', { 'isMain': 'true', 'title_selector' : 'titre2',
 'has_title_attr' : False,
 'link_selector' : 'titre2',
 'picture_selector': 'img2', 
 'excerpt_selector' : 'excerpt'})


goalEn = Source('https://www.goal.com','en', { 'isMain': 'true'})
goalAr = Source('https://www.goal.com','ar', { 'isMain': 'true'})

page = requests.get(goalFr.url)
soup = BeautifulSoup(page.text, 'html.parser')

links = soup.find_all('a')
imgs = soup.find_all('img')
#print links



##
# Gets all links with the right selector
##
def get_links_list(links, selector):
    empty_list = []
    for item in links:
        if item.get('class') is not None:
            if  item['class'][0] == selector:
                empty_list.append(item)
    return empty_list


def get_imgs_list(imgs, selector):
    empty_list = []
    for img in imgs:
        print img
        if img.get('class') is not None:
            if img['class'][0] == selector:
                empty_list.append(img)
    return empty_list

a = get_links_list(links, goalFr.options['link_selector'])
b = get_links_list(imgs, goalFr.options['picture_selector'])
for i in range(0,13):
    print a[i].get('href') 
    print b[i].get('data-original')
    
    






'''
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

print finalList 


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
'''




