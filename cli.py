import argparse
from airbnb_scraper import scrape_airbnb_reviews
import json

def main():
    parser = argparse.ArgumentParser(description="Scrape Airbnb reviews")
    parser.add_argument("url", help="URL of the Airbnb listing reviews page")
    parser.add_argument("--output", "-o", help="Output JSON file name", default="reviews.json")
    args = parser.parse_args()

    print(f"Scraping reviews from: {args.url}")
    reviews = scrape_airbnb_reviews(args.url)

    print(f"\nFound {len(reviews)} top 5-star reviews:")
    for i, review in enumerate(reviews, 1):
        print(f"\nReview {i}:")
        print(f"Name: {review['name']}")
        print(f"Date: {review['date']}")
        print(f"Image: {review.get('local_img_path', 'No image')}")
        print(f"Review: {review['text'][:100]}...")  # Print first 100 characters
        print("Rating: 5 stars")

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    
    print(f"\nReviews saved to {args.output}")

if __name__ == "__main__":
    main()