#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:44:07 2022

@author: dylanelder
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

result = []


def getRefs(month, day):
    date_text = f'2022-{month}-{day}'

    log_url = 'https://official.nba.com/referee-assignments/'

    driver.get(log_url)
    link = driver.find_element_by_class_name('dropdown-toggle')
    link.click()


    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ref-date"]')))
    element.clear()
    element.click()

    driver.find_element_by_class_name('hasDatepicker').send_keys(date_text)
    element.submit()

    time.sleep(3)


    games = driver.find_elements_by_xpath('//*[@id="main"]/div/section[1]')



    for game in games:

        teams = game.find_elements_by_xpath('//*[@id="main"]/div/section[1]/article/div/div[1]/div/table/tbody/tr/td[1]')
        official1 = game.find_elements_by_xpath('//*[@id="main"]/div/section[1]/article/div/div[1]/div/table/tbody/tr/td[2]/a')
        official2 = game.find_elements_by_xpath('//*[@id="main"]/div/section[1]/article/div/div[1]/div/table/tbody/tr/td[3]/a')
        official3 = game.find_elements_by_xpath('//*[@id="main"]/div/section[1]/article/div/div[1]/div/table/tbody/tr/td[4]/a')
        date = game.find_element_by_xpath('//*[@id="main"]/div/section[1]/article/header/div').text


        for i in range(len(teams)):
            temporary_data = {'Team': teams[i].text,
                              'Official 1': official1[i].text,
                              'Official 2': official2[i].text,
                              'Official 3': official3[i].text,
                              'Date': date,
    
            
            }
    
            result.append(temporary_data)
            
        return
    
month = oct(1)

for month in range (1, 6):
    
    month = ("{:02d}".format(month))

    day = oct(1)
    
    
    if  month == '01':

        for day in range (6, 32):
            
            day = ("{:02d}".format(day))

            getRefs(month, day)
            
    elif  month == '02':

        for day in range (1, 29):
            day = ("{:02d}".format(day))
    
            getRefs(month, day)          

    elif  month == '03':

        for day in range (1, 32):
            day = ("{:02d}".format(day))
    
            getRefs(month, day)
            
            
    elif  month == '04':

        for day in range (1, 29):
            day = ("{:02d}".format(day))
    
            getRefs(month, day)
            
    elif  month == '05':

        for day in range (1, 10):
            day = ("{:02d}".format(day))
    
            getRefs(month, day)



df = pd.DataFrame(result)

print('Fin!')

df.to_excel('NBA Ref Data.xlsx')