from os import system
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode



def get_top_business_names(total,term,location,output_file):
    url = f"https://www.yelp.com/search/snippet?find_desc={term}&find_loc={location}"
    base_url = f"https://api.scrapingdog.com/scrape?dynamic=false&api_key=6746c4f6dfbccc0cb181718c&url={url}"
    params = {
        "find_desc":term,
        "find_loc": location,
        "request_origin":"user"
        }
    params=urlencode(params)
    page = 0

    pages=[]
    counter = 0
    while page <= total:
        current = requests.get(base_url)
        print(current.status_code)
        pages.append(current)

        print('Page: ',page+1,' scanned')
        page+=1
        
        counter+=1
        counter%var

    count = 0

    while count <= total:
        plain_text = pages[count].text     
        soup = BeautifulSoup(plain_text,'html.parser')
      
        it=0      
        for link in soup.findAll('a',{'class':'y-css-1ijjqcc'}):
            title = link.string
            href = 'https://www.yelp.com' + link.get('href')
            if it < 3:  ##first 2 are always adds
                it+=1
                continue
            print('title: ',title)
        page+=1

        plain_text = pages[count].text
        soup = BeautifulSoup(plain_text,'html.parser')
        names = []

        for link in soup.findAll('a',{'class':'y-css-1ijjqcc'}):
            title = link.string
            dynamic_link = 'https://www.yelp.com' + link.get('href')

            names.append((title,dynamic_link))


        count+=1

    with open(output_file, "w", encoding="utf-8") as f:
        for name in names:
            f.write(f"{name}\n")
    
    print(f"Business names saved to {output_file}")





if __name__ =='__main__':
    total = int(input("Enter Total Number of Pages: "))
    term = input("Enter search term (e.g., Pizza): ")
    location = input("Enter location (e.g., New York): ")
    output_file = input("Enter output filename (default: business_names.txt): ") or "business_names.txt"

    get_top_business_names(total,term,location,output_file)

    


