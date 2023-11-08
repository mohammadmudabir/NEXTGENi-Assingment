import requests
from bs4 import BeautifulSoup

# Define the product you want to compare
product_to_compare = "iPhone 13 Pro"

# Amazon URL
amazon_url = f"https://www.amazon.com/s?k={product_to_compare.replace(' ', '+')}"

# eBay URL
ebay_url = f"https://www.ebay.com/sch/i.html?_nkw={product_to_compare.replace(' ', '+')}"

# Scrape data from Amazon
amazon_response = requests.get(amazon_url)
amazon_soup = BeautifulSoup(amazon_response.text, 'html.parser')

# Scrape data from eBay
ebay_response = requests.get(ebay_url)
ebay_soup = BeautifulSoup(ebay_response.text, 'html.parser')

# Test if the code is working properly by printing a portion of the scraped data
print("Amazon Title:", amazon_soup.title)
print("eBay Title:", ebay_soup.title)
