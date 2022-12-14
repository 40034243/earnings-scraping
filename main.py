#ticker CIK
from ast import Num
from matplotlib import ticker
import yahoo_fin.stock_info as si
import requests
import pandas as pd
final_ticker = 'AAPL'


import re, requests
headers = {"user-agent": "Safari"}

def getCIKs(TICKERS):
    URL = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
    CIK_RE = re.compile(r'.*CIK=(\d{10}).*')    
    cik_dict = {}
    for ticker in TICKERS:
        f = requests.get(URL.format(ticker),headers= headers, stream = True)
        results = CIK_RE.findall(f.text)
        if len(results):
            results[0] = int(re.sub('\.[0]*', '.', results[0]))
            cik_dict[str(ticker).upper()] = str(results[0])
    f = open('cik_dict', 'w')
    f.close()
    return(cik_dict)


final = getCIKs(([final_ticker]))

for i in final:
    CIKnum = (final[i])

num_of_zeros = 10 - len(CIKnum)


if num_of_zeros == 4:
    CIK = "0000" + CIKnum
    
if num_of_zeros == 5:
    CIK = "00000" + CIKnum
    
if num_of_zeros == 3:
    CIK = "000" + CIKnum


import requests
import pandas as pd
headers = {'User-Agent': "zachhefferman@gmail.com"}
tickers_cik = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers)
response1 = requests.get("https://data.sec.gov/api/xbrl/companyconcept/CIK" + CIK + "/us-gaap/EarningsPerShareDiluted.json", headers=headers).json()
final = (response1.get('units').get('USD/shares')[-1].get('val'))


aapl_earnings_hist = si.get_earnings_history(final_ticker)
estimatedEPS = aapl_earnings_hist[4].get('epsestimate')
print("Estimated:", estimatedEPS)

if final >= (2 * estimatedEPS):
    final = (response1.get('units').get('USD/shares')[-2].get('val'))
    print('Reported:', final)
else:
    print('Reported:', final)

if final > estimatedEPS:
    print("Opportunity!")
else:
    print("No opportunity...")




#add a revenue side, to the eps


'''import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=PAYX&apikey=0UPLO7L4EVYB34Q7'
r = requests.get(url)
data = r.json()

print(data)'''
