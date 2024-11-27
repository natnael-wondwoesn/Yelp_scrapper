from bs4 import BeautifulSoup
import requests
import streamlit as st



def details(address):
    l = {}
    data = []
    base_url = f'https://api.scrapingdog.com/scrape?dynamic=false&api_key=6746c4f6dfbccc0cb181718c&url={address}'
    r = requests.get(base_url).text
    print(businessName)
    print(base_url)

    soup = BeautifulSoup(r,'html.parser')

    try:
        l["name"]=soup.find("h1",{"class":"y-css-olzveb"}).text
    except:
        l["name"]=None
    try:
        l["Phone"]=soup.find_all("div",{"class":"y-css-13akgjv"})[1].text.replace("Phone number","")
        if l["Phone"][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            l["Phone"]=soup.find_all("div",{"class":"y-css-13akgjv"})[0].text.replace("Phone number","")
    except:
        l["Phone"]=None
    try:
        l["stars"]=soup.find("div",{"class":"y-css-f0t6x4"}).get('aria-label')
    except:
        l["stars"]=None
    try:
        l["Address"]=soup.find("p",{"class":"y-css-jbomhy"}).text
    except:
        l["Address"]=None
    try:
        l["Number of Reviews"]=soup.find("a",{"class":"y-css-1ijjqcc"}).text
        
    except:
        l["Number of Reviews"]=0
    try:
        l["Hours of Operation"]=soup.find("div",{"class":"y-css-4dn0rh"}).text.replace("Closed","")
        
    except:
        l["Hours of Operation"]=None
    try:
        l["Amenities"]=soup.find_all('span', {"class":'y-css-19xonnr'}).text
        
    except:
        l["Amenities"]=None

    if l["Number of Reviews"]!=0:
            l["Number of Reviews"]=l["Number of Reviews"].replace("(","")
            l["Number of Reviews"]=l["Number of Reviews"].replace(")","")

    data.append(l)
    l={}
    return data

st.title("Business Details Scraper")

tasks = st.number_input("Enter Number of Businesses to be scraped:", min_value=1, step=1, value=1)

queue = []
for i in range(tasks):
    url_address = st.text_input(f"Please Enter Business URL #{i+1}:", key=f"url_{i}")
    if url_address:
        queue.append(url_address)

if st.button("Scrape"):
    all_results = []
    for lo in queue:
        result = details(lo)
        all_results.extend(result)

    st.write("Scraping Results:")
    st.json(all_results)