import requests
import csv

url = 'https://www.eyefootball.com/rss/news.xml'
response = requests.get(url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(url, headers=headers)


club_name = input('Enter the club name: ')
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'xml')
print(soup.prettify())
a_tag = soup.find_all('a', attrs={'alt': f'{club_name} news'})
print(a_tag)

for tag in a_tag:
    club_url = tag.get('href')

club_response = requests.get(club_url)
club_soup = BeautifulSoup(club_response.text, 'html.parser')
target_style = "font-size:14px; padding-bottom:8px"
li_elements = club_soup.find_all('li', attrs={'style': target_style}) 
article_hrefs = []

if li_elements:
    print(f"\nExtracting news links for {club_name}:")
    for li_tag in li_elements:
        a_tag_in_li = li_tag.find('a') 
        if a_tag_in_li:
            href = a_tag_in_li.get('href')
            if href:
                if not href.startswith('http'):
                    base_url_for_articles = 'https://www.eyefootball.com'
                    href = base_url_for_articles + href
                article_hrefs.append(href)
                print(href) 
else:
    print(f"No news articles found with the specified style for {club_name}.")

all_scraped_data = []

for href in article_hrefs:
    response = requests.get(href, headers=headers) 
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h1', attrs={'itemprop':'name'})
    content_paragraphs = soup.find_all('p', attrs={'style':'font-size:16px; padding-top:10px'})

    current_title = ""
    if titles:
       
        current_title = titles[0].get_text(strip=True)

    current_content = ""
    if content_paragraphs:
        
        current_content = "\n".join([p_tag.get_text(strip=True) for p_tag in content_paragraphs])

   
    all_scraped_data.append({
        'URL': href,
        'Title': current_title,
        'Content': current_content
    })

    print(f"\n--- From URL: {href} ---")
   
    if current_title:
        print("Title:")
        print(f"- {current_title}")
    else:
        print("No titles found for this article.")


    if current_content:
        print("Content:")
        print(current_content)
    else:
        print("No content found for this article.")

 

csv_file_name = f"{club_name.replace(' ', '_')}_news.csv"
try:
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'Title', 'Content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader() 
        writer.writerows(all_scraped_data) 
    print(f"\nSuccessfully saved scraped data to {csv_file_name}")
except IOError as e:
    print(f"\nError saving data to CSV file: {e}")