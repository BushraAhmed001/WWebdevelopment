from bs4 import BeautifulSoup
import requests
import pandas as pd
my_file = open("Day_1/index.html", "r")

souped_html = BeautifulSoup(my_file, "lxml")

print(souped_html)

# html_text = requests.get("http://127.0.0.1:5500/Day_1/index.html")

# souped_html = BeautifulSoup(html_text.text, "lxml")

categories = souped_html.find_all("h2")

choice_no_1 = souped_html.find_all("span", class_= "choice-no-1") 
choice_no_2 = souped_html.find_all("span",class_="choice-no-2") 
choice_no_3 = souped_html.find_all("span",class_="choice-no-3") 
print(choice_no_1)

df = pd.DataFrame({
    "Categories": [category.text for category in categories],
    "Choice_no_1": [choice.text for choice in choice_no_1],
    "Choice_no_2": [choice.text for choice in choice_no_2],
    "Choice_no_3": [choice.text for choice in choice_no_3] 
})
df=df.set_index("Categories")

df.to_excel("DataScraper.xlsx")
print(df)