from bs4 import BeautifulSoup
import requests

def parsing_beatuifulsoup(url) :
    data = requests.get(url)
    
    html = data.text
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup

def extract_itworld(soup) :

    url = 'http://www.itworld.co.kr/insight'
    data = requests.get(url)

    html = data.text
    soup = BeautifulSoup(html, 'html.parser')

    upload_contents = ''
    new_insights = soup.select('#m_topic_news_list_title')
    contents = soup.select('#m_topic_news_list_summary')

    url_prefix = 'http://www.itworld.co.kr'

    for new_insight, content in zip(new_insights, contents) :
        title = new_insight.select('a')[0].text
        url_suffix = new_insight.select('a')[0].attrs['href']
        url = url_prefix + url_suffix
        text = content.select('p')[0].text

        summary = f"<a href={url}>" + str(new_insight) + "</a>" + "<br/>" + str(text[11:]) + "<br/>\n"
        upload_contents += summary
        
    return upload_contents