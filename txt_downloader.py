import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#input the url
f = open("text.txt", "x")
url = input("Enter your book url: ")
parsed_url = urlparse(url)
base_url = parsed_url.scheme + "://" + parsed_url.netloc
web = requests.get(url)                        
soup = BeautifulSoup(web.text, "html.parser") 
title = input("Enter your book title: ")
first_ch = input("Enter your the first chapter of the book: ")
first_ch_line =  input("Enter first name of the first chapter: ")     
first_skip = 0
f.write(title)                            
#search first chapter text and find the tag of it save it to tags_with_the_text[0]
def has_the_text(tag):
    return tag.get_text() == first_ch
tags_with_the_text = soup.find_all(has_the_text)
all_tags_text = soup.find_all(tags_with_the_text[0].name)
#find all chapter in the page and its url
for each_tag in all_tags_text:
    if(abs( len(str(each_tag.get('href'))) - len(str(tags_with_the_text[0].get('href')))) <= 3 ):
        if str(each_tag.get('href'))[:10] == str(tags_with_the_text[0].get('href'))[:10]:
            if first_skip == 0:
                if tags_with_the_text[0].get_text == each_tag.get_text:
                    first_skip += 1
                    web = requests.get(base_url + str(each_tag.get('href')))                       
                    soup2 = BeautifulSoup(web.text, "html.parser")
                    selector = f':-soup-contains-own("{first_ch_line}")'
                    tags_with_the_text2 = soup2.select_one(selector)
                    all_tags_text2 = soup2.find_all(tags_with_the_text2.name)
            else:
                web = requests.get(base_url + str(each_tag.get('href')))                       
                soup2 = BeautifulSoup(web.text, "html.parser")
                all_tags_text2 = soup2.find_all(tags_with_the_text2.name)
            if(first_skip == 1):
                for each_text in all_tags_text2:
                    f.write(each_text.text)
f.close()