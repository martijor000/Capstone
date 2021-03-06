import requests
import pandas as pd
import time
from bs4 import BeautifulSoup as soup

headers = {
  'Cookie': 'ACID=b7468c25-85bc-49cd-95e0-eaa09556d165; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; TS013ed49a=01538efd7c7fe16ea06b4b698988bbca81ffd8e6b5d6397d953fee423cc5bc927d6d15c5e60253ada1b1107dac8673af86e33360f4; ak_bmsc=5DFEFE19D3338A92552CC96CBEE845E4~000000000000000000000000000000~YAAQVi4gF2mCIiSBAQAAsBvtOhDt+TnOAnqrGbJbwWLHW44KVJboMFsS27rN4QcmsA5RA4llS5hpGE9cH2KO/prdvibTGkn3z1KeF2VZeNPg25oiZvB71LHaRXnfJHf+KqvJcekYjfD5SNuiCv7WCUNLzO0XOpeFlCaH7F18NmQXJzj07i39mSCM8CFVrSZUafkeZ/VvTZB/yVF9MkM2INgytxCXwZ33bL/QmhECM0glOJQQtW/OSpDwyO4PQgLLc7NrgeKs9glOU/iHE638B+Cng6DqnC+eGm+APDUCWCsCUfnkFsODrDAhHmFKg/noWJ9Jvf+8FeTwfmoiy2JxpmePJvhio/I7YzPo8MV76RlzwjKKJ53BTeFDrA==; assortmentStoreId=3531; auth=MTAyOTYyMDE491W2ipO%2Ba1alPAYvzCrqoTONC6QI1kOkYlQ06gEDHmBf4HGA3hRFG496QjQWWIMPdhp51jIm0V3ZBZ%2Bv8r0925CMPxTlYCaUAOsLY1UEl2yoPk8bL%2FZQHpsivZd3nasI767wuZloTfhm7Wk2Kcjygi5k0VvBM%2FJjwcKWWhCnBS8cSOuS03S3uTYEOH6P1BlzLvVAzng1Y1GtspZRwx6M1Mhmp0PrvaqCK8gMWT7%2BBO0UMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrq%2FGLYYlxNYjeDycQGMJcs8FeHbTRO0qM4qvBSlrb81MF%2B20s9Lx2p3QeFctyM4aqHpLF7vj8gubTgIvUDt1%2FObuG02e%2BO%2FnsuKl0AHUsl5f5B7e46FmnjjHs%2F125jLrjSQzX7MAlLBJXxL%2Bwi6fx6Y%3D; bm_mi=6380A2B75655736047CFA6E894B7C3D7~YAAQbC4gFyWVGCaBAQAAAaj1OhCIbPKOL3zU8HdgPQtpnXXCRLz0nUU66pzOlsrmKurPmOj7Wbd+vvcwzajLQf9gSeES40WsObnr8s8tvPV5TRgsY6dXijQgnFiFUCeMgyQMxrFeAORMrJbJi/BgY8atlEe/N1U84ZPOHPmB1vskQAgsN4sYm1ZU9SUus981Z767lbHftkl310Y3FO2wQ3hLiKnNBbHtbIYw+tBFLeBIpoyCRjkZj1vjIBRbE25OgWmRROVbf8lfaYktX0DJJwExjLGjfkhTdv8B1R/nGj9SB88ulMMOgSAuPw3H47T0ZrHEM+cgT/iJPggj5i04jNGeeFBn75hoC0fwxARIxjDZ5Wz4l+pTpYcOOwIbvA==~1; bm_sv=4C419486FD45574CD30E9F95ECBFDB9F~YAAQbC4gFyaVGCaBAQAAAaj1OhBE9p8mu+k/u+zKjg0ydcgNYqOLtJs0y9aA9pnE6brX079TLkusSP//vwUjyX2S7MKEVZfyI/+WbBKpZDK1BqmoIRezAXPg9rXKVof+sYM2GSKjmu4lKVzZAOO1SmJXNFm2J1rNQhaaYWO2gxLg7wmev9WaakRVmkvmGYHuEArBwcx6GNXoGO6p2PvgEqFhYBN+a5rpWGetVIuGgRrzGgssgMEHhK4+QF4QtwKRqg==~1; bstc=eTP5-qMeB3Q6zMD3kp1ncE; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1654484165000@firstcreate:1649092530820"; exp-ck=0Nd9e10t4gT11jR7v16Yrc-18wp7a29Lv_92Zm3yB2eJ9VH2eXnIH1gVG-b1gynZP2hGNr-1hQziI2obzLE1; hasACID=true; hasLocData=1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIzNTMxIiwiZGlzcGxheU5hbWUiOiJMYWNleSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5ODUxNiIsImFkZHJlc3NMaW5lMSI6IjE0MDEgR2FsYXh5IERyIE5lIiwiY2l0eSI6IkxhY2V5Iiwic3RhdGUiOiJXQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTg1MTYtNDc0NiJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDcuMDYwNDY1LCJsb25naXR1ZGUiOi0xMjIuNzczODQ0fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiMzUzMSIsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdfV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6NDcuMDA3OSwibG9uZ2l0dWRlIjotMTIyLjc1MzMsInBvc3RhbENvZGUiOiI5ODUxMyIsImNpdHkiOiJPbHltcGlhIiwic3RhdGUiOiJXQSIsImNvdW50cnlDb2RlIjoiVVNBIiwiZ2lmdEFkZHJlc3MiOmZhbHNlfSwiYXNzb3J0bWVudCI6eyJub2RlSWQiOiIzNTMxIiwiZGlzcGxheU5hbWUiOiJMYWNleSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiI0NzU3IiwiZGlzcGxheU5hbWUiOiJMYWNleSBOZWlnaGJvcmhvb2QgTWFya2V0Iiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk4NTAzIiwiYWRkcmVzc0xpbmUxIjoiNTExMCBZZWxtIEhpZ2h3YXkiLCJjaXR5IjoiTGFjZXkiLCJzdGF0ZSI6IldBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5ODUwMy0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjo0Ni45OTcyMDYsImxvbmdpdHVkZSI6LTEyMi44MTg3NTd9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjpmYWxzZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiNDc1NyIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NTQ1NzMxODU3MDUsInZhbGlkYXRlS2V5IjoicHJvZDp2MjpiNzQ2OGMyNS04NWJjLTQ5Y2QtOTVlMC1lYWEwOTU1NmQxNjUifQ%3D%3D; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjM1MzEiLCJ0aW1lc3RhbXAiOjE2NTQ0ODE4MDU2NDd9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY1NDQ4MTgwNTY0NywiYmFzZSI6Ijk4NTEzIn0sInZhbGlkYXRlS2V5IjoicHJvZDp2MjpiNzQ2OGMyNS04NWJjLTQ5Y2QtOTVlMC1lYWEwOTU1NmQxNjUifQ%3D%3D; mobileweb=0; vtc=WHMuN-dcOBqeI-JqQXna-U; xpa=0Nd9e|0t4gT|1jR7v|6Yrc-|8wp7a|9DjTL|9Lv_9|HmBmS|LTD5Y|OBldi|ObD24|QnZNm|Umo04|Zm3yB|bupnU|cfVAR|duBe9|eJ9VH|eXnIH|gVG-b|gynZP|hGNr-|hQziI|obzLE|sGDe9|srerY|viJr2|xCzID; xpm=1%2B1654551025%2BWHMuN-dcOBqeI-JqQXna-U~%2B0; xptwg=1962312203:218CEB777F3E040:57178B9:298CD91:6CDD5847:D9DF77A2:; TS01b0be75=01538efd7ca00233a8d53fb0281c6e7b6784612cb202eed51c4c8db8e164254ee2ac67ae8f474e24788f785fc0ea0b3f280975b75f; akavpau_p2=1654552186~id=21b8e235792e570fa3b07605e2eec33e'
}

payload={}

url = "https://www.fredmeyer.com/pl/fresh-vegetables/06112?page=1"

url_list = []

for i in range(1, 30):
    url_list.append(url.replace("page=1", "page=" + str(i)))



item_names = []
price_list = []
priceper_list = []

for url in url_list:
  time.sleep(3)
  result = requests.get(url, headers=headers, data=payload)
  bsobj = soup(result.content,'lxml')
  
  product_name = bsobj.findAll('h3',{'class':'kds-Text--l text-default-900 font-secondary font-500 mt-8 mb-0'})
  product_price = bsobj.findAll('div',{'class':'b black f5 mr1 mr2-xl lh-copy f4-l'})
  product_priceper = bsobj.findAll('div',{'class':'f7 f6-l gray mr1'})
for names,price,priceper in zip(product_name,product_price, product_priceper):
    item_names.append(names.a.span.text.strip())
    price_list.append(price.text)
    priceper_list.append(priceper.text)

df = pd.DataFrame({'Product_Name':item_names, 'Price':price_list, 'Price_Per':product_priceper}, columns=['Product_Name', 'Price', 'PricePer'])
df.to_csv('Walmart Test' + '.csv')