import requests
import json
import pandas as pd
import time
from sqlalchemy import create_engine

payload={}

def CatCare():
  filename = "CatCare"
  url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=6864012685082&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_22_2&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D398&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
  headers = {
  'authority': 'www.safeway.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; safeway_ga_gid=GA1.2.798881682.1651463806; _clck=1f44y5o|1|f14|0; nlbi_1610353=pHnFPYkoVnVMeX/d6eNT2gAAAAB75ZuADAQClSFeJoNcDzl0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; _ga_LZL2CD3SX2=GS1.1.1651516956.12.0.1651516956.0; incap_ses_526_1610353=oE47BUQdAGWJCtLk6bpMB0o4cGIAAAAAA6D1qqy+p0zx5FaBd9HpqA==; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19115%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1652130144%7C9%7CMCAAMB-1652130144%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651532544s%7CNONE%7CvVersion%7C5.2.0; s_vncm=1654066799943%26vn%3D4; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; s_nr30=1651530049584-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Apersonal-care-health%3Avitamins-supplements; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D398; _uetsid=e29fdfc0c9cb11eca160b303e1375430; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9TGlmUjlRZWZHNmdwbWZ2V0VxZXpzYVRRNlJkdlBSU2wmbj00T1UxUTFUV1JtTV85allnczhLa2R3Jm09MSZ0PUFBQUFBR0p3V1VJJnJtPTEmcnQ9QUFBQUFHSndXVUk; _clsk=oye3oc|1651530864700|22|0|l.clarity.ms/collect; reese84=3:3A/tzWntUf77Tzl8GgmOIg==:IRhGO1diISL+3Hdcdaan5JvA515kFfu+cSs3TigpG/hbiQblT7WJFqeSwuEuewauh9BIdM4oleQg+xNLUe8HUvYYT4Qj8uYtyoBNEUDAhT1hTEPAALjXZMpIMpVK7SyZSeMf+EmK1h65P2g7zFPZ+EGx3csV75zR+oi4LHjQDdgKYvGvbxguj/zUnMyEuf1yhRLpO81IH6aK2FArrH9Mn7JKw/tc2bUQ0jjgX8YqNCNMdtUBCJJX2wf9hRKpS6aplrLB0F3pd4tnakvzuAvocThuqHADWw+dAFspMXzEqXBaFq3g8HVsOZfQCuQZL2QfA32AMTAVmLq7PgNpr4elmV82qXWEeVeqI4M4+b0rV+jBVKJEb1EpWNLh6jeBN0NppBxd00UxOMR3OubWIAfMGk5XhlowiHg5qgsIETN0TmU=:ReZ9HLnXzbCVvDz+lKfd7PIEJQi7CQ5mN2LMxC5IZoA=; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Apersonal-care-health%25253Avitamins-supplements%2526link%253DCat%252520Care%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Apersonal-care-health%25253Avitamins-supplements%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fpet-care%25252Fcat-care.3132.html%2526ot%253DA; nlbi_1610353_2147483392=6/nfd77QgR6YD0Sh6eNT2gAAAACal20daO3RbnsdjuO00WjD; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714775771|session#ff976e21c4e246ef811c922e86f4e099#1651532831; ADRUM_BT1=R%3A76%7Ci%3A3313187%7Cd%3A159; ADRUM_BTa=R%3A76%7Cg%3A0554566d-d711-43b7-bb0f-08412a7945cb%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=e29bOv/T8kQZLTOE6eNT2gAAAADs7+HMWPJtn78YdHOxnL6O; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
  'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
  'referer': 'https://www.safeway.com/shop/aisles/pet-care/cat-care.3132.html?sort=&page=1',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  SafewayRequest(url, headers, payload, filename)
def DogCare():
  filename = "DogCare"
  url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=8242196968295&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_22_4&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D400&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
  headers = {
  'authority': 'www.safeway.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; safeway_ga_gid=GA1.2.798881682.1651463806; _clck=1f44y5o|1|f14|0; nlbi_1610353=pHnFPYkoVnVMeX/d6eNT2gAAAAB75ZuADAQClSFeJoNcDzl0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; _ga_LZL2CD3SX2=GS1.1.1651516956.12.0.1651516956.0; incap_ses_526_1610353=oE47BUQdAGWJCtLk6bpMB0o4cGIAAAAAA6D1qqy+p0zx5FaBd9HpqA==; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19115%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1652130144%7C9%7CMCAAMB-1652130144%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651532544s%7CNONE%7CvVersion%7C5.2.0; s_vncm=1654066799943%26vn%3D4; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:3A/tzWntUf77Tzl8GgmOIg==:IRhGO1diISL+3Hdcdaan5JvA515kFfu+cSs3TigpG/hbiQblT7WJFqeSwuEuewauh9BIdM4oleQg+xNLUe8HUvYYT4Qj8uYtyoBNEUDAhT1hTEPAALjXZMpIMpVK7SyZSeMf+EmK1h65P2g7zFPZ+EGx3csV75zR+oi4LHjQDdgKYvGvbxguj/zUnMyEuf1yhRLpO81IH6aK2FArrH9Mn7JKw/tc2bUQ0jjgX8YqNCNMdtUBCJJX2wf9hRKpS6aplrLB0F3pd4tnakvzuAvocThuqHADWw+dAFspMXzEqXBaFq3g8HVsOZfQCuQZL2QfA32AMTAVmLq7PgNpr4elmV82qXWEeVeqI4M4+b0rV+jBVKJEb1EpWNLh6jeBN0NppBxd00UxOMR3OubWIAfMGk5XhlowiHg5qgsIETN0TmU=:ReZ9HLnXzbCVvDz+lKfd7PIEJQi7CQ5mN2LMxC5IZoA=; s_nr30=1651530971064-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Apet-care%3Acat-care; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D400; _uetsid=e29fdfc0c9cb11eca160b303e1375430; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9NFNUNzhNOUZhanl5bGlqeU9UbmNBMEdRUWtvT0dwdHAmbj1BWHRXMFhyMUpua3BNdjJwckt5X1hBJm09MSZ0PUFBQUFBR0p3WE53JnJtPTEmcnQ9QUFBQUFHSndYTnc; _clsk=oye3oc|1651530972818|23|0|l.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Apet-care%25253Acat-care%2526link%253DDog%252520Care%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Apet-care%25253Acat-care%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fpet-care%25252Fdog-care.3132.html%2526ot%253DA; nlbi_1610353_2147483392=5hKkTL01LHXiwGAc6eNT2gAAAABHApeWjNrqw6+OLRQMz291; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714775918|session#ff976e21c4e246ef811c922e86f4e099#1651532978; ADRUM_BT1=R%3A76%7Ci%3A3313187%7Cd%3A163; ADRUM_BTa=R%3A76%7Cg%3Ab74857d7-ca37-4a45-8828-591f7d3ee836%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=e29bOv/T8kQZLTOE6eNT2gAAAADs7+HMWPJtn78YdHOxnL6O; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
  'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
  'referer': 'https://www.safeway.com/shop/aisles/pet-care/dog-care.3132.html?sort=&page=1',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  SafewayRequest(url, headers, payload, filename)
def SmallAnimalCare():
  filename = "SmallAnimalCare"
  url = f"https://www.safeway.com/abs/pub/xapi/v1/aisles/products?request-id=9423743962487&url=https://www.safeway.com&pageurl=https://www.safeway.com&pagename=aisles&rows=30&start=0&search-type=category&category-id=1_22_5&storeid=3132&featured=true&search-uid=uid%253D9587123903556%253Av%253D12.0%253Ats%253D1649266626599%253Ahc%253D402&q=&sort=&userid=&featuredsessionid=&screenwidth=859&dvid=web-4.1aisles&pp=none&channel=instore&banner=safeway"
  headers = {
  'authority': 'www.safeway.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'safeway_ga=GA1.2.1007655441.1642183783; visid_incap_1610353=C6jZu81NRRqgbzwUkiBufCwoS2IAAAAAQUIPAAAAAADon/9DcCZd8vODizgnIvcy; aam_uuid=48286462568079877321785283656852940828; _gcl_au=1.1.1370304885.1649266627; _fbp=fb.1.1649266627349.646321825; _pin_unauth=dWlkPVpUSXlPVFl3Wm1RdE9EWXpOUzAwT1RZMExXRmpaREF0Wm1NMk1XSmlORFU0T0RWbA; _ga=GA1.1.1007655441.1642183783; _gac_UA-172784514-2=1.1649526980.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_aw=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _gcl_dc=GCL.1649526981.CjwKCAjw3cSSBhBGEiwAVII0Z8vz76iVXE1F7hzQvxe1hhA4SiCKFHOENbuatLZSgDUEmaSDAqxrhBoC3AgQAvD_BwE; _fwnguid=f3845b1e-554e-43d7-b304-af6a09333fb6; __qca=P0-192704564-1649527253282; safeway_ga_gid=GA1.2.798881682.1651463806; _clck=1f44y5o|1|f14|0; nlbi_1610353=pHnFPYkoVnVMeX/d6eNT2gAAAAB75ZuADAQClSFeJoNcDzl0; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; s_cc=true; _ga_LZL2CD3SX2=GS1.1.1651516956.12.0.1651516956.0; incap_ses_526_1610353=oE47BUQdAGWJCtLk6bpMB0o4cGIAAAAAA6D1qqy+p0zx5FaBd9HpqA==; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19115%7CMCMID%7C53070417963508696801324674344628904632%7CMCAAMLH-1652130144%7C9%7CMCAAMB-1652130144%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1651532544s%7CNONE%7CvVersion%7C5.2.0; s_vncm=1654066799943%26vn%3D4; s_ivc=true; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%223132%22%2C%22zipcode%22%3A%2294611%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:3A/tzWntUf77Tzl8GgmOIg==:IRhGO1diISL+3Hdcdaan5JvA515kFfu+cSs3TigpG/hbiQblT7WJFqeSwuEuewauh9BIdM4oleQg+xNLUe8HUvYYT4Qj8uYtyoBNEUDAhT1hTEPAALjXZMpIMpVK7SyZSeMf+EmK1h65P2g7zFPZ+EGx3csV75zR+oi4LHjQDdgKYvGvbxguj/zUnMyEuf1yhRLpO81IH6aK2FArrH9Mn7JKw/tc2bUQ0jjgX8YqNCNMdtUBCJJX2wf9hRKpS6aplrLB0F3pd4tnakvzuAvocThuqHADWw+dAFspMXzEqXBaFq3g8HVsOZfQCuQZL2QfA32AMTAVmLq7PgNpr4elmV82qXWEeVeqI4M4+b0rV+jBVKJEb1EpWNLh6jeBN0NppBxd00UxOMR3OubWIAfMGk5XhlowiHg5qgsIETN0TmU=:ReZ9HLnXzbCVvDz+lKfd7PIEJQi7CQ5mN2LMxC5IZoA=; _br_uid_2=uid%3D9587123903556%3Av%3D12.0%3Ats%3D1649266626599%3Ahc%3D402; _uetsid=e29fdfc0c9cb11eca160b303e1375430; _uetvid=268bbf80756511ec99edb56d6bb4e245; _derived_epik=dj0yJnU9OWNWOXpZdTY5MkQyclZPNVNPeERGcnNLcF9ubXRsVlUmbj0yb2hyM3hrSk4yTWQ2cXlzR2Q3cmlnJm09MSZ0PUFBQUFBR0p3WFc0JnJtPTEmcnQ9QUFBQUFHSndYVzQ; _clsk=oye3oc|1651531119333|24|0|l.clarity.ms/collect; s_sq=sfsafewayprod1%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsafeway%25253Adelivery%25253Aaisles%25253Apet-care%25253Adog-care%2526link%253DSmall%252520Animal%252520Care%2526region%253DshopFlyOutModal%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsafeway%25253Adelivery%25253Aaisles%25253Apet-care%25253Adog-care%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.safeway.com%25252Fshop%25252Faisles%25252Fpet-care%25252Fsmall-animal-care.3132.html%2526ot%253DA; nlbi_1610353_2147483392=7dKCZSriyS/RG+Kf6eNT2gAAAAA2PImGUsiAKrnHkGtnQ+lV; mbox=PC#9b6c5b75050b44f89bb0e0946900cf45.35_0#1714776010|session#ff976e21c4e246ef811c922e86f4e099#1651533070; s_nr30=1651531209121-Repeat; gpv_Page=safeway%3Adelivery%3Aaisles%3Apet-care%3Asmall-animal-care; ADRUM_BT1=R%3A85%7Ci%3A3313187%7Ce%3A176%7Cd%3A271; ADRUM_BTa=R%3A85%7Cg%3Ad3dfc1e8-aca5-4e9a-8423-aba84b07701b%7Cn%3Asafeway-loyalty_d99a98d0-07cc-4871-98b7-0beac77d0580; SameSite=None; nlbi_1610353=e29bOv/T8kQZLTOE6eNT2gAAAADs7+HMWPJtn78YdHOxnL6O; visid_incap_1610353=EjDbpG8oRQ2swTN7o/8MWKvJUWIAAAAAQUIPAAAAAAAWPH6+Feg0fTaOdEPdTY+I',
  'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
  'referer': 'https://www.safeway.com/shop/aisles/pet-care/small-animal-care.3132.html?sort=&page=1',
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
  prods = prods.drop(columns=['sellByWeight','aisleName', 'prop65WarningIconRequired', 'departmentName', 'pid', 'aisleId', 'upc', 'restrictedValue', 'displayType', 'averageWeight', 'salesRank', 'id', 'featured', 'inventoryAvailable', 'pastPurchased', 'promoDescription', 'promoType', 'isArProduct', 'displayUnitQuantityText', 'promoEndDate', 'isMtoProduct', 'displayEstimateText', 'channelEligibility.delivery', 'channelEligibility.inStore', 'channelEligibility.pickUp', 'channelInventory.delivery', 'channelInventory.pickup', 'channelInventory.instore', 'preparationTime', 'unitQuantity', 'basePrice'], axis=1)
  # prods.to_csv('Safeway-Baby' + str(fileName) + '.csv')
  
  DB = {'servername': '(localdb)\MSSQLLocalDB',
      'database': 'Safeway',
      'driver': 'driver=SQL Server Native Client 11.0'}

  engine = create_engine('mssql+pyodbc://' + DB['servername'] + '/' + DB['database'] + "?" + DB['driver'])

# add table to sql server
  prods.to_sql("PetCare" + tableName, index=False, con=engine)

  # write the DataFrame to a table in the sql database