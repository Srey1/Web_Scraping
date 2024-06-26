from bs4 import BeautifulSoup as my_soup 
from urllib.request import urlopen as uReq

link = "https://www.newegg.com/p/pl?d=graphic+cards"
# Oppening a connection and grabbing the html. Then closing the connection. Note the html we have is unparsed. 
connection = uReq(link)
html = connection.read()
connection.close()

# Parse the html using Beautiful soup
parsed_html = my_soup(html, "html.parser")
containers = parsed_html.findAll("div", {"class" : "item-container"})

# Create a file
#filename = "cards.csv"
#f = open(filename, "w")
#headers = "Title, Price, Shipping\n"
#f.write(headers)

counter = 0
for container in containers:
    title = container.findAll("a", {"class" : "item-title"})[0].text
    if (container.findAll("div",{"class" : "item-action"})[0].strong != None):
        price = container.findAll("div",{"class" : "item-action"})[0].strong.text
        dec_price = container.findAll("div",{"class" : "item-action"})[0].sup.text
    else:
        price = "Unkown"
        dec_price = "Unkown"
    shipping = container.findAll("li",{"class" : "price-ship"})[0].text
    if container == containers[-1]:
        print("Title: " + title)
        print("Price: " + price + dec_price)
        print("Shipping: " + shipping)
    #f.write(title.replace(",", "|") + "," + price + dec_price + "," + shipping.replace(",", " |") + "\n")

print(counter)

