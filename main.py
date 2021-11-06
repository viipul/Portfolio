
coins=['CoShi Inu','SafeMoon','Saitama','Pig Finance','Kishu Inu','Akita Inu']
coin_data={'CoShi Inu':[582651869,0.0000000214,12.46875],'SafeMoon':[1869791,0.000006,11.218746],'Saitama':[159855769.2,0.000000078,12.46875],'Pig Finance':[34202626,0.0000002485,12.46874992],'Kishu Inu':[1377762430,0.00000000905,12.46875],'Akita Inu':[2459804,0.000005069,12.46874648]}
symb=0
import time
import numpy as np 
import matplotlib.pyplot as plt 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


from IPython.display import display, clear_output
while (True):
    
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '9c34b744-7c3b-4acc-ab83-9469e4d594ef',
    }
    
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        e
  
    d=data['data']

    
   
    time.sleep(5) 
    invest=[]
    returnv=[]
    for i in coins:
        print("*********{}*********".format(i))
        for j in range(len(d)):
            if d[j]['name']==i:
                data=d[j]
                quantity=coin_data[i][0]
                avg_price=coin_data[i][1]
                invested=coin_data[i][2]
                rate=d[j]['quote']['USD']['price']
                curr=rate*quantity
                print("BOUGHT AT:",avg_price)
                print("CURRENT RATE:",rate)
                print("INVESTED VALUE:",round(invested,5))
                invest.append(invested)
                returnv.append(curr)
                print('CURRENT VALUE:',round(curr,5))
                per=round(100*((curr-invested)/invested),5)
                print('PROFIT/LOSS%:',per)
    X = coins
    Ygirls = invest
    Zboys = returnv

    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Invested')
    plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Current')

    plt.xticks(X_axis, X,rotation=45)
    plt.xlabel("Coins")
    plt.ylabel("Amount in USD")
    plt.title("Coins Current vs Invested")
    plt.legend()
    plt.show()
    clear_output(wait=True)



            
        
