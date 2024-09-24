import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import re

def scrape_airbnb_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    reviews = []
    review_elements = soup.find_all('div', class_='r1are2x1 dir dir-ltr')

    for element in review_elements:
        name = element.find('h3', class_='t1qo31eb dir dir-ltr').text.strip()
        date_element = element.find('li', class_='l1h6eamc dir dir-ltr')
        date = date_element.text.strip() if date_element else 'Unknown'
        
        img_element = element.find('img', class_='br5cckx dir dir-ltr')
        img_url = img_element['src'] if img_element else None
        
        text = element.find('span', class_='ll4r2nl dir dir-ltr').text.strip()
        
        rating_element = element.find('span', class_='t1uylsth dir dir-ltr')
        rating = len(rating_element.find_all('span', {'aria-hidden': 'true'})) if rating_element else 0

        if rating == 5:
            reviews.append({
                'name': name,
                'date': date,
                'img_url': img_url,
                'text': text,
                'rating': rating
            })

    reviews.sort(key=lambda x: len(x['text']), reverse=True)
    top_reviews = reviews[:10]

    if not os.path.exists('reviewer_images'):
        os.makedirs('reviewer_images')

    for i, review in enumerate(top_reviews):
        if review['img_url']:
            img_response = requests.get(review['img_url'])
            img_name = f"reviewer_image_{i+1}.jpg"
            with open(os.path.join('reviewer_images', img_name), 'wb') as f:
                f.write(img_response.content)
            review['local_img_path'] = os.path.join('reviewer_images', img_name)

    return top_reviews