import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_website(url, max_retries=5, delay=5):
    """
    Scrapes the website and returns the HTML content.
    
    Args:
        url (str): URL of the website to scrape.
        max_retries (int): Maximum number of retries.
        delay (int): Delay between retries in seconds.
    
    Returns:
        str: HTML content of the website.
    """
    headers = {'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    for i in range(max_retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch the webpage. Retrying ({i+1}/{max_retries})...")
            time.sleep(delay)
    print("Failed to fetch the webpage after maximum retries.")
    return None

def extract_product_info(html):
    """
    Extracts product information from the HTML content.
    
    Args:
        html (str): HTML content of the website.
    
    Returns:
        list: List of dictionaries containing product information.
    """
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    # Extract product names, prices, and ratings
    for product in soup.find_all('div', class_='sg-col-inner'):
        name_elem = product.find('span', class_='a-size-medium')
        price_elem = product.find('span', class_='a-price')
        rating_elem = product.find('span', class_='a-icon-alt')
        
        name = name_elem.text.strip() if name_elem else 'Not available'
        
        # Check if price_elem exists and contains the nested span
        if price_elem and price_elem.find('span', class_='a-offscreen'):
            price = price_elem.find('span', class_='a-offscreen').text.strip()
        else:
            price = 'Not available'
        
        rating = rating_elem.text.strip() if rating_elem else 'Not available'
        
        products.append({'Name': name, 'Price': price, 'Rating': rating})
    return products

def save_to_csv(products, filename):
    """
    Saves product information to a CSV file.
    
    Args:
        products (list): List of dictionaries containing product information.
        filename (str): Name of the CSV file.
    """
    with open(filename, "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

# URL of the e-commerce website to scrape (Amazon India in this case)
url = 'https://www.amazon.in/s?k=laptops'

# Scrape the website
html = scrape_website(url)

# Extract product information
if html:
    products = extract_product_info(html)
    print(f"Extracted {len(products)} products.")
    
    # Save product information to a CSV file
    filename = 'amazon_products.csv'
    save_to_csv(products, filename)
    print(f"Product information saved to {filename}.")