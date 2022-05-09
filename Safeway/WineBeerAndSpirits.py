import requests
import json
import pandas as pd
import time
from sqlalchemy import create_engine

payload={}

def Beer():
    filename = "Beer"
    url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=4322310147923&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_29_1&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D404&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; safeway_ga_gid=GA1.2.798881682.1651463806; _clck=1f44y5o|1|f14|0; nlbi_1610353=pHnFPYkoVnVMeX/d6eNT2gAAAAB75ZuADAQClSFeJoNcDzl0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; _ga_LZL2CD3SX2=GS1.1.1651516956.12.0.1651516956.0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; s_vncm=1654066799943%26vn%3D4; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; s_nr30=1651531209121-Repeat; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D404; _uetsid=e29fdfc0c9cb11eca160b303e1375430; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9NGFGdnJVWGNYSXQwd0FiUDJ4MFpRNHk5WTBGM0x0dzYmbj1oc3NHMl9DZGNBTDFVNlgwOGtwcHFRJm09MSZ0PUFBQUFBR0p3WGNrJnJtPTEmcnQ9QUFBQUFHSndYY2s; incap_ses_526_1610353=V2ERZ4HMJC6+2hnl6bpMBy5lcGIAAAAAqX1TjtVbaTBg8Uz91r1Zmw==; reese84=3:nUhcyc2zGiN/NG8kHyVk3A==:SnpYUfuz7a4C11Asiupf9lpW87G4jD4LHrhEpGnv2HHV5mAu7/yQlHtAo2umDqtBGB9A+HXSUKmpiGVfdGEr9Tq1iDamOCvzPeHAuO3hPzGefzl1dUPZ1SrV77ibhQP5F1UAsbp1wGvLxLKw0i2MIkR7R39nCLqPjfBYxLyKnNsy8NOrn4mRVlZlTav+4FI7ed95bBpZ+SNVugK9XuKmYC16ttY3USnStOxWMS4PvGcqxv4iE4lPgKfnvsJRpOYCfCqfJlhoSv5icxvgMxmcoQtBn8gIFG+8yma9Mxdh/ojkFQ0GzYYnfy/NzkwrLAb+sRp3mNxNw5Ye3eOavw8CMkf66HnqFf9OGkKuVCAAmvAL0zkyk8fPOkQSi2t1OLzLOJcmYhHNjwIyOwIq/DimxkkivceBVQVHJfC5o8pbaHH7VY0NMz/QVPIpt+8ZdjC6PSVGqvuKO+gwfufCD8jnuP3Ydf7wgBGNyU89bSKPZ6w=:7RbnSGdZby1bjTUnRsO5PnNNvhtCAb2LsshJJSAUlXE=; _clsk=jtala3|1651533104244|1|0|l.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Apet-care%25253Asmall-animal-care%2526link%253DBeer%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Apet-care%25253Asmall-animal-care%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fwine-beer-spirits%25252Fbeer.3132.html%2526ot%253DA; nlbi_1610353_2147483392=UBf2HwLGpFWzfY5q6eNT2gAAAAAdu13LWstx1ilcv8hpSaeh; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19115%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1652137985%7C9%7CMCAAMB-1652137985%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651540385s%7CNONE%7CvVersion%7C5.2.0; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714777986|session#b8c71014e51d4103956b08a01fdfe9a8#1651535046; ADRUM_BT1=R%3A81%7Ci%3A3313187%7Cd%3A155; ADRUM_BTa=R%3A81%7Cg%3Acf519af5-efc6-4ba8-ba60-b3108766b6ec%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=e29bOv/T8kQZLTOE6eNT2gAAAADs7+HMWPJtn78YdHOxnL6O; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/wine-beer-spirits/beer.3132.html?sort=&page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def SpiritsAndMixer():
    filename = "SpiritsAndMixers"
    url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=8320360794275&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_29_2&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D406&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; safeway_ga_gid=GA1.2.798881682.1651463806; _clck=1f44y5o|1|f14|0; nlbi_1610353=pHnFPYkoVnVMeX/d6eNT2gAAAAB75ZuADAQClSFeJoNcDzl0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; _ga_LZL2CD3SX2=GS1.1.1651516956.12.0.1651516956.0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; incap_ses_526_1610353=V2ERZ4HMJC6+2hnl6bpMBy5lcGIAAAAAqX1TjtVbaTBg8Uz91r1Zmw==; reese84=3:nUhcyc2zGiN/NG8kHyVk3A==:SnpYUfuz7a4C11Asiupf9lpW87G4jD4LHrhEpGnv2HHV5mAu7/yQlHtAo2umDqtBGB9A+HXSUKmpiGVfdGEr9Tq1iDamOCvzPeHAuO3hPzGefzl1dUPZ1SrV77ibhQP5F1UAsbp1wGvLxLKw0i2MIkR7R39nCLqPjfBYxLyKnNsy8NOrn4mRVlZlTav+4FI7ed95bBpZ+SNVugK9XuKmYC16ttY3USnStOxWMS4PvGcqxv4iE4lPgKfnvsJRpOYCfCqfJlhoSv5icxvgMxmcoQtBn8gIFG+8yma9Mxdh/ojkFQ0GzYYnfy/NzkwrLAb+sRp3mNxNw5Ye3eOavw8CMkf66HnqFf9OGkKuVCAAmvAL0zkyk8fPOkQSi2t1OLzLOJcmYhHNjwIyOwIq/DimxkkivceBVQVHJfC5o8pbaHH7VY0NMz/QVPIpt+8ZdjC6PSVGqvuKO+gwfufCD8jnuP3Ydf7wgBGNyU89bSKPZ6w=:7RbnSGdZby1bjTUnRsO5PnNNvhtCAb2LsshJJSAUlXE=; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19115%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1652137985%7C9%7CMCAAMB-1652137985%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651540385s%7CNONE%7CvVersion%7C5.2.0; s_nr30=1651533185554-Repeat; s_vncm=1654066799943%26vn%3D5; s_ivc=true; gpv_Page=safeway%3Adelivery%3Aaisles%3Awine-beer-spirits%3Abeer; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D406; _uetsid=e29fdfc0c9cb11eca160b303e1375430; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9dzFWSjZwbzdNOVBfZDduU09wNlNva0F4RFBlaTBlMmgmbj1LUUVBNU0zRC1JTmc3THpDa0REQmt3Jm09MSZ0PUFBQUFBR0p3WllNJnJtPTEmcnQ9QUFBQUFHSndaWU0; _clsk=jtala3|1651533187943|2|0|l.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Awine-beer-spirits%25253Abeer%2526link%253DSpirits%252520%252526%252520Mixers%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Awine-beer-spirits%25253Abeer%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fwine-beer-spirits%25252Fspirits-mixers.3132.html%2526ot%253DA; nlbi_1610353_2147483392=mHx9RSRJwQWtQ0TK6eNT2gAAAADYi7H/XwlFm2PuiKpNNln9; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714778073|session#b8c71014e51d4103956b08a01fdfe9a8#1651535133; ADRUM_BT1=R%3A91%7Ci%3A3313187%7Ce%3A192%7Cd%3A157; ADRUM_BTa=R%3A91%7Cg%3Af0dee370-a92f-4549-8e0e-0689142894ba%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; ADRUM_BTs=R%3A91%7Cs%3Af; SameSite=None; nlbi_1610353=e29bOv/T8kQZLTOE6eNT2gAAAADs7+HMWPJtn78YdHOxnL6O; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/wine-beer-spirits/spirits-mixers.3132.html?sort=&page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def Wine():
  filename = "Wine"
  url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=4773932919365&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_29_3&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D408&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
  headers = {
  'authority': 'www.safeway.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; safeway_ga_gid=GA1.2.798881682.1651463806; _clck=1f44y5o|1|f14|0; nlbi_1610353=pHnFPYkoVnVMeX/d6eNT2gAAAAB75ZuADAQClSFeJoNcDzl0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; _ga_LZL2CD3SX2=GS1.1.1651516956.12.0.1651516956.0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; incap_ses_526_1610353=V2ERZ4HMJC6+2hnl6bpMBy5lcGIAAAAAqX1TjtVbaTBg8Uz91r1Zmw==; reese84=3:nUhcyc2zGiN/NG8kHyVk3A==:SnpYUfuz7a4C11Asiupf9lpW87G4jD4LHrhEpGnv2HHV5mAu7/yQlHtAo2umDqtBGB9A+HXSUKmpiGVfdGEr9Tq1iDamOCvzPeHAuO3hPzGefzl1dUPZ1SrV77ibhQP5F1UAsbp1wGvLxLKw0i2MIkR7R39nCLqPjfBYxLyKnNsy8NOrn4mRVlZlTav+4FI7ed95bBpZ+SNVugK9XuKmYC16ttY3USnStOxWMS4PvGcqxv4iE4lPgKfnvsJRpOYCfCqfJlhoSv5icxvgMxmcoQtBn8gIFG+8yma9Mxdh/ojkFQ0GzYYnfy/NzkwrLAb+sRp3mNxNw5Ye3eOavw8CMkf66HnqFf9OGkKuVCAAmvAL0zkyk8fPOkQSi2t1OLzLOJcmYhHNjwIyOwIq/DimxkkivceBVQVHJfC5o8pbaHH7VY0NMz/QVPIpt+8ZdjC6PSVGqvuKO+gwfufCD8jnuP3Ydf7wgBGNyU89bSKPZ6w=:7RbnSGdZby1bjTUnRsO5PnNNvhtCAb2LsshJJSAUlXE=; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19115%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1652137985%7C9%7CMCAAMB-1652137985%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651540385s%7CNONE%7CvVersion%7C5.2.0; s_vncm=1654066799943%26vn%3D5; s_ivc=true; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D408; _uetsid=e29fdfc0c9cb11eca160b303e1375430; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9S3NHYTN0VHRaOGxjQVZzUkZkSm5hQ0NUbThfMDhyVk8mbj13OVk3ZmpjSlRtdG5jWmZsblpSaTZ3Jm09MSZ0PUFBQUFBR0p3WmRrJnJtPTEmcnQ9QUFBQUFHSndaZGs; _clsk=jtala3|1651533274412|3|0|l.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Awine-beer-spirits%25253Aspirits-mixers%2526link%253DWine%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Awine-beer-spirits%25253Aspirits-mixers%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fwine-beer-spirits%25252Fwine.3132.html%2526ot%253DA; nlbi_1610353_2147483392=So/Ld4/tAmqV3xv16eNT2gAAAADNXfgH1FqCwvqyTwMa4j8P; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714778161|session#b8c71014e51d4103956b08a01fdfe9a8#1651535221; s_nr30=1651533360825-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Awine-beer-spirits%3Awine; ADRUM_BT1=R%3A81%7Ci%3A3313187%7Ce%3A161%7Cd%3A164; ADRUM_BTa=R%3A81%7Cg%3Aa5d6f236-23e1-4fbb-bf20-151999c67137%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=e29bOv/T8kQZLTOE6eNT2gAAAADs7+HMWPJtn78YdHOxnL6O; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
  'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
  'referer': 'https://www.safeway.com/shop/aisles/wine-beer-spirits/wine.3132.html?sort=&page=1',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  SafewayRequest(url, headers, payload, filename)

def SafewayRequest(updateURL, insertHeaders, insertPayload, tableName): 
  for rows in range(30, 1000, 30):
    test = updateURL.replace("rows=30", "rows=" + str(rows))
    newURL = f"{test}"
    r = requests.get(newURL, headers=insertHeaders, data=insertPayload)
    data = json.loads(r.text)
    if(r.ok == True and "response" in data):
        newData = data["response"]["docs"]
        time.sleep(3)
        print(f'Getting row {rows}', 'waiting..')
    else:
      break
  
  filteredData = []
  # Filtering out duplicate data from our request by going through each object and seeing if its already in our filtered data object.
  for x in newData:
    if x not in filteredData: 
      filteredData.append(x)
  prods = pd.DataFrame([])
  prods = prods.from_records(pd.json_normalize(newData)) 
  prods = prods.drop(columns=['sellByWeight','aisleName', 'prop65WarningIconRequired', 'departmentName', 'pid', 'aisleId', 'upc', 'restrictedValue', 'displayType', 'averageWeight', 'salesRank', 'id', 'featured', 'inventoryAvailable', 'pastPurchased', 'isArProduct', 'displayUnitQuantityText', 'promoEndDate', 'isMtoProduct', 'displayEstimateText', 'channelEligibility.delivery', 'channelEligibility.inStore', 'channelEligibility.pickUp', 'channelInventory.delivery', 'channelInventory.pickup', 'channelInventory.instore', 'preparationTime', 'unitQuantity', 'basePrice'], axis=1)
  # prods.to_csv('Safeway-Baby' + str(fileName) + '.csv')

  DB = {'servername': '(localdb)\MSSQLLocalDB',
      'database': 'Safeway',
      'driver': 'driver=SQL Server Native Client 11.0'}


  engine = create_engine('mssql+pyodbc://' + DB['servername'] + '/' + DB['database'] + "?" + DB['driver'])
  engine.execute('DROP TABLE IF EXISTS ' + "WineBeerAndSpirits" + tableName)

# add table to sql server
  prods.to_sql("WineBeerAndSpirits" + tableName, index=False, con=engine)

  # write the DataFrame to a table in the sql database