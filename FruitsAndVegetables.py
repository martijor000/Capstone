import requests
import json
import pandas as pd
import time

def SafewayFreshFruits():
  filename = "FreshFruits"
  url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=4423603710089&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=20&search-type=category&category-id=1_23_1&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D274&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

  payload={}
  headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ADRUM_BTa=R%3A89%7Cg%3Ac083317d-9148-4626-98ea-fb63b7264549%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; ADRUM_BT1=R%3A89%7Ci%3A3313187%7Ce%3A171%7Cd%3A212; SameSite=None; safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; _clck=1f44y5o|1|f11|0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; incap_ses_526_1610353=fhPTQuvwV3oc0t7e6bpMB1Zga2IAAAAAYiGUDjaaGlRTrYVvitlXIA==; nlbi_1610353=r+v/UnDFLkB+310S6eNT2gAAAABYePuocupLwT53MeGQQbTQ; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; s_vncm=1651388399271%26vn%3D10; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:SMkxa1ljVUx31huBeaWIhw==:9wqF5rvd9lZycrSBbJT76Ufvp8AYmHQAT0vuGDX3gL+Nn4AfKB8nnWNLhZ3cE4FsbQMTbUQediq9A389bn9Y6tYWxkNt8TDllmOvvFEYG+zzss1gwmmUP9VPo4Wgeh63EMHcwOO7ck+NpfO03jdNJgWYhEy2bO5GvsuXbP10o1mXNtGgS3o4xsK04xBuTu8tCEyC1tw38Y7OsLh69ayUFpwMSyI6pl8ZYPDOr78jUJ8vfQ2A402eYFlB9xzOAy4jDSdtLE4kTqlWxTIoF976xKaublOgZtm8VTfR/r6ABbcJ8pcA5E/YUX6DuLtnD6agwk9LiYK7GERBj6adO4IvW0F9NNb4w/Mf7YsidKZBE7HjatO7+XCIUaj1b68jEy4OUuEiQArRUNa8Al5co0NmVPccrX9BGdV0jUlWk4aNyjlqMknoABCmT39ZQjz0gHJTJuB/in0Sr0gfHzI1Gat/Ng==:+HOSag2X46daRnJUHBMZ9fMrlTz4U/bDIu6m2lkWDEo=; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651810046%7C9%7CMCAAMB-1651810046%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651212446s%7CNONE%7CvVersion%7C5.2.0; gpv_Page=safeway%3Adelivery%3Aaisles%3Afruits-vegetables%3Afresh-fruits; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714450118|session#830e1bec3bcf41f4ac750daeaa65d799#1651207178; s_nr30=1651205317914-Repeat; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D276; _gat_gtag_UA_172784514_2=1; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9ZGUyQ3pnN2F5MERfTWV0YjFBU0ZHQThEQkVEOTZ6c0smbj1PWDVyQnlQcWl1OWI2TTZmWlVTTVBRJm09MSZ0PUFBQUFBR0pyWk1jJnJtPTEmcnQ9QUFBQUFHSnJaTWM; _clsk=1krfxqa|1651205320021|5|0|b.clarity.ms/collect; nlbi_1610353_2147483392=W72rD2b4jWumz4Qo6eNT2gAAAABWWPmWPvAgLiQ1x+XEfBjP; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%25253Afresh-fruits%2526link%253DLoad%252520more%2526region%253Dsearch-grid_0%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%25253Afresh-fruits%2526pidt%253D1%2526oid%253DLoad%252520more%2526oidt%253D3%2526ot%253DSUBMIT; ADRUM_BT1=R%3A89%7Ci%3A3313187%7Ce%3A178%7Cd%3A217; ADRUM_BTa=R%3A89%7Cg%3Aa9d5159c-7818-408e-854a-cb1a788cdeaa%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=ParBUWk5BFRzww/F6eNT2gAAAACHSuGbgC92cwalPMQS1iQ8; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/fruits-vegetables/fresh-fruits.3132.html?sort=&page=2',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  SafewayRequest(url, headers, payload, filename)
def SafewayFreshVegetablesAndHerbs():
  filename = "FreshVegetablesAndHerbs"
  url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=4670931000210&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=20&search-type=category&category-id=1_23_2&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D276&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

  payload={}
  headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ADRUM_BTa=R%3A99%7Cg%3A6d53d9e0-a86f-4b4a-904d-0b0924dfa386%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; ADRUM_BT1=R%3A99%7Ci%3A3313187%7Ce%3A166%7Cd%3A157; SameSite=None; safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; _clck=1f44y5o|1|f11|0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; incap_ses_526_1610353=fhPTQuvwV3oc0t7e6bpMB1Zga2IAAAAAYiGUDjaaGlRTrYVvitlXIA==; nlbi_1610353=r+v/UnDFLkB+310S6eNT2gAAAABYePuocupLwT53MeGQQbTQ; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; s_vncm=1651388399271%26vn%3D10; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:SMkxa1ljVUx31huBeaWIhw==:9wqF5rvd9lZycrSBbJT76Ufvp8AYmHQAT0vuGDX3gL+Nn4AfKB8nnWNLhZ3cE4FsbQMTbUQediq9A389bn9Y6tYWxkNt8TDllmOvvFEYG+zzss1gwmmUP9VPo4Wgeh63EMHcwOO7ck+NpfO03jdNJgWYhEy2bO5GvsuXbP10o1mXNtGgS3o4xsK04xBuTu8tCEyC1tw38Y7OsLh69ayUFpwMSyI6pl8ZYPDOr78jUJ8vfQ2A402eYFlB9xzOAy4jDSdtLE4kTqlWxTIoF976xKaublOgZtm8VTfR/r6ABbcJ8pcA5E/YUX6DuLtnD6agwk9LiYK7GERBj6adO4IvW0F9NNb4w/Mf7YsidKZBE7HjatO7+XCIUaj1b68jEy4OUuEiQArRUNa8Al5co0NmVPccrX9BGdV0jUlWk4aNyjlqMknoABCmT39ZQjz0gHJTJuB/in0Sr0gfHzI1Gat/Ng==:+HOSag2X46daRnJUHBMZ9fMrlTz4U/bDIu6m2lkWDEo=; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651810046%7C9%7CMCAAMB-1651810046%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651212446s%7CNONE%7CvVersion%7C5.2.0; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714450250|session#830e1bec3bcf41f4ac750daeaa65d799#1651207310; s_nr30=1651205449611-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Afruits-vegetables%3Afresh-vegetables-herbs; _gat_gtag_UA_172784514_2=1; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D278; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9ODE1YVFUb212OGpLM3h2V2djQUw1NTJoTGFwQTlvdHkmbj1ISUh0QkxaaUVoQ1F0LTRnV1NQanpRJm09MSZ0PUFBQUFBR0pyWlVvJnJtPTEmcnQ9QUFBQUFHSnJaVW8; _clsk=1krfxqa|1651205451163|7|0|b.clarity.ms/collect; nlbi_1610353_2147483392=bHTjfGoNpCbVkt6a6eNT2gAAAAB1l5qBAwrjQ/eiWtDqfzcv; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%25253Afresh-vegetables-herbs%2526link%253DLoad%252520more%2526region%253Dsearch-grid_0%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%25253Afresh-vegetables-herbs%2526pidt%253D1%2526oid%253DLoad%252520more%2526oidt%253D3%2526ot%253DSUBMIT; ADRUM_BT1=R%3A99%7Ci%3A3313187%7Cd%3A327; ADRUM_BTa=R%3A99%7Cg%3A810b6f65-f82b-43b8-a0af-565ae66aadb4%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=ParBUWk5BFRzww/F6eNT2gAAAACHSuGbgC92cwalPMQS1iQ8; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/fruits-vegetables/fresh-vegetables-herbs.3132.html?sort=&page=2',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  SafewayRequest(url, headers, payload, filename)
def SafewayNutsAndDriedFruits():
  filename = "NutsAndDriedFruits"
  url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=7265449127247&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=20&search-type=category&category-id=1_23_3&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D278&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

  payload={}
  headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ADRUM_BTa=R%3A94%7Cg%3A470d329d-37ad-4f57-8c4d-642398d52ac4%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; ADRUM_BT1=R%3A94%7Ci%3A3313187%7Ce%3A173%7Cd%3A152; SameSite=None; safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; _clck=1f44y5o|1|f11|0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; incap_ses_526_1610353=fhPTQuvwV3oc0t7e6bpMB1Zga2IAAAAAYiGUDjaaGlRTrYVvitlXIA==; nlbi_1610353=r+v/UnDFLkB+310S6eNT2gAAAABYePuocupLwT53MeGQQbTQ; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; s_vncm=1651388399271%26vn%3D10; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:SMkxa1ljVUx31huBeaWIhw==:9wqF5rvd9lZycrSBbJT76Ufvp8AYmHQAT0vuGDX3gL+Nn4AfKB8nnWNLhZ3cE4FsbQMTbUQediq9A389bn9Y6tYWxkNt8TDllmOvvFEYG+zzss1gwmmUP9VPo4Wgeh63EMHcwOO7ck+NpfO03jdNJgWYhEy2bO5GvsuXbP10o1mXNtGgS3o4xsK04xBuTu8tCEyC1tw38Y7OsLh69ayUFpwMSyI6pl8ZYPDOr78jUJ8vfQ2A402eYFlB9xzOAy4jDSdtLE4kTqlWxTIoF976xKaublOgZtm8VTfR/r6ABbcJ8pcA5E/YUX6DuLtnD6agwk9LiYK7GERBj6adO4IvW0F9NNb4w/Mf7YsidKZBE7HjatO7+XCIUaj1b68jEy4OUuEiQArRUNa8Al5co0NmVPccrX9BGdV0jUlWk4aNyjlqMknoABCmT39ZQjz0gHJTJuB/in0Sr0gfHzI1Gat/Ng==:+HOSag2X46daRnJUHBMZ9fMrlTz4U/bDIu6m2lkWDEo=; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651810046%7C9%7CMCAAMB-1651810046%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651212446s%7CNONE%7CvVersion%7C5.2.0; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714450477|session#830e1bec3bcf41f4ac750daeaa65d799#1651207537; s_nr30=1651205676209-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Afruits-vegetables%3Anuts-dried-fruits; _gat_gtag_UA_172784514_2=1; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D280; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9b3Yzak1WOFZfNlFKMnYxcXh1RXd1OGlmWDZSc3dlZXcmbj1CbmFmWjVnU3pJRm5SMzYzZjhTMGFRJm09MSZ0PUFBQUFBR0pyWmkwJnJtPTEmcnQ9QUFBQUFHSnJaaTA; _clsk=1krfxqa|1651205677735|9|0|b.clarity.ms/collect; nlbi_1610353_2147483392=ZQvzQ64tVgOcvm1n6eNT2gAAAACiVjI9KAONhAU1jI149Cw0; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%25253Anuts-dried-fruits%2526link%253DLoad%252520more%2526region%253Dsearch-grid_0%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%25253Anuts-dried-fruits%2526pidt%253D1%2526oid%253DLoad%252520more%2526oidt%253D3%2526ot%253DSUBMIT; ADRUM_BT1=R%3A94%7Ci%3A3313187%7Ce%3A161%7Cd%3A153; ADRUM_BTa=R%3A94%7Cg%3A926122db-08bf-44b0-bd5c-2444fd4e6a8f%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=ParBUWk5BFRzww/F6eNT2gAAAACHSuGbgC92cwalPMQS1iQ8; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/fruits-vegetables/nuts-dried-fruits.3132.html?sort=&page=2',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  SafewayRequest(url, headers, payload, filename)
def SafewayPackagedProduce():
  filename = "PackagedProduce"
  url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=9238092787180&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_23_4&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D280&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

  payload={}
  headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; _clck=1f44y5o|1|f11|0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; incap_ses_526_1610353=fhPTQuvwV3oc0t7e6bpMB1Zga2IAAAAAYiGUDjaaGlRTrYVvitlXIA==; nlbi_1610353=r+v/UnDFLkB+310S6eNT2gAAAABYePuocupLwT53MeGQQbTQ; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; s_vncm=1651388399271%26vn%3D10; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:SMkxa1ljVUx31huBeaWIhw==:9wqF5rvd9lZycrSBbJT76Ufvp8AYmHQAT0vuGDX3gL+Nn4AfKB8nnWNLhZ3cE4FsbQMTbUQediq9A389bn9Y6tYWxkNt8TDllmOvvFEYG+zzss1gwmmUP9VPo4Wgeh63EMHcwOO7ck+NpfO03jdNJgWYhEy2bO5GvsuXbP10o1mXNtGgS3o4xsK04xBuTu8tCEyC1tw38Y7OsLh69ayUFpwMSyI6pl8ZYPDOr78jUJ8vfQ2A402eYFlB9xzOAy4jDSdtLE4kTqlWxTIoF976xKaublOgZtm8VTfR/r6ABbcJ8pcA5E/YUX6DuLtnD6agwk9LiYK7GERBj6adO4IvW0F9NNb4w/Mf7YsidKZBE7HjatO7+XCIUaj1b68jEy4OUuEiQArRUNa8Al5co0NmVPccrX9BGdV0jUlWk4aNyjlqMknoABCmT39ZQjz0gHJTJuB/in0Sr0gfHzI1Gat/Ng==:+HOSag2X46daRnJUHBMZ9fMrlTz4U/bDIu6m2lkWDEo=; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651810046%7C9%7CMCAAMB-1651810046%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651212446s%7CNONE%7CvVersion%7C5.2.0; s_nr30=1651205676209-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Afruits-vegetables%3Anuts-dried-fruits; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D280; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9b3Yzak1WOFZfNlFKMnYxcXh1RXd1OGlmWDZSc3dlZXcmbj1CbmFmWjVnU3pJRm5SMzYzZjhTMGFRJm09MSZ0PUFBQUFBR0pyWmkwJnJtPTEmcnQ9QUFBQUFHSnJaaTA; _clsk=1krfxqa|1651205687509|10|0|b.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%25253Anuts-dried-fruits%2526link%253DPackaged%252520Produce%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Afruits-vegetables%25253Anuts-dried-fruits%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Ffruits-vegetables%25252Fpackaged-produce.3132.html%2526ot%253DA; nlbi_1610353_2147483392=dU7YTe5NZRetKfNL6eNT2gAAAAD7Nqs9T2mkxmd30n0JaC5K; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714450621|session#830e1bec3bcf41f4ac750daeaa65d799#1651207681; ADRUM_BT1=R%3A93%7Ci%3A3313187%7Ce%3A185%7Cd%3A155; ADRUM_BTa=R%3A93%7Cg%3A6c4a3f9f-c529-432a-9156-3cee02d04f4b%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=ParBUWk5BFRzww/F6eNT2gAAAACHSuGbgC92cwalPMQS1iQ8; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/fruits-vegetables/packaged-produce.3132.html?sort=&page=1',
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
# SafewayFreshFruits()
# SafewayFreshVegetablesAndHerbs()
# SafewayNutsAndDriedFruits()
# SafewayPackagedProduce()

