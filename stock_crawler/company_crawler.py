import requests 
from bs4 import BeautifulSoup
import pandas as pd 

market_types=["1", "2", "3", "5", "7", "A", "C", "M"]

for market_type in market_types:
    url=f"https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market={market_type}&issuetype=&industry_code=&Page=1&chklike=Y"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml") 

    whole_table = soup.findAll('tr')
    print(f"market type :{market_type}, number of rows: {len(whole_table)-1}")

    cols=[]
    for col in whole_table:
        data = [td.get_text() for td in col.findAll("td")]
        cols.append(data)

    company_df=pd.DataFrame(cols[1:],columns=cols[0])
    print(company_df.head())
    company_df.to_csv(f"output_market{market_type}.csv", index=False)



