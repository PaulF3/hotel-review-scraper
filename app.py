from flask import Flask, render_template, request, send_file, jsonify
from airbnb_scraper import scrape_airbnb_reviews
import os
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        save_path = request.form['save_path']
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        reviews = scrape_airbnb_reviews(url)
        
        # Save reviews to JSON file
        json_file = os.path.join(save_path, 'reviews.json')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(reviews, f, ensure_ascii=False, indent=2)
        
        # Move downloaded images to the selected folder
        for review in reviews:
            if 'local_img_path' in review:
                old_path = review['local_img_path']
                new_path = os.path.join(save_path, os.path.basename(old_path))
                os.rename(old_path, new_path)
                review['local_img_path'] = new_path
        
        return jsonify(reviews)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)