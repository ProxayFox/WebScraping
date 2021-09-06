import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"

# Open Connection Grab Page
uClient = uReq(my_url)
page_html = uClient.read()
# Close Connection
uClient.close()
# HTML Pass
page_soup = soup(page_html, "html.parser")

# Grab Each item
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "procuct.csv"
f = open(filename, "w")

headers = "brand, procuct_name, shipping\n"

f.write(headers)

for container in containers:
  brand = container.div.div.a.img["title"]

  title_container = container.findAll("a",{"class":"item-title"})
  procuct_name = title_container[0].text

  shipping_container = container.findAll("li", {"class":"price-ship"})
  shipping = shipping_container[0].text.strip()

  # print("brand" + brand)
  # print("procuct_name" + procuct_name)
  # print("shipping" + shipping)

  f.write(brand.replace(",", "|") + "," + procuct_name.replace(",", "|") + "," + shipping.replace(",", "|") + "\n")
f.close()