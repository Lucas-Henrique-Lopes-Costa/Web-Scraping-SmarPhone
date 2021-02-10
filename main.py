import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.zoom.com.br/celular'

# Opening up connection, grapping the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser") # convertento o arquivo para algo intentivel

containers = page_soup.findAll("div", {"class" : "cardBody"}) # pegando o que eu quero
# print(containers)

# limit = 5
limit = len(containers)

title_container = page_soup.findAll("a", {"class" : "name"}, limit=limit) # pegando o que eu quero
price_container = page_soup.findAll("span", {"class" : "mainValue"})

filename = "SmartPhones.csv"
f = open(filename, "w")

headers = "Model, Price\n"

f.write(headers)

for container in range(0, limit):    
    title = title_container[container].text
    price = price_container[container].text
    
    print("\n" + "Tílulo: " + title)
    print("Preço: " + price)

    f.write(title + "," + price + "\n")
f.close()