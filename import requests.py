import requests
import json
import pandas as pd
import time

# I access the endpoint and created an API call from postman. A lot of credit goes to https://www.youtube.com/watch?v=GqICHBfeAWk&t=556s he helped me alot and showed me ways to bypass safeways security and make api calls without being blocked.
payload={}
headers = {
  'authority': 'www.safeway.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'adrum': 'isAjax:true',
  'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; nlbi_1610353=lrDYC3VEzngyDYw/6eNT2gAAAABugtT4hzw6RnKIVEOSvwDb; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; incap_ses_217_1610353=10H2SjQKblqaGZtl7PACA4kuT2IAAAAANCPL13TE/jOx4AQagYfC3g==; incap_ses_1567_1610353=pMVhTd0w6gGDTPSiRxq/FcHIUWIAAAAAS31Falsjs5Kllp0ehr7N/w==; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19092%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1650131778%7C9%7CMCAAMB-1650131778%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1649534178s%7CNONE%7CvVersion%7C5.2.0; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; s_vncm=1651388399271%26vn%3D2; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:az+saKrjCXTm0w6cAMsvIA==:jW1VCFCCu5YcVjWLFO5nblSfKnBVs3A0gWNQgG+DR9jE9wPvtqbTm2mzdXj76dgsJ11kujCzvuhkW/vn816xiLiMwcj8FFls7WAXiJHWsWF5c/25NND8UHbnTVDOHFTwPcBCA65zwOwiF3Im0rGcjmIl+UpvdPtlsysJwMWEbatpTGRzWzgiI1j5YvEZkm0czm3E/qqlf0VudlKZIFEDHGu+M5YkCMiEsx67HxPCFcoWPdTaT+c2RO/jhT8xn3G9vsWoDj1H4ba2Ig+Adqy78xrT9k0s5mACpgLB+G4YHamAZHV9WBo2BYZgc13VjgNQDA1u75J9HUemKpRRFM7Wg6jLlCxvupvHxvS5zzV2paIx6pvQEZsnFRKgcYkWnG015y1iJoC5D6/SkwMTblp0Ok5O0mPq9KAjLccSrsFJxVntw2T69FOTDNDqRGSIHwVW7HaqS8T+NXv52rTMljihBfw9LkyBHbzGjmFIEuiDvbo=:1oRyMMrrhPHFCSVDyL2gB/kt5RN/lDPxhmgKArbndPc=; safeway_ga_gid=GA1.2.1473246677.1649526980; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _clck=1f44y5o|1|f0h|0; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; _ga_LZL2CD3SX2=GS1.1.1649527265.2.0.1649527265.0; gpv_Page=safeway%3Aloyalty%3Alp%3Afresh-produce%3Aproduce; s_sq=%5B%5BB%5D%5D; s_nr30=1649527294609-Repeat; _uetsid=5cb91640b82e11ec85a95b940c11c91e; _uetvid=268bbf80756511ec99edb56d6bb4e245; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D11; _derived_epik=dj0yJnU9cW50Zng0ZHJLZzhhcG4ybE91ZHhlcDU1QW8wQXRBWDUmbj1hM3FUaVZZLVgxLXkzRkhldlNQN01RJm09MSZ0PUFBQUFBR0pSeWY0JnJtPTEmcnQ9QUFBQUFHSlJ5ZjQ; _clsk=p6xdcx|1649527295365|3|0|i.clarity.ms/collect; ADRUM=s=1649527447986&r=https%3A%2F%2Fwww.safeway.com%2Flp%2Ffresh-produce%2Fproduce.html; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1712772249|session#cbf62dc1e2374e099c498ca50d03e68e#1649529309; nlbi_1610353_2147483392=yrnoMiTKQ2wa3/8X6eNT2gAAAADz4KWJWTcJXBZN5bcSdlzw; incap_ses_1567_1610353=yt53A6xoC0S+fdSnRxq/Fc27U2IAAAAAmKN5RpK93WYnJ3vOpYIEdg==; nlbi_1610353=OtCGAh8fpj4lq5U36eNT2gAAAAALkcS9GON9WeVsn5CzHT3h; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
  'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
  'referer': 'https://www.safeway.com/lp/fresh-produce/produce.html',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}


prods = pd.DataFrame([])


for rows in range(0, 1000, 30):
  url = f"https://www.safeway.com/abs/pub/xapi/wcax/pathway/search?request-id=7205314034675&url=https://www.safeway.com&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D11&q=produce&rows={rows}&start=1&channel=instore&storeid=3132&sort=&widget-id=39r3q79r&facet=false&availabilityCheck=true&banner=safeway"
  r = requests.get(url, headers=headers, data=payload)
  data = json.loads(r.text)
  if(r.ok == True):
    newData = data["response"]["docs"]
    time.sleep(5)
    print(f'Getting row {rows}', 'waiting..')
  else:
    break
  
filteredData = []
# Filtering out duplicate data from our request by going through each object and seeing if its already in our filtered data object.
for x in newData:
  if x not in filteredData: 
    filteredData.append(x)

print(newData)

prods = prods.append(pd.json_normalize(newData), ignore_index=True)

prods.to_csv('safeway-produce.csv')



