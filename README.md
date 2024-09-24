# Hotel Review Scraper

This project scrapes top 5-star reviews from Airbnb listing pages and provides a web interface for easy use.

## Setup

1. Ensure you have Python 3.7+ installed.
2. Clone this repository:
   ```
   git clone https://github.com/PaulF3/hotel-review-scraper.git
   cd hotel-review-scraper
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```
2. Open a web browser and go to `http://localhost:5000`
3. Enter the Airbnb listing URL and select a folder to save the results
4. Click "Scrape Reviews" to start the process
5. The scraped reviews will be displayed on the page and saved to the selected folder

## Note

Web scraping may be against Airbnb's terms of service. Use this script responsibly and ensure you have permission to scrape the website. Consider using official APIs if available.