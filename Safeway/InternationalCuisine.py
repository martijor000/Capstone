import requests
import json
import pandas as pd
import time
from sqlalchemy import create_engine

payload={}

def AsianFood():
    filename = "AsianFoods"
    url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=2374397450818&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_13_1&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D312&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; _clck=1f44y5o|1|f11|0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; incap_ses_526_1610353=fhPTQuvwV3oc0t7e6bpMB1Zga2IAAAAAYiGUDjaaGlRTrYVvitlXIA==; s_vncm=1651388399271%26vn%3D10; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651810046%7C9%7CMCAAMB-1651810046%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651212446s%7CNONE%7CvVersion%7C5.2.0; nlbi_1610353=/bzKNIbqNjy/6wll6eNT2gAAAAC/KCAM/udikxlQ6RS56pnL; s_nr30=1651209121146-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Agrains-pasta-sides%3Astuffing-mix; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D312; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9ZTNUS2dObVFEU1RMeVpXZ3hGRFJvbW9NX2UxMDhiOUMmbj03OVlpd1R5SFJIZmNsUGlJeEtnZ3FnJm09MSZ0PUFBQUFBR0pyYzZJJnJtPTEmcnQ9QUFBQUFHSnJjNkk; _clsk=1krfxqa|1651209814821|29|0|b.clarity.ms/collect; reese84=3:8FxH8bnRJw5KRPjUoBxxiA==:dAABWDFcIudaF+1ZzBtiIkbxTsddX5mJsu9+D3quvdotnXOS1IZ8uCWMHlk0K8g0mbQt439tV6PmK+N8IBOCcuw0NXV3gikXn0dLW1NpZqWWGQr7oStG3U+VfissCvWFRguj/g82kFlZ3EcxjydlVVg0zrXwnk5SbRoSEL3i+V5jIGlL07A7IHo+qJAmnJbaopYlPOdak8d5JcCWQ4T1IYaiDRafe8JiUEtlEIhY25XzF88CEWcZ5hc6y6ZQ/HtMODSUprzLq12B+KMhqvcHROFli1x5OMlihYFvVGYBaqgE+ccfa0m+YFzZi4XlviiUz51fIBr8uUyxVCHwsBjct/9A5ESF9sPTQpXypH3DEg2QDFDZ78Eybv0AWL/rGBcCn8ibMa0YrVUEHmEvIaJI/GZsbZ9UKTWvqXtA9HdtQlbB33QrdJ7K9DnBn5XkkFda+R4Q2aulcwt4LiWZuw3L/g==:yFmtYNt7D/ckq5fNJjyMs0YFzDUuDbljHyudFdYn8as=; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Agrains-pasta-sides%25253Astuffing-mix%2526link%253DAsian%252520Foods%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Agrains-pasta-sides%25253Astuffing-mix%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Finternational-cuisine%25252Fasian-foods.3132.html%2526ot%253DA; nlbi_1610353_2147483392=uF+teB4ROnZwKhG96eNT2gAAAABaFaKB5xH7ywzoI0HM7xAn; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714455403|session#830e1bec3bcf41f4ac750daeaa65d799#1651212463; ADRUM_BT1=R%3A86%7Ci%3A3313187%7Cd%3A156; ADRUM_BTa=R%3A86%7Cg%3Adf5c5397-5762-4a00-af6c-cd2bcf38e851%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=V0HiWu8uC2ku8na86eNT2gAAAACWeTskuKyiwgaYIod0KUbB; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/international-cuisine/asian-foods.3132.html?page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def HispanicFood():
    filename = "HispanicFoods"
    url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=4108339835382&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_13_2&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D314&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; _clck=1f44y5o|1|f11|0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; incap_ses_526_1610353=fhPTQuvwV3oc0t7e6bpMB1Zga2IAAAAAYiGUDjaaGlRTrYVvitlXIA==; s_vncm=1651388399271%26vn%3D10; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651810046%7C9%7CMCAAMB-1651810046%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651212446s%7CNONE%7CvVersion%7C5.2.0; nlbi_1610353=/bzKNIbqNjy/6wll6eNT2gAAAAC/KCAM/udikxlQ6RS56pnL; reese84=3:8FxH8bnRJw5KRPjUoBxxiA==:dAABWDFcIudaF+1ZzBtiIkbxTsddX5mJsu9+D3quvdotnXOS1IZ8uCWMHlk0K8g0mbQt439tV6PmK+N8IBOCcuw0NXV3gikXn0dLW1NpZqWWGQr7oStG3U+VfissCvWFRguj/g82kFlZ3EcxjydlVVg0zrXwnk5SbRoSEL3i+V5jIGlL07A7IHo+qJAmnJbaopYlPOdak8d5JcCWQ4T1IYaiDRafe8JiUEtlEIhY25XzF88CEWcZ5hc6y6ZQ/HtMODSUprzLq12B+KMhqvcHROFli1x5OMlihYFvVGYBaqgE+ccfa0m+YFzZi4XlviiUz51fIBr8uUyxVCHwsBjct/9A5ESF9sPTQpXypH3DEg2QDFDZ78Eybv0AWL/rGBcCn8ibMa0YrVUEHmEvIaJI/GZsbZ9UKTWvqXtA9HdtQlbB33QrdJ7K9DnBn5XkkFda+R4Q2aulcwt4LiWZuw3L/g==:yFmtYNt7D/ckq5fNJjyMs0YFzDUuDbljHyudFdYn8as=; s_nr30=1651210603154-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Ainternational-cuisine%3Aasian-foods; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D314; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9RFJid3NkYTRFTkUwQTVvSExlNGxDaWRqcTZNclNXSWEmbj1kNTcwNUxZbHFoSnpKU1B4X28talJ3Jm09MSZ0PUFBQUFBR0pyZVd3JnJtPTEmcnQ9QUFBQUFHSnJlV3c; _clsk=1krfxqa|1651210604764|30|0|b.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Ainternational-cuisine%25253Aasian-foods%2526link%253DHispanic%252520Foods%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Ainternational-cuisine%25253Aasian-foods%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Finternational-cuisine%25252Fhispanic-foods.3132.html%2526ot%253DA; nlbi_1610353_2147483392=dvzUKGsHvWjwhNku6eNT2gAAAABT9jJLHJJopWdRoCbphxpe; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714455615|session#830e1bec3bcf41f4ac750daeaa65d799#1651212675; ADRUM_BT1=R%3A95%7Ci%3A3313187%7Cd%3A158; ADRUM_BTa=R%3A95%7Cg%3A14e9477d-987e-43ba-b15c-c61749349780%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=V0HiWu8uC2ku8na86eNT2gAAAACWeTskuKyiwgaYIod0KUbB; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/international-cuisine/hispanic-foods.3132.html?sort=&page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def KosherFood():
    filename = "IceAndJuice"
    url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=5166351689451&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_15_6&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D268&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; _clck=1f44y5o|1|f11|0; incap_ses_526_1610353=cQTLY1NB+khyDoze6bpMB4U1a2IAAAAAHn8QHhS5ojJ8UtWcMbr+MA==; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; s_ivc=true; s_vncm=1651388399271%26vn%3D9; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651802805%7C9%7CMCAAMB-1651802805%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651205205s%7CNONE%7CvVersion%7C5.2.0; nlbi_1610353=6k49Ih2OjiKfmMx06eNT2gAAAACwWIGfiwE+C3fNAydsF4XQ; reese84=3:5J3aPr33ET9OD+xDiMkJpQ==:DmK+cG4CC7KOgD7QBO8th5EY4qFi9MakKMJgFelKl5gAQV2LVtsDT2nYQFp/ahW0fv8NU+PRh/JBTXRKRe+no/EwR2dF63gQQijP6kwax1gZ6HeoRn6/ZPX++GJb5oCjcUVIPoPRleF1CjNxGdPEgiyd8kDKL3QiZpmPjzqMhoBfPAS7M7lP5dwg6KLxmlu/p+xyOeyr3dKb1P6+RBIueImhxsUUzJleOuGbnInjCYirU23IimFTg5na4qcMNWp42mcfbrfM232VsxlWuygi64NfF9Ww+aqXkrKV3Fx+MCoFwybIpl1Z77qL/C2U5MMsig/1hJWemUv/5g00irNlqCWTQh7NoM+aj78wvfoOBwhEeoUa3giAoXS2YpyyR+giWCY4/D8U/sFUOuSgvJWLB+vjVXg68aEDtNqXR+Ceg8l8YBm2TV6vC+OXxMDRhgZun2zkHISzs74UkaIsaSsrvQ==:GTDnCE3ZZuyrphSzZVfdFbIILXMOUm4g5zDhysCqJq4=; s_nr30=1651200932707-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Afrozen-foods%3Afrozen-vegetables; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D268; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9RXpQTkltNjZ5aURjX3FSTUx5ZWoxU3JVWEx6V096ZVcmbj1NYlFtRHRZMjdvUEc1eEdoMmdtRFJRJm09MSZ0PUFBQUFBR0pyVTZZJnJtPTEmcnQ9QUFBQUFHSnJVNlk; _clsk=y6hckl|1651200934723|108|0|b.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Afrozen-foods%25253Afrozen-vegetables%2526link%253DIce%252520%252526%252520Frozen%252520Juice%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Afrozen-foods%25253Afrozen-vegetables%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Ffrozen-foods%25252Fice-frozen-juice.3132.html%2526ot%253DA; nlbi_1610353_2147483392=A4j/HhCr42Ozrm4v6eNT2gAAAADmTS/dsk4ibRUxkmWE695v; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714445875|session#53742e6f561f4801b76ce0a1cd91d816#1651202935; ADRUM_BT1=R%3A88%7Ci%3A3313187%7Ce%3A172%7Cd%3A159; ADRUM_BTa=R%3A88%7Cg%3Ab9aa0b12-ac06-4095-b602-7f42b8703c85%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=ParBUWk5BFRzww/F6eNT2gAAAACHSuGbgC92cwalPMQS1iQ8; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/frozen-foods/ice-frozen-juice.3132.html?sort=&page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    SafewayRequest(url, headers, payload, filename)
def FrozenIceCreamAndNovelty():
    filename = "IceCreamAndNovelties"
    url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=4919399184800&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_15_7&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D270&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; _clck=1f44y5o|1|f11|0; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; s_vncm=1651388399271%26vn%3D9; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651802805%7C9%7CMCAAMB-1651802805%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651205205s%7CNONE%7CvVersion%7C5.2.0; s_nr30=1651201074553-Repeat; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D270; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9N0Q5aTJnZmJINTR2M1FBTlAxVHVrQXdmaHozaktZeWYmbj1tdnctXy1CODdXRFYtYVIyanhyRWp3Jm09MSZ0PUFBQUFBR0pyVkRRJnJtPTEmcnQ9QUFBQUFHSnJWRFE; incap_ses_526_1610353=fhPTQuvwV3oc0t7e6bpMB1Zga2IAAAAAYiGUDjaaGlRTrYVvitlXIA==; reese84=3:rd6YmqKhctDWSCetO3sS3A==:nD/rdMFTRpYstXJ/uvgbVaOr7E/xsX5IWZ4QZxQHETCisHEE64mezCiQN7qV5GuswQslSdomU1SiN4ubMkqPGebB0e3y6k43tCXOksAwA2eEa389SjV8peI2Tgd3Ip1TlOZWyyOhJblw0wHv6cS0/2zjDpqj7S4EMfWaOenUon4aRSaN3JEW3I/Defbs4XewesnAJapIu1kOtd/ovqay0I92XHibGRpTxzV3cd+s4aBTGmu6aF8S57gLmds3dBgLR9FTi0xUpuWGphm7y4p+Aclmwz6JPa7CivZF/89vtHFYKn65gSESxmF3VJWpVQwffFJmWH82EnJHQ/Hgz4cMquLEHd0PcmZ0RIdSK1Nju0QHu00Y/ScTxRwdGssBi4X81XzeIwFCPpGW00NRxaFgbNjDp+xqZnDY9WTgyzapbp5eMT3KlEUu3JNLRRRUmya5O+tHkW8DwGVd+vy+j35sTQ==:b9KXlkku8p4UHD5G0+waYylDCPQL9yjqPSFlYgB7MC0=; _clsk=1krfxqa|1651204232624|1|0|b.clarity.ms/collect; nlbi_1610353=r+v/UnDFLkB+310S6eNT2gAAAABYePuocupLwT53MeGQQbTQ; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Afrozen-foods%25253Aice-frozen-juice%2526link%253DIce%252520Cream%252520%252526%252520Novelties%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Afrozen-foods%25253Aice-frozen-juice%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Ffrozen-foods%25252Fice-cream-novelties.3132.html%2526ot%253DA; nlbi_1610353_2147483392=ou+HZJ5lVVKAb4Pz6eNT2gAAAAA5KjVegHOR0cSI3U7snZZr; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714449044|session#830e1bec3bcf41f4ac750daeaa65d799#1651206104; ADRUM_BT1=R%3A85%7Ci%3A3313187%7Cd%3A170; ADRUM_BTa=R%3A85%7Cg%3A074178a2-bea0-457c-8d3c-ce9a47231c10%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=ParBUWk5BFRzww/F6eNT2gAAAACHSuGbgC92cwalPMQS1iQ8; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/frozen-foods/ice-cream-novelties.3132.html?page=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
    SafewayRequest(url, headers, payload, filename)
    url = "https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=2220313860318&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=20&search-type=category&category-id=1_12_11&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D244&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"

    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ADRUM_BTa=R%3A85%7Cg%3A0a918de7-3428-4d41-b7bf-6130a15d5177%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; ADRUM_BT1=R%3A85%7Ci%3A3313187%7Ce%3A174%7Cd%3A152; SameSite=None; safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; ECommBanner=safeway; ECommSignInCount=0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; safeway_ga_gid=GA1.2.1368526857.1651178650; _ga_LZL2CD3SX2=GS1.1.1651178679.10.1.1651181182.0; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19112%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1651795298%7C9%7CMCAAMB-1651795298%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651197698s%7CNONE%7CvVersion%7C5.2.0; _clck=1f44y5o|1|f11|0; nlbi_1610353=McYPUXp1oExSo1J+6eNT2gAAAAD2m3eSNyaV92BOd/RCaHsY; incap_ses_526_1610353=cQTLY1NB+khyDoze6bpMB4U1a2IAAAAAHn8QHhS5ojJ8UtWcMbr+MA==; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; s_ivc=true; s_vncm=1651388399271%26vn%3D9; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:GNJLsMj9GAf0JEqBpFFc9g==:Sz+4UktAdj/XQnBQ3o2xFbxaTlfmIXVZNj9TSuY2yL+4Se2R9KU4f811yrFJhZEKBiGGPs4bFso+sQIZTxfSNSaQ7rcM+AIHau7gb6mhBTj7QP+LZ1LHhgng5UBWzw/fSqGHmAtUafhPLYywGdWBPro/eiMwsOL3Cq3grGQjNU6kP+IgQtUa/b7i1Jnjf+rYvODvnHkZwv7ciAd/mGUu7V/jiSCQDHqbkvTInjsppZ3bD8yb9AfrctjEQix38mYbUbuZjCs5gug9/PtdMgSJ5iOGn/0lO1vYZZUaKbW5jFt+qv7pB/NmkxdjH6kHcDVW9LDlkqCwqoW5uXbbIEoinx/eyi9Uo60jGhPQ9+z6kD/Wp1/RkuLkAFheDwryMJPiQWgdYmvVsZCcSaCrxK//TNdeDi4HbWZMAI/0tOcg8yxDQJFLqx6L3l8RbRIWDWI/Bp2aJu1Zs6a2XRtx5wpDYw==:GjfVJ9Wh72IpguoAULylBeYZUzb8e9Nsicc4mXT3LTQ=; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714440729|session#53742e6f561f4801b76ce0a1cd91d816#1651197789; s_nr30=1651195928714-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Adeli%3Adeli-sandwiches-wraps; _gat_gtag_UA_172784514_2=1; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D246; _uetsid=f4bbb860c73311eca899f12ac5286d6c; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9LUNhWlZMQTQ5VU9icDUwelV3cTdpNnRpenZUX2s4b1Umbj1FckJpMlJhclNZWjlWQ2RVMU5Xcm5RJm09MSZ0PUFBQUFBR0pyUUJvJnJtPTEmcnQ9QUFBQUFHSnJRQm8; _clsk=y6hckl|1651195930397|92|0|b.clarity.ms/collect; nlbi_1610353_2147483392=Kyn2Cnx0yzRa8dTq6eNT2gAAAACEkiBeB7zCXJyewLd1A+Cj; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Adeli%25253Adeli-sandwiches-wraps%2526link%253DLoad%252520more%2526region%253Dsearch-grid_0%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Adeli%25253Adeli-sandwiches-wraps%2526pidt%253D1%2526oid%253DLoad%252520more%2526oidt%253D3%2526ot%253DSUBMIT; ADRUM_BT1=R%3A85%7Ci%3A3313187%7Cd%3A152; ADRUM_BTa=R%3A85%7Cg%3Ab3c70ad3-a0cf-4117-bb18-f6604fb1dea5%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=pM22IGWtkTVlmmnJ6eNT2gAAAAADduG/x40UVUZFZFCT2/WF; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
    'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
    'referer': 'https://www.safeway.com/shop/aisles/deli/deli-sandwiches-wraps.3132.html?sort=&page=2',
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
  engine.execute('DROP TABLE IF EXISTS ' + "InternationalCuisine" + tableName)

# add table to sql server
  prods.to_sql("InternationalCuisine" + tableName, index=False, con=engine)

  # write the DataFrame to a table in the sql database