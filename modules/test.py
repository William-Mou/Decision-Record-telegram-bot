import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import requests
# site = "https://query1.finance.yahoo.com/v8/finance/chart/" + str(self.stock) + \
#    ".TW?period1="+self.get_ts(0)+"&period2="+self.get_ts(-1) + \
#    "&interval=1d&events=history&=hP2rOschxO0"


def show_stock(stock, p1, p2, id):

    site = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock}.TW?period1={p1}&period2={p2}&interval=1d&events=history&=hP2rOschxO0"
    #site = "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=1545351086&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"

    response = requests.get(site)

    data = json.loads(response.text)
    df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(
        np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))
    fig = df.close.plot()
    fig.figure.savefig(str(id) + '_stock.png')
