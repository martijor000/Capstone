import requests
import json
import pandas as pd
import time
from sqlalchemy import create_engine, false, true


def WalmartRequest(updateURL, insertHeaders, insertPayload, tableName, categoryName): 
  for page in range(1, 100, 1):
    test = updateURL.replace("page=1", "page=" + str(page))
    newURL = f"{test}"
    r = requests.get(newURL, headers=insertHeaders, data=insertPayload)
    data = json.loads(r.text)
    if(r.ok == false):
        newData = data
        time.sleep(3)
        print(f'Getting row {page} of ' + categoryName + ' ' + tableName, 'waiting..')
    else:
      break
  
  # filteredData = []
  # # Filtering out duplicate data from our request by going through each object and seeing if its already in our filtered data object.
  # for x in newData:
  #   if x not in filteredData: 
  #     filteredData.append(x)
  prods = pd.DataFrame([])
  prods = prods.from_records(pd.json_normalize(data)) 
  #prods = prods.drop(columns=['sellByWeight','aisleName', 'prop65WarningIconRequired', 'departmentName', 'pid', 'aisleId', 'upc', 'restrictedValue', 'displayType', 'averageWeight', 'salesRank', 'id', 'featured', 'inventoryAvailable', 'pastPurchased', 'isArProduct', 'displayUnitQuantityText', 'promoEndDate', 'isMtoProduct', 'displayEstimateText', 'channelEligibility.delivery', 'channelEligibility.inStore', 'channelEligibility.pickUp', 'channelInventory.delivery', 'channelInventory.pickup', 'channelInventory.instore', 'preparationTime', 'unitQuantity', 'basePrice'], axis=1)
  prods.to_csv('Walmart' + str(categoryName) + '.csv')



#   DB = {'servername': '(localdb)\MSSQLLocalDB',
#       'database': 'Walmart',
#       'driver': 'driver=SQL Server Native Client 11.0'}


#   engine = create_engine('mssql+pyodbc://' + DB['servername'] + '/' + DB['database'] + "?" + DB['driver'])
#   engine.execute('DROP TABLE IF EXISTS ' + categoryName + tableName)

# # add table to sql server
#   prods.to_sql(categoryName + tableName, index=False, con=engine)
#   engine.execute("ALTER TABLE " + categoryName + tableName +  " ADD ID INT IDENTITY(1,1) not null CONSTRAINT PK_" + categoryName + tableName + " PRIMARY KEY(ID)")
#   # write the DataFrame to a table in the sql database
