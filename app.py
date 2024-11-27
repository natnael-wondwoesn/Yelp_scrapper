import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO

def details(address):
    l = {}
    data = []
    base_url = f'https://api.scrapingdog.com/scrape?dynamic=false&api_key=6746c4f6dfbccc0cb181718c&url={address}'
    r = requests.get(base_url).text

    soup = BeautifulSoup(r, 'html.parser')

    try:
        l["Business"] = soup.find("h1", {"class": "y-css-olzveb"}).text
    except:
        l["Business"] = None
    try:
        l["Phone"] = soup.find_all("div", {"class": "y-css-13akgjv"})[1].text.replace("Phone number", "")
        if l["Phone"][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            l["Phone"] = soup.find_all("div", {"class": "y-css-13akgjv"})[0].text.replace("Phone number", "")
    except:
        l["Phone"] = None
    try:
        l["stars"] = soup.find("div", {"class": "y-css-f0t6x4"}).get('aria-label')
    except:
        l["stars"] = None
    try:
        l["Address"] = soup.find("p", {"class": "y-css-jbomhy"}).text
    except:
        l["Address"] = None
    try:
        l["Number of Reviews"] = soup.find("a", {"class": "y-css-1ijjqcc"}).text
    except:
        l["Number of Reviews"] = 0
    try:
        l["Hours of Operation"] = soup.find("div", {"class": "y-css-4dn0rh"}).text.replace("Closed", "").replace("Open", "")
    except:
        l["Hours of Operation"] = None
    try:
        l["Amenities"] = soup.find_all('div', {"class": 'arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG y-css-mhg9c5'})[0].text
    except:
        l["Amenities"] = None

    if l["Number of Reviews"] != 0:
        l["Number of Reviews"] = l["Number of Reviews"].replace("(", "").replace(")", "")

    data.append(l)
    return data

# Streamlit UI
st.title("Business Details Scraper")

urls_input = st.text_area(
    "Enter URLs (one per line):",
    placeholder="https://example1.com\nhttps://example2.com\nhttps://example3.com"
)

if st.button("Scrape"):
    queue = [url.strip() for url in urls_input.split('\n') if url.strip()]
    all_results = []

    for lo in queue:
        result = details(lo)
        all_results.extend(result)

    for result in all_results:
        st.markdown("---")
        st.markdown(f"**Business:** {result['Business']}")
        st.markdown(f"**Phone:** {result['Phone']}")
        st.markdown(f"**Stars:** {result['stars']}")
        st.markdown(f"**Address:** {result['Address']}")
        st.markdown(f"**Number of Reviews:** {result['Number of Reviews']}")
        st.markdown(f"**Hours of Operation:** {result['Hours of Operation']}")
        st.markdown(f"**Amenities:** {result['Amenities']}")


    df = pd.DataFrame(all_results)
    csv = StringIO()
    df.to_csv(csv, index=False)


    st.download_button(
        label="Download Data as CSV",
        data=csv.getvalue(),
        file_name="scraped_business_data.csv",
        mime="text/csv"
    )
