import requests
import json
import pandas as pd
import time

def SafewayButterAndSourCream():
    filename = "ButterAndSourCream"
    url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=5678764357426&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_11_1&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D218&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

    payload={}
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; incap_ses_526_1610353=OPixaiuj7xqNDfbd6bpMB5f8amIAAAAA8fei1mu+RceuCG4di0BzLw==; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommBanner=safeway; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_ivc=true; s_vncm=1651388399271%26vn%3D8; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _clck=1f44y5o|1|f10|0; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19110%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651790655%7C9%7CMCAAMB-1651790655%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651193055s%7CNONE%7CvVersion%7C5.2.0; s_nr30=1651188849838-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Acookies-snacks-candy%3Asalsa-dips; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D218; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9bWxaRmJEeXR3Rk5xbkFVSlFmY2pKT19hZ0tIcDRxc08mbj1kMjRQTUlOeFg0Y0tXOG5zcTVwTTBRJm09MSZ0PUFBQUFBR0pySkhNJnJtPTEmcnQ9QUFBQUFHSnJKSE0; reese84=3:x3hxsiIR2rZlDDa/awjjAQ==:dKSI02hEsNbqJ3jBPPFNyWGNVZDoIFnWvFiDpiqFccycozrudnpUbdTleRHkljofEzxXGPHllDjCDa4Fh+ncHYvQEPf2OGyhwAiNLgIDONWCzQZHRLTwlW89PGV4OfJX7sNSu+cmTA1Ksg+b592S706UJ8lwzvaZvwlK2GlUOZ72Jix9bdO11wr5YcjO35gP2NNR9UB59lnyMiEhy6JSBLBL/i6UfLT+jQNvnBCyPDWSKxUXty0Kj4odZdlZzFhWRxZKkcrrY0Y3ldxU1RIMTJkVzB9oFlu48i6COQFCnfn3waia8ExfNEkmSxM8jNy+g5eAlebh/p40x/Sj00cGUBpVX1xia/l8n1asqANVaJYsDxhKTS2XVwlOtNGzjP05Jak8mWlL15U4nkCO/ZFFhuw1HIbH2caTrLgj/wgQ7a8fgr3duBxEHJLRDNG32MsipHngDDLqdK3CUXh7b0JVHA==:FOCbBTRvl93qHgpy51dFAXMy49opAPqD9GgG0rd0MxU=; _clsk=y6hckl|1651190232224|69|0|b.clarity.ms/collect; nlbi_1610353=37N2FYSQah7jICRU6eNT2gAAAACcfwsIe/IHuuG1Z8cEa43A; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Acookies-snacks-candy%25253Asalsa-dips%2526link%253DButter%252520%252526%252520Sour%252520Cream%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Acookies-snacks-candy%25253Asalsa-dips%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fdairy-eggs-cheese%25252Fbutter-sour-cream.3132.html%2526ot%253DA; nlbi_1610353_2147483392=Nq/ef4zzWiun2RlO6eNT2gAAAABiDg3w9aELyZxQMiqvBsk3; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714435156|session#a15305c092034645a49e74eac4c6f5fc#1651192216; ADRUM_BT1=R%3A88%7Ci%3A3313187%7Cd%3A154; ADRUM_BTa=R%3A88%7Cg%3A1344384a-e374-492c-a466-4fd56ffe69e6%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=oJy3Jn7gWxYp9E646eNT2gAAAACEqq3Nv9xMtjLrNZ4YwE5m; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/dairy-eggs-cheese/butter-sour-cream.3132.html?page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def SafewayCheese():
    filename = "Cheeses"
    url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=7299837989011&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_11_11&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D220&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

    payload={}
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; incap_ses_526_1610353=OPixaiuj7xqNDfbd6bpMB5f8amIAAAAA8fei1mu+RceuCG4di0BzLw==; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommBanner=safeway; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_vncm=1651388399271%26vn%3D8; s_ivc=true; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _clck=1f44y5o|1|f10|0; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; reese84=3:x3hxsiIR2rZlDDa/awjjAQ==:dKSI02hEsNbqJ3jBPPFNyWGNVZDoIFnWvFiDpiqFccycozrudnpUbdTleRHkljofEzxXGPHllDjCDa4Fh+ncHYvQEPf2OGyhwAiNLgIDONWCzQZHRLTwlW89PGV4OfJX7sNSu+cmTA1Ksg+b592S706UJ8lwzvaZvwlK2GlUOZ72Jix9bdO11wr5YcjO35gP2NNR9UB59lnyMiEhy6JSBLBL/i6UfLT+jQNvnBCyPDWSKxUXty0Kj4odZdlZzFhWRxZKkcrrY0Y3ldxU1RIMTJkVzB9oFlu48i6COQFCnfn3waia8ExfNEkmSxM8jNy+g5eAlebh/p40x/Sj00cGUBpVX1xia/l8n1asqANVaJYsDxhKTS2XVwlOtNGzjP05Jak8mWlL15U4nkCO/ZFFhuw1HIbH2caTrLgj/wgQ7a8fgr3duBxEHJLRDNG32MsipHngDDLqdK3CUXh7b0JVHA==:FOCbBTRvl93qHgpy51dFAXMy49opAPqD9GgG0rd0MxU=; s_nr30=1651190356612-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Adairy-eggs-cheese%3Abutter-sour-cream; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D220; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9QXRoV0pCV19DVUY0TUxBZElsMFhFVkNtdlJoNjF6d2Imbj1hR3JNZERwYjBiR0MtWUZURWF4Z1hRJm09MSZ0PUFBQUFBR0pyS2xZJnJtPTEmcnQ9QUFBQUFHSnJLbFk; _clsk=y6hckl|1651190358925|70|0|b.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Adairy-eggs-cheese%25253Abutter-sour-cream%2526link%253DCheese%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Adairy-eggs-cheese%25253Abutter-sour-cream%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fdairy-eggs-cheese%25252Fcheese.3132.html%2526ot%253DA; nlbi_1610353=GCo5ZbYBKHCP0chJ6eNT2gAAAACPvIXevx4DHBVVnbAHySoD; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651795298%7C9%7CMCAAMB-1651795298%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651197698s%7CNONE%7CvVersion%7C5.2.0; nlbi_1610353_2147483392=5wyCYIJSon1HZxMD6eNT2gAAAAD0yTciS+nPvBgc3cU6VzIw; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714435299|session#a15305c092034645a49e74eac4c6f5fc#1651192359; ADRUM_BT1=R%3A83%7Ci%3A3313187%7Ce%3A172%7Cd%3A154; ADRUM_BTa=R%3A83%7Cg%3Ab559a8d2-6028-4be4-8e62-6ff1bd81a015%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=oJy3Jn7gWxYp9E646eNT2gAAAACEqq3Nv9xMtjLrNZ4YwE5m; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/dairy-eggs-cheese/cheese.3132.html?sort=&page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def SafewayEggs():
    filename = "Eggs"
    url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=7819984489144&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_11_3&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D222&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

    payload={}
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; incap_ses_526_1610353=OPixaiuj7xqNDfbd6bpMB5f8amIAAAAA8fei1mu+RceuCG4di0BzLw==; ECommBanner=safeway; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommSignInCount=0; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_vncm=1651388399271%26vn%3D8; s_ivc=true; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; reese84=3:x3hxsiIR2rZlDDa/awjjAQ==:dKSI02hEsNbqJ3jBPPFNyWGNVZDoIFnWvFiDpiqFccycozrudnpUbdTleRHkljofEzxXGPHllDjCDa4Fh+ncHYvQEPf2OGyhwAiNLgIDONWCzQZHRLTwlW89PGV4OfJX7sNSu+cmTA1Ksg+b592S706UJ8lwzvaZvwlK2GlUOZ72Jix9bdO11wr5YcjO35gP2NNR9UB59lnyMiEhy6JSBLBL/i6UfLT+jQNvnBCyPDWSKxUXty0Kj4odZdlZzFhWRxZKkcrrY0Y3ldxU1RIMTJkVzB9oFlu48i6COQFCnfn3waia8ExfNEkmSxM8jNy+g5eAlebh/p40x/Sj00cGUBpVX1xia/l8n1asqANVaJYsDxhKTS2XVwlOtNGzjP05Jak8mWlL15U4nkCO/ZFFhuw1HIbH2caTrLgj/wgQ7a8fgr3duBxEHJLRDNG32MsipHngDDLqdK3CUXh7b0JVHA==:FOCbBTRvl93qHgpy51dFAXMy49opAPqD9GgG0rd0MxU=; nlbi_1610353=GCo5ZbYBKHCP0chJ6eNT2gAAAACPvIXevx4DHBVVnbAHySoD; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651795298%7C9%7CMCAAMB-1651795298%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651197698s%7CNONE%7CvVersion%7C5.2.0; s_nr30=1651190498549-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Adairy-eggs-cheese%3Acheese; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D222; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _clck=1f44y5o|1|f11|0; _derived_epik=dj0yJnU9cW9DOWxTV3ZQZjlhM1pMaUhBemtSYU9uY3N1dktKRDQmbj1rSEtoN25taVdDTEFmOE5iemx2WXJRJm09MSZ0PUFBQUFBR0pyS3VRJnJtPTEmcnQ9QUFBQUFHSnJLdVE; _clsk=y6hckl|1651190500388|71|0|b.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Adairy-eggs-cheese%25253Acheese%2526link%253DEggs%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Adairy-eggs-cheese%25253Acheese%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fdairy-eggs-cheese%25252Feggs.3132.html%2526ot%253DA; nlbi_1610353_2147483392=nJgXJe6dcyeZLCrF6eNT2gAAAACVMiFvw+rqR4iUZfR6a9LT; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714435406|session#a15305c092034645a49e74eac4c6f5fc#1651192466; ADRUM_BT1=R%3A81%7Ci%3A3313187%7Ce%3A170%7Cd%3A216; ADRUM_BTa=R%3A81%7Cg%3A015092d4-689f-40bd-82eb-c6c54547abd1%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=ow2PO+5TRFEIlyUw6eNT2gAAAABdKn1fiL02BrplC8YJYDDz; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/dairy-eggs-cheese/eggs.3132.html?sort=&page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def SafewayMilkAndCream():
    filename = "MilkAndCream"
    url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=4018358666558&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_11_4&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D224&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

    payload={}
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; incap_ses_526_1610353=OPixaiuj7xqNDfbd6bpMB5f8amIAAAAA8fei1mu+RceuCG4di0BzLw==; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommBanner=safeway; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_vncm=1651388399271%26vn%3D8; s_ivc=true; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651795298%7C9%7CMCAAMB-1651795298%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651197698s%7CNONE%7CvVersion%7C5.2.0; _clck=1f44y5o|1|f11|0; s_nr30=1651190605261-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Adairy-eggs-cheese%3Aeggs; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D224; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _clsk=y6hckl|1651190606918|72|0|b.clarity.ms/collect; _derived_epik=dj0yJnU9d0poWWxqLURBaml2REhCZkZaRjdqMW9zY3VqYWxyaEEmbj05TTRGU2M2UjVhWVhybXBua0N0dVB3Jm09MSZ0PUFBQUFBR0pySzA0JnJtPTEmcnQ9QUFBQUFHSnJLMDQ; reese84=3:xr7z0gh7VB+/nXT3TVqXhQ==:ewuQztgAaBIgtB2U44IDDIA+hbAVzYgu9dpqKTS5pZn8ljs4gqAdfqxshvezl/NIjUDgBDiy0lMR4MS2P1VEFwUy8StsA5H8+JoiprVxmDJGp6hw9W1O9hRNkzsHIiK7ftlBl/pHms0igiYY9eIjnN3qFpIaWSs32JW45IaWvJ0uk9jD0OQp65BGJ0wN+0Or5LFYRLHetXO4LP1OHGqG4QXbWsw1A3kRHivHEQNFRgxbTSR9UEloSxjHuuJwlrCHBJ1ZGbWva+HC6Ly5ZGjWDTDJsIdMYwfxjl46hpVad2s4X55dNzJsZj5WoycJvo+q4TGWvQgCQD6Y9J4FH1kabEHJqsF0rtuP1znrZrD2U/tgwptHNyqFERvtz5ux6u3kmBbi03m0b1GGRAG1R3v+4HYxn0yvn2pRUYE3vCYDi2w=:HvlZuPFtwSkymo1lwyDHwktXXJmaSZqgF3dPbzNZWlQ=; nlbi_1610353=CLwGMsxQ/1mPbI8P6eNT2gAAAAAQyaOxV1GGcJM3uoUs2JmR; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Adairy-eggs-cheese%25253Aeggs%2526link%253DMilk%252520%252526%252520Cream%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Adairy-eggs-cheese%25253Aeggs%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fdairy-eggs-cheese%25252Fmilk-cream.3132.html%2526ot%253DA; nlbi_1610353_2147483392=UwtiWFRWIT3s/4Vn6eNT2gAAAABKC97LxQ5Lj5dOKmhoRsjV; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714435519|session#a15305c092034645a49e74eac4c6f5fc#1651192579; ADRUM_BT1=R%3A87%7Ci%3A3313187%7Cd%3A311; ADRUM_BTa=R%3A87%7Cg%3Ae8d3981f-3548-40af-a60e-2c22c5d1a51d%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=ow2PO+5TRFEIlyUw6eNT2gAAAABdKn1fiL02BrplC8YJYDDz; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/dairy-eggs-cheese/milk-cream.3132.html?sort=&page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def SafewayYogurtAndPudding():
    filename = "YogurtAndPudding"
    url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=3510898000529&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_11_8&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D226&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

    payload={}
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; incap_ses_526_1610353=OPixaiuj7xqNDfbd6bpMB5f8amIAAAAA8fei1mu+RceuCG4di0BzLw==; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommBanner=safeway; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22default%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_vncm=1651388399271%26vn%3D8; s_ivc=true; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22default%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651795298%7C9%7CMCAAMB-1651795298%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651197698s%7CNONE%7CvVersion%7C5.2.0; _clck=1f44y5o|1|f11|0; reese84=3:xr7z0gh7VB+/nXT3TVqXhQ==:ewuQztgAaBIgtB2U44IDDIA+hbAVzYgu9dpqKTS5pZn8ljs4gqAdfqxshvezl/NIjUDgBDiy0lMR4MS2P1VEFwUy8StsA5H8+JoiprVxmDJGp6hw9W1O9hRNkzsHIiK7ftlBl/pHms0igiYY9eIjnN3qFpIaWSs32JW45IaWvJ0uk9jD0OQp65BGJ0wN+0Or5LFYRLHetXO4LP1OHGqG4QXbWsw1A3kRHivHEQNFRgxbTSR9UEloSxjHuuJwlrCHBJ1ZGbWva+HC6Ly5ZGjWDTDJsIdMYwfxjl46hpVad2s4X55dNzJsZj5WoycJvo+q4TGWvQgCQD6Y9J4FH1kabEHJqsF0rtuP1znrZrD2U/tgwptHNyqFERvtz5ux6u3kmBbi03m0b1GGRAG1R3v+4HYxn0yvn2pRUYE3vCYDi2w=:HvlZuPFtwSkymo1lwyDHwktXXJmaSZqgF3dPbzNZWlQ=; s_nr30=1651190718365-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Adairy-eggs-cheese%3Amilk-cream; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D226; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9R3Fmal9nNkIzYVRBeUNHT1VDMHZ4WDkwa0h0YzZ4SVEmbj1admR6ZTZxOER2amtVTGR0V29oRnJnJm09MSZ0PUFBQUFBR0pySzhBJnJtPTEmcnQ9QUFBQUFHSnJLOEE; _clsk=y6hckl|1651190720272|73|0|b.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Adairy-eggs-cheese%25253Amilk-cream%2526link%253DYogurt%252520%252526%252520Pudding%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Adairy-eggs-cheese%25253Amilk-cream%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fdairy-eggs-cheese%25252Fyogurt-pudding.3132.html%2526ot%253DA; nlbi_1610353=faGNRtVryXdHiuk16eNT2gAAAADIknB6go3sA/CYs2gxKTwZ; nlbi_1610353_2147483392=yPChdfD0tQzwMqjQ6eNT2gAAAACPOgjB3Xi/XDL8i7P01lzU; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714435619|session#a15305c092034645a49e74eac4c6f5fc#1651192679; ADRUM_BT1=R%3A91%7Ci%3A3313187%7Cd%3A161; ADRUM_BTa=R%3A91%7Cg%3Acd5b8895-28d2-4bbb-b3a6-08a89b76f45f%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; ADRUM_BTs=R%3A91%7Cs%3Af; SameSite=None; nlbi_1610353=ow2PO+5TRFEIlyUw6eNT2gAAAABdKn1fiL02BrplC8YJYDDz; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/dairy-eggs-cheese/yogurt-pudding.3132.html?sort=&page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)

def SafewayRequest(updateURL, insertHeaders, insertPayload, fileName): 

  prods = pd.DataFrame([])
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

  prods = prods.from_records(pd.json_normalize(newData)) 
  prods.to_csv('Safeway' + str(fileName) + '.csv')

###############################
# Main Program
###############################
# SafewayButterAndSourCream()
# SafewayCheese()
# SafewayEggs()
# SafewayMilkAndCream()
# SafewayYogurtAndPudding()