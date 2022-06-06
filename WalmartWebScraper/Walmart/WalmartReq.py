import requests
from bs4 import BeautifulSoup as soup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

url = "https://www.walmart.com/browse/summer-produce/c2hlbGZfaWQ6NTU5MDY2NQieie?page=1&affinityOverride=default"

url_list = []

for i in range(1, 2):
    url_list.append(url.replace("page=1", "page=" + str(i)))


#Create Arrays for Tags

item_names = []
price_list = []
priceper_list = []

for url in url_list:
  result = requests.get(url)
  bsobj = soup(result.content,'lxml')
  
  product_name = bsobj.findAll('div',{'class':'w_At'})
  product_price = bsobj.findAll('div',{'class':'b black f5 mr1 mr2-xl lh-copy f4-l'})
  product_priceper = bsobj.findAll('div',{'class':'f7 f6-l gray mr1'})
for names,price,priceper in zip(product_name,product_price, product_priceper):
    item_names.append(names.a.span.text.strip())
    price_list.append(price.text)
    priceper_list.append(priceper.text)

# creating a dataframe 
import pandas as pd
df = pd.DataFrame({'Product_Name':item_names, 'Price':price_list, 'Price_Per':product_priceper}, columns=['Product_Name', 'Price', 'PricePer'])
df.to_csv('Walmart Test' + '.csv')