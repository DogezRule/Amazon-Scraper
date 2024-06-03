import json
from scraper import scrape_prices

def main():
    product_urls = [

    ]

    prices = scrape_prices(product_urls)

    with open('prices.json', 'w') as f:
        json.dump(prices, f, indent=4)
    print("Prices saved to prices.json")

if __name__ == "__main__":
    main()
import json
from scraper import scrape_prices

def main():
    product_urls = [
        'https://amzn.to/4aL71Nw', 'https://amzn.to/4aG87dm', 
        'https://amzn.to/3w2Zpqw', 'https://amzn.to/3vPqYna', 
        'https://amzn.to/49Mskgn', 'https://amzn.to/3WjQ34r', 'https://amzn.to/3xL0dkg',
        'https://amzn.to/3W2VqEU', 'https://amzn.to/3UppsBn', 'https://amzn.to/49QQgPn',
        'https://amzn.to/4aIgaGw', 'https://amzn.to/3vXpvuZ', 'https://amzn.to/3QaLtkR',
        'https://amzn.to/3TZDate', 'https://amzn.to/3UrSdxA', 'https://amzn.to/3W8cSYx',
        'https://amzn.to/3w8M6of', 'https://amzn.to/3UrahHW', 'https://amzn.to/4aXRB8N',
        'https://amzn.to/49PKsFU', 'https://amzn.to/3QbucrO', 'https://amzn.to/3Qg5c2H',
        'https://amzn.to/3JsoWfL', 'https://amzn.to/4d6qae3', 'https://amzn.to/4aIzRxI',
        'https://amzn.to/3Qcvweh', 'https://amzn.to/3vZFwAC', 'https://amzn.to/3W5n6cc',
        'https://amzn.to/3W8MHBg', 'https://amzn.to/3Qc9oAz', 'https://amzn.to/3xF4pSq',
        'https://amzn.to/4d7fig7', 'https://amzn.to/447L08U', 'https://amzn.to/3Wdn9D3',
        'https://amzn.to/3Q8fhyE', 'https://amzn.to/446MXT4', 'https://amzn.to/3xH2BbH'
    ]

    prices = scrape_prices(product_urls)

    with open('prices.json', 'w') as f:
        json.dump(prices, f, indent=4)
    print("Prices saved to prices.json")

if __name__ == "__main__":
    main()
