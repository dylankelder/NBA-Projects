#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:29:16 2022

@author: dylanelder
"""




import requests
from bs4 import BeautifulSoup
import pandas as pd



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}

EFG = {
        'Teams': [],
        '2022 EFG': [],
        'Last3 EFG': [],
        'Last1 EFG': [],
        'Home EFG': [],
        'Away EFG': [],
        'Date': []
        
        }



def getEFG(year, month, day):
    url = f'https://www.teamrankings.com/nba/stat/effective-field-goal-pct?date={year}-{month}-{day}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    
    for x in range (0,30):
        x = url
        x = x.split('=')
        
        y = x[1]
        EFG['Date'].append(y)

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')
            
            
        EFG['Teams'].append(td[1].text)
        EFG['2022 EFG'].append(td[2].text)
        EFG['Last3 EFG'].append(td[3].text)
        EFG['Last1 EFG'].append(td[4].text)
        EFG['Home EFG'].append(td[5].text)
        EFG['Away EFG'].append(td[6].text)
        
    return


month = oct(1)

for month in range (1, 5):
    date = oct(1)
    
    if  month == 1:
        for date in range (1, 32):
            getEFG('2022', month, date)
            
    elif  month == 2:
        for date in range (1, 29):
            getEFG('2022', month, date)
            
    elif  month == 3:
        for date in range (1, 32):
            getEFG('2022', month, date)
            
    elif  month == 4:
        for date in range (1, 11):
            getEFG('2022', month, date)
            


df_EFG = pd.DataFrame(EFG)


print(df_EFG)



df_EFG.to_excel('2022_Daily_EFG.xlsx')





