from bs4 import BeautifulSoup
import requests
import csv

# Scrape
URL = 'https://www.olx.co.id/makassar_g5005674/dijual-rumah-apartemen_c5158'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

html = requests.get(URL, headers=headers)
soup = BeautifulSoup(html.content, 'lxml')

results = soup.find(class_='_3etsg')

job_elems = results.find_all('div', class_='IKo3_')

# Scraping and Writing to csv Process
with open('data20.csv', 'w', newline='') as f:
    fieldnames = ['Title', 'Price', 'Bedroom', 'Bathroom', 'B_Area', 'Location', 'Date']

    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for job_elem in job_elems:
        title = job_elem.find('span', class_='_2tW1I').text
        price = job_elem.find('span', class_='_89yzn').text[3:].replace('.', '')

        # Room and Size
        size = job_elem.find('span', class_='_2TVI3')
        bedroom = size.text[0]
        bathroom = size.text[7]

        # Building Area
        b_area = size.text[-7:].replace(' ', '').replace('-', '').replace('m2', '')
        location = job_elem.find('span', class_='tjgMj').text[:-15]
        date = job_elem.find('span', class_='zLvFQ').text

        dictionary = {}
        dictionary['Title'] = title
        dictionary['Price'] = price
        dictionary['Bedroom'] = bedroom
        dictionary['Bathroom'] = bathroom
        dictionary['B_Area'] = b_area
        dictionary['Location'] = location
        dictionary['Date'] = date

        writer.writerow(dictionary)
        # print("Title    :", title)
        # print("Price    :", price)
        # print("Bedroom  :", bedroom)
        # print("Bathroom :", bathroom)
        # print("B_Area   :", b_area)
        # print("Location :", location)
        # print("Date     :", date)
        # print("\n")
