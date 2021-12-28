import os
import string
from pprint import pprint

import requests
from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020'
prefix = 'https://www.nature.com'
suffix = '&page='

stop_page = int(input())
cat_page = str(input())

def save_articles_from_url(input_url, category, page):
    mydir = 'Page_' + str(page)
    os.mkdir(mydir)
    file_extension = 'txt'
    r = requests.get(input_url)
    if r.status_code != 200:
        print("The URL returned", r.status_code)
        exit()
    page_content = r.content
    soup = BeautifulSoup(page_content, 'html.parser')
    myvar= ()
    the_links = soup.find_all('article')
    saved_articles = []
    for article in the_links:
        to_save = ''
        type_span = article.select_one('span[data-test]')
        type = type_span.text.replace('\n', '')
        if type == str(category):
            #print('found news')
            a_content_raw = ''
            a_content_raw = article.select_one('a[data-track-action="view article"]')
            target_url = prefix + a_content_raw['href']
            #print(target_url)
            target_raw = requests.get(target_url)
            to_soup = BeautifulSoup(target_raw.content, 'html.parser')
            #pees = to_soup.findAll('div', {"class": "c-article-body u-clearfix"})
            divs = to_soup.find_all('div')
            for div in divs:
                if "body" in str(div.get("class")):
                    ps = div.find_all('p')
                    x=0
                    for p in ps:
                        #print(p.get('class'))
                        #to_save += p.text + '\n'
                        pass
            #tag.name == "div" and ("article" in tag.get("class", [""])[0] and "body" in tag.get("class", [""])[0])
                    to_save += div.text
            t_content_raw = article.select_one('h3').text.strip('\n')
            for n in string.punctuation:
                t_content_raw = t_content_raw.replace(n,'')
            title = t_content_raw.replace(" ","_")

            file_name = mydir + '/' + title + "." + file_extension
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(to_save)
            saved_articles.append(file_name)
    print('Saved all articles.')
#print(saved_articles)

for n in range(1,stop_page+1):
    input_url = url + suffix + str(n)
    save_articles_from_url(input_url, cat_page, n)



