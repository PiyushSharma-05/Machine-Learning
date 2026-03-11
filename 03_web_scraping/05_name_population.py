from bs4 import BeautifulSoup
import pandas as pd

with open("scraped_data/data1.html") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "lxml")

# print(soup.get_text())
# print(soup.find_all("h3"))
all_ccountries = []
all_h3 = soup.find_all("h3")
for h3 in all_h3:
  name =  h3.get_text(strip=True)
  population = h3.find_next("div").select("span.country-population")[0].get_text(strip=True)

  all_ccountries.append([name, population])

# print(all_ccountries, end="\n")
print("[", end="")
for info in all_ccountries:
   print(f"{info},")
print("]")

df = pd.DataFrame(all_ccountries, columns=["name", "population"])
print(df)

df.to_csv("cleaned_data/data_collection.csv", index=False)