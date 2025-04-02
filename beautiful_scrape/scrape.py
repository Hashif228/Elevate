import requests
from bs4 import BeautifulSoup
import csv

def scrape_mobiles(mobile_url):
    mobile_response = requests.get(mobile_url, headers={'User-Agent': 'Mozilla/5.0'})
    if mobile_response.status_code != 200:
        print("Wepage is not getting....")
        return []
    
    mobile_soup = BeautifulSoup(mobile_response.text, 'html.parser')
    mobiles = []
    # d=mobile_soup
    # print(d.prettify())
    for item in mobile_soup.select('.yKfJKb'): 
        if item.select_one('.KzDlHZ'):
            name = item.select_one('.KzDlHZ').text
        else:
            'N/A'
        if item.select_one('.Nx9bqj'):
            offer_price = item.select_one('.Nx9bqj').text
        else: 
            'N/A'
        if item.select_one('.yRaY8j '):
             price= item.select_one('.yRaY8j ').text  
        else:
            'N/A'
        mobiles.append([name, price,offer_price])
    return mobiles



def scrape_watches(watches_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    watches_response = requests.get(watches_url, headers=headers)
    if watches_response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []
    
    watches_soup = BeautifulSoup(watches_response.text, 'html.parser')
    watches = []

    for item in watches_soup.select('.hCKiGj'): 
        if item.select_one('.WKTcLC'):
            name = item.select_one('.WKTcLC').text.strip()
        else:
            'N/A'
        if item.select_one('.Nx9bqj'):
            Offer_price = item.select_one('.Nx9bqj').text.strip() 
        else: 
            'N/A'
        if item.select_one('.yRaY8j'):
            price = item.select_one('.yRaY8j').text.strip() 
        else: 
            'N/A'


        watches.append([name, price,Offer_price])
        
    return watches
    


def save_to_csv_mobiles(mobiles, filename="details/mobiles.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
        writer.writerow(["Product Name", "Price","Offer price"])
        writer.writerows(mobiles)

def save_to_csv_watches(watches, filename="details/watches.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
        writer.writerow(["Product Name", "Price","Offer price"])
        writer.writerows(watches)


def main():
    mobile_url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"  # Replace with actual mobile_url
    mobiles = scrape_mobiles(mobile_url)
    watches_url="https://www.flipkart.com/search?q=watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show="
    watches=scrape_watches(watches_url)
    if mobiles:
        save_to_csv_mobiles(mobiles)
        
        print(f"Data saved to mobiles.csv successfully.")
    else:
        print("No mobiles found.")



    if watches:
        save_to_csv_watches(watches)
        
        print(f"Data saved to watches.csv successfully.")
    else:
        print("No watches found.")

main()
