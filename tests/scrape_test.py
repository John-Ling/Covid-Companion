from bs4 import BeautifulSoup
import requests
# scrape and print India covid data (cases, deaths and recoviers)

def main():
    URL = "https://www.worldometers.info/coronavirus/country/india"
    webpage = requests.get(URL)
    content = BeautifulSoup(webpage.content, "html.parser")
    elements = content.find_all("div", class_="maincounter-number")
    for element in elements:
        value = element.find("span")
        print(value.text.strip())

if __name__ == "__main__":
    main()