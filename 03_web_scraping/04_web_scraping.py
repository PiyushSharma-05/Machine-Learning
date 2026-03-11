import requests
from bs4 import BeautifulSoup

# url = "https://www.scrapethissite.com/pages/simple/"
# response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.content)
# print(response.headers)

# with open("scraped_data/data1.html", "w", encoding="utf-8") as f:
#     f.write(response.text)

# try:
#     res = requests.get(url, timeout=5)
#     res.raise_for_status() 
# except requests.exceptions.RequestException as e:
#     print("Error: ", e)

with open("scraped_data/data1.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "lxml")    
# print(soup)
# methods
# print(soup("h1")) #first h1
# print(soup.find("h1")) #first h1
# print(soup.h1) #first h1

all_h3 = soup.find_all("h3")
# print(all_h3)
# print(type(all_h3))
for h3 in all_h3:
    # print(h3.get_text)
    # print(h3.get_text(strip=True)) #data under h3
    # print(h3.find_parent("div"))
    # print(h3.find_parent("div")["class"]) #all classes
    # print(h3.find_next("div"))
    # print(h3.find_next("div").select("span.country-population")[0].get_text(strip=True)) #all country population
    # print(h3.find_next("div").select_one("span.country-population").get_text(strip=True))  #all country population
    print(h3.attrs)

    all_countries = []

    