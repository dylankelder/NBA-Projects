#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:02:07 2022

@author: dylanelder
"""



import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}

df2 = pd.read_csv(r'/Users/dylanelder/Downloads/latest_RAPTOR_by_team (89).csv')

pdiff = {
        'TR Teams': [],
        '2021 PD': [],
        'Last1 PD': [],
        
        }

efg = {
        'TR Teams': [],
        '2021 EFG': [],

        }

reb = {
        'TR Teams': [],
        #'2021 REB': [],
        'Last3 REB': [],
        'Last1 REB': [],
        
        }

ast = {
        'TR Teams': [],
        '2021 AST': [],
        
        }

to = {
        'TR Teams': [],
        '2021 TO': [],
        'Last1 TO': [],
        
        }

ft = {
        'TR Teams': [],
        '2021 FT': [],
        
        
        
        }

oreb = {
        'TR Teams': [],
        '2021 OREB': [],
        
        }

pointspaint = {
        'TR Teams': [],
        'Last1 Points Paint': [],
        
        }

fouls = {
        'TR Teams': [],
        'Last3 Fouls': [],
        
        }

pointsfromFT = {
        'TR Teams': [],
        'Last1 % Points From FT': [],
        
        }

floor = {
        'TR Teams': [],
        '2021 Floor': [],
        'Last3 Floor': [],
        'Last1 Floor': [],
        
        }

opponentEFG = {
        'TR Teams': [],
        '2021 Opponent EFG': [],
        
        }

fastbreak = {
        'TR Teams': [],
        '2021 Fastbreak': [],
        'Last3 Fastbreak': [],
        
        }


odds = {
        'DK Teams': [],
        'spread': [],
        'ML': [],
        
        }

data = {
        'player_name': [],
        'Roto Teams': [],
        'status': [],
        
        }

def getOdds():
    url = 'https://sportsbook.draftkings.com/leagues/basketball/88670846'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    stat_table = soup.find('div', class_ = 'sportsbook-offer-category-card')

    for item in stat_table:
        rows = item.find_all('tr')

    for name in rows:
        name = name.find_all('div', class_ = 'event-cell__name-text')
        
        if name ==[]:
            continue
    
    
        odds['DK Teams'].append(name[0].text)

    for td in rows:
    
        td = td.find_all('span', class_ = 'sportsbook-outcome-cell__line')
        
        if td ==[]:
            continue

        odds['spread'].append(td[0].text)
        
    for ML in rows:
        ML = ML.find_all('span', class_ = 'sportsbook-odds american no-margin default-color')
        
        if ML ==[]:
            #ML = '0'
            continue
    
        odds['ML'].append(ML[0].text)
        
    return



def getPD():
    url = 'https://www.teamrankings.com/nba/stat/average-scoring-margin'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

        
    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')
            
            
        pdiff['TR Teams'].append(td[1].text)
        pdiff['2021 PD'].append(td[2].text)
        pdiff['Last1 PD'].append(td[4].text)
        
        
    return


def getEFG():
    url = 'https://www.teamrankings.com/nba/stat/effective-field-goal-pct'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
     

        
    table = soup.find('tbody')
    rows = table.find_all('tr')
    

    for td in rows:
        td = td.find_all('td')
            
        efg['TR Teams'].append(td[1].text)    
        efg['2021 EFG'].append(td[2].text)
        
        
    return




def getREB():
    url = 'https://www.teamrankings.com/nba/stat/total-rebounding-percentage'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
        
    table = soup.find('tbody')
    rows = table.find_all('tr')
    
    for td in rows:
        td = td.find_all('td')
            
        reb['TR Teams'].append(td[1].text)
        reb['Last3 REB'].append(td[3].text)
        reb['Last1 REB'].append(td[4].text)
       
        
    return







def getAST():
    url = 'https://www.teamrankings.com/nba/stat/assist--per--turnover-ratio'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
     
    
        
    table = soup.find('tbody')
    rows = table.find_all('tr')

    
    for td in rows:
        td = td.find_all('td')
            
        ast['TR Teams'].append(td[1].text)    
        ast['2021 AST'].append(td[2].text)
        
        
    return


def getTO():
    url = 'https://www.teamrankings.com/nba/stat/turnovers-per-possession'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
     

    table = soup.find('tbody')
    rows = table.find_all('tr')

    
    for td in rows:
        td = td.find_all('td')
            
        to['TR Teams'].append(td[1].text)    
        to['2021 TO'].append(td[2].text)
        to['Last1 TO'].append(td[4].text)
        
        
    return


def getFT():
    url = 'https://www.teamrankings.com/nba/stat/free-throw-rate'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
     
    
        
    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')
            
        ft['TR Teams'].append(td[1].text)    
        ft['2021 FT'].append(td[2].text)
        
        
    return

def getOREB():
    url = 'https://www.teamrankings.com/nba/stat/offensive-rebounding-pct'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find('tbody')
    rows = table.find_all('tr')
    
    for td in rows:
        td = td.find_all('td')
            
        oreb['TR Teams'].append(td[1].text)    
        oreb['2021 OREB'].append(td[2].text)
        
        
    return

def getPointsPaint():
    url = 'https://www.teamrankings.com/nba/stat/points-in-paint-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

        
    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')
            
        pointspaint['TR Teams'].append(td[1].text)    
        pointspaint['Last1 Points Paint'].append(td[4].text)
        
        
    return

def getFouls():
    url = 'https://www.teamrankings.com/nba/stat/personal-fouls-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find('tbody')
    rows = table.find_all('tr')
    

    for td in rows:
        td = td.find_all('td')
            
        fouls['TR Teams'].append(td[1].text)    
        fouls['Last3 Fouls'].append(td[3].text)
        
        
    return

def getPointsFromFT():
    url = 'https://www.teamrankings.com/nba/stat/percent-of-points-from-free-throws'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    
    for td in rows:
        td = td.find_all('td')
            
        pointsfromFT['TR Teams'].append(td[1].text)    
        pointsfromFT['Last1 % Points From FT'].append(td[4].text)
        
        
    return

def getFloor():
    url = 'https://www.teamrankings.com/nba/stat/floor-percentage'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
     
    
        
    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')
            
        floor['TR Teams'].append(td[1].text)
        floor['2021 Floor'].append(td[2].text)
        floor['Last3 Floor'].append(td[3].text)
        floor['Last1 Floor'].append(td[4].text)
        
        
    return

def getOpponentEFG():
    url = 'https://www.teamrankings.com/nba/stat/opponent-effective-field-goal-pct'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
     
    
        
    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')
            
        opponentEFG['TR Teams'].append(td[1].text)
        opponentEFG['2021 Opponent EFG'].append(td[2].text)
        
        
    return

def getFastbreak():
    url = 'https://www.teamrankings.com/nba/stat/fastbreak-points-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
     
    
        
    table = soup.find('tbody')
    rows = table.find_all('tr')

    
    for td in rows:
        td = td.find_all('td')
            
        fastbreak['TR Teams'].append(td[1].text)
        fastbreak['2021 Fastbreak'].append(td[2].text)
        fastbreak['Last3 Fastbreak'].append(td[3].text)
        
    return



getOdds()
getPD()
getEFG()
getREB()
getAST()
getTO()
getFT()
getOREB()
getPointsPaint()
getFouls()
getPointsFromFT()
getFloor()
getOpponentEFG()
getFastbreak()



df_odds = pd.DataFrame(odds)
df_pd = pd.DataFrame(pdiff)
df_efg = pd.DataFrame(efg)
df_reb = pd.DataFrame(reb)
df_ast = pd.DataFrame(ast)
df_to = pd.DataFrame(to)
df_ft = pd.DataFrame(ft)
df_oreb = pd.DataFrame(oreb)
df_pointspaint = pd.DataFrame(pointspaint)
df_fouls = pd.DataFrame(fouls)
df_pointsfromFT = pd.DataFrame(pointsfromFT)
df_floor = pd.DataFrame(floor)
df_opponentEFG = pd.DataFrame(opponentEFG)
df_fastbreak = pd.DataFrame(fastbreak)

df_odds.spread[df_odds.spread == 'pk'] = 0



df_target = pd.DataFrame({'TR Teams':['Phoenix', 'Golden State', 'Utah', 'Boston', 'Miami', 'Memphis', 'Milwaukee', 'Cleveland', 'Dallas', 'Denver', 'Philadelphia', 'Minnesota', 'Chicago', 'Toronto', 'Atlanta', 'San Antonio', 'Charlotte', 'LA Clippers', 'Brooklyn', 'New Orleans', 'New York', 'LA Lakers', 'Indiana', 'Washington', 'Sacramento', 'Portland', 'Okla City', 'Orlando', 'Detroit', 'Houston']})


df_odds_target = pd.DataFrame({'DK Teams':['PHO Suns', 'GS Warriors', 'UTA Jazz', 'BOS Celtics', 'MIA Heat', 'MEM Grizzlies', 'MIL Bucks', 'CLE Cavaliers', 'DAL Mavericks', 'DEN Nuggets', 'PHI 76ers', 'MIN Timberwolves', 'CHI Bulls', 'TOR Raptors', 'ATL Hawks', 'SA Spurs', 'CHA Hornets', 'LA Clippers', 'BKN Nets', 'NO Pelicans', 'NY Knicks', 'LA Lakers', 'IND Pacers', 'WAS Wizards', 'SAC Kings', 'POR Trail Blazers', 'OKC Thunder', 'ORL Magic', 'DET Pistons', 'HOU Rockets'],
                               'TR Teams:': ['Phoenix', 'Golden State', 'Utah', 'Boston', 'Miami', 'Memphis', 'Milwaukee', 'Cleveland', 'Dallas', 'Denver', 'Philadelphia', 'Minnesota', 'Chicago', 'Toronto', 'Atlanta', 'San Antonio', 'Charlotte', 'LA Clippers', 'Brooklyn', 'New Orleans', 'New York', 'LA Lakers', 'Indiana', 'Washington', 'Sacramento', 'Portland', 'Okla City', 'Orlando', 'Detroit', 'Houston']})


df_odds_target2 = pd.DataFrame({'DK Teams':['PHO Suns', 'GS Warriors', 'UTA Jazz', 'BOS Celtics', 'MIA Heat', 'MEM Grizzlies', 'MIL Bucks', 'CLE Cavaliers', 'DAL Mavericks', 'DEN Nuggets', 'PHI 76ers', 'MIN Timberwolves', 'CHI Bulls', 'TOR Raptors', 'ATL Hawks', 'SA Spurs', 'CHA Hornets', 'LA Clippers', 'BKN Nets', 'NO Pelicans', 'NY Knicks', 'LA Lakers', 'IND Pacers', 'WAS Wizards', 'SAC Kings', 'POR Trail Blazers', 'OKC Thunder', 'ORL Magic', 'DET Pistons', 'HOU Rockets']})

df_odds_target3 = pd.DataFrame({'TR Teams:': ['Phoenix', 'Golden State', 'Utah', 'Boston', 'Miami', 'Memphis', 'Milwaukee', 'Cleveland', 'Dallas', 'Denver', 'Philadelphia', 'Minnesota', 'Chicago', 'Toronto', 'Atlanta', 'San Antonio', 'Charlotte', 'LA Clippers', 'Brooklyn', 'New Orleans', 'New York', 'LA Lakers', 'Indiana', 'Washington', 'Sacramento', 'Portland', 'Okla City', 'Orlando', 'Detroit', 'Houston'],
                               'DK Teams':['PHO Suns', 'GS Warriors', 'UTA Jazz', 'BOS Celtics', 'MIA Heat', 'MEM Grizzlies', 'MIL Bucks', 'CLE Cavaliers', 'DAL Mavericks', 'DEN Nuggets', 'PHI 76ers', 'MIN Timberwolves', 'CHI Bulls', 'TOR Raptors', 'ATL Hawks', 'SA Spurs', 'CHA Hornets', 'LA Clippers', 'BKN Nets', 'NO Pelicans', 'NY Knicks', 'LA Lakers', 'IND Pacers', 'WAS Wizards', 'SAC Kings', 'POR Trail Blazers', 'OKC Thunder', 'ORL Magic', 'DET Pistons', 'HOU Rockets']})



inner_join_odds = pd.merge(df_odds,
                           df_odds_target,
                           on = 'DK Teams',
                           how = 'left')



inner_join1 = pd.merge(df_target,
                      df_pd,
                      on = 'TR Teams',
                      how = 'left')


inner_join2 = pd.merge(inner_join1,
                       df_efg,
                       on = 'TR Teams',
                       how = 'left')




inner_join3 = pd.merge(inner_join2,
                       df_reb,
                       on = 'TR Teams',
                       how = 'left')



inner_join4 = pd.merge(inner_join3,
                       df_ast,
                       on = 'TR Teams',
                       how = 'left')

inner_join5 = pd.merge(inner_join4,
                       df_to,
                       on = 'TR Teams',
                       how = 'left')

inner_join6 = pd.merge(inner_join5,
                       df_ft,
                       on = 'TR Teams',
                       how = 'left')

inner_join7 = pd.merge(inner_join6,
                       df_oreb,
                       on = 'TR Teams',
                       how = 'left')

playoff_join1 = pd.merge(inner_join7,
                       df_pointspaint,
                       on = 'TR Teams',
                       how = 'left')

playoff_join2 = pd.merge(playoff_join1,
                       df_fouls,
                       on = 'TR Teams',
                       how = 'left')

playoff_join3 = pd.merge(playoff_join2,
                       df_pointsfromFT,
                       on = 'TR Teams',
                       how = 'left')

playoff_join4 = pd.merge(playoff_join3,
                       df_floor,
                       on = 'TR Teams',
                       how = 'left')

playoff_join5 = pd.merge(playoff_join4,
                       df_opponentEFG,
                       on = 'TR Teams',
                       how = 'left')

playoff_join6 = pd.merge(playoff_join5,
                       df_fastbreak,
                       on = 'TR Teams',
                       how = 'left')






df_fouls = pd.DataFrame(fouls)
df_pointsfromFT = pd.DataFrame(pointsfromFT)
df_floor = pd.DataFrame(floor)
df_opponentEFG = pd.DataFrame(opponentEFG)
df_fastbreak = pd.DataFrame(fastbreak)



inner_join_odds = inner_join_odds.set_index('TR Teams:')


full_data = pd.merge(inner_join_odds, playoff_join6, left_index=True, right_on='TR Teams') 

full_data.drop_duplicates(subset = 'DK Teams',
                          keep = 'first', inplace = True)







def getInjuries():
    url = 'https://www.rotoballer.com/daily-nba-injury-roundup-for-may-27th-2022'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    injury_table = soup.find('table', class_ = 'marianExclude')
    
    
    
    for player in injury_table.find_all('tbody'):
        rows = player.find_all('tr')
        
        for row in rows:
            all_players = row.find_all('td')
            
            data['player_name'].append(all_players[0].text)
            data['Roto Teams'].append(all_players[1].text)
            data['status'].append(all_players[2].text)
            


getInjuries()

df_injury = pd.DataFrame(data)

new = df_injury['status'].str.split(' ', n = 1, expand = True)
    
df_injury['StatusType'] = new[0]

df_injury.drop(columns = ['status'], inplace  = True)



df2 = df2.drop(df2.columns[[1,2,3,5,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22]], axis=1)



join_raptor = pd.merge(df_injury,
                     df2,
                     on = 'player_name',
                     how = 'left')


join_raptor.drop(join_raptor.index[join_raptor['mp'] < 900], inplace=True)
join_raptor.drop(join_raptor.index[join_raptor['StatusType'] == 'Probable'], inplace=True)

join_raptor = join_raptor.dropna()



def NewRaptor(row):
    if row['raptor_total'] < 0:
        val = 0
        
    elif row['raptor_total'] > 0:
        val = -row['raptor_total']
        
    return val

join_raptor['New Raptor'] = join_raptor.apply(NewRaptor, axis = 1)

print(join_raptor)

def OutRaptor(row):
    if row['StatusType'] == 'Out':
        global newVal
        newVal = row['New Raptor']
        
    elif row['StatusType'] == 'Doubtful':
        newVal = row['New Raptor']
        
        
    elif row['StatusType'] == 'Questionable':
        newVal = 0
        
    return newVal

join_raptor['Out Raptor'] = join_raptor.apply(OutRaptor, axis = 1)


def QuestionableRaptor(row):
    if row['StatusType'] == 'Questionable':
        global newVal2
        newVal2 = row['New Raptor']
        
    elif row['StatusType'] == 'Out':
        newVal2 = 0
        
    elif row['StatusType'] != 'Questionable':
        newVal2 = 0
        
        
    return newVal2




join_raptor['Questionable Raptor'] = join_raptor.apply(QuestionableRaptor, axis = 1)






df_target1 = pd.DataFrame({'Roto Teams': ['PHO', 'GS', 'UTA', 'BOS', 'MIA', 'MEM', 'MIL', 'CLE', 'DAL', 'DEN', 'PHI', 'MIN', 'CHI', 'TOR', 'ATL', 'SA', 'CHA', 'LAC', 'BKN', 'NO', 'NY', 'LAL', 'IND', 'WAS', 'SAC', 'POR', 'OKC', 'ORL', 'DET', 'HOU'],
                               'DK Teams':['PHO Suns', 'GS Warriors', 'UTA Jazz', 'BOS Celtics', 'MIA Heat', 'MEM Grizzlies', 'MIL Bucks', 'CLE Cavaliers', 'DAL Mavericks', 'DEN Nuggets', 'PHI 76ers', 'MIN Timberwolves', 'CHI Bulls', 'TOR Raptors', 'ATL Hawks', 'SA Spurs', 'CHA Hornets', 'LA Clippers', 'BKN Nets', 'NO Pelicans', 'NY Knicks', 'LA Lakers', 'IND Pacers', 'WAS Wizards', 'SAC Kings', 'POR Trail Blazers', 'OKC Thunder', 'ORL Magic', 'DET Pistons', 'HOU Rockets']})



join_games = pd.merge(full_data,
                      df_target1,
                      on = 'DK Teams',
                      how = 'left')



num_injuries = join_raptor.StatusType == 'Out'
num_doubtful = join_raptor.StatusType =='Doubtful'
num_total_injuries = num_injuries | num_doubtful
risk_df = pd.concat([num_total_injuries], axis=1)



num_questionable = join_raptor.StatusType == 'Questionable'
risk2_df = pd.concat([num_questionable], axis=1)



player_injuries = join_raptor.player_name




join_raptor['Number of Injuries'] = risk_df.sum(axis=1)
join_raptor['Number of Questionable'] = risk2_df.sum(axis=1)


def PlayerOut(row):
    if row['StatusType'] == 'Out':
        global player_out
        player_out = row['player_name']
    
    elif row['StatusType'] == 'Doubtful':
        player_out = row['player_name']
        
        
    elif row['StatusType'] == 'Questionable':
        player_out = 0
        
    return player_out

join_raptor['Player Injuries'] = join_raptor.apply(PlayerOut, axis = 1)



def PlayerQuestionable(row):
    if row['StatusType'] == 'Questionable':
        global player_questionable
        player_questionable = row['player_name']
        
        
    elif row['StatusType'] == 'Out':
        player_questionable = 0
        
    elif row['StatusType'] != 'Questionable':
        player_questionable = 0
        
    return player_questionable


join_raptor['Player Questionable'] = join_raptor.apply(PlayerQuestionable, axis = 1)





pregrouped = join_raptor['Roto Teams']
grouper = join_raptor[['Roto Teams', 'Player Injuries']]



full = pd.merge(pregrouped,
                grouper,
                on = 'Roto Teams',
                how = 'left')



full.groupby('Roto Teams')['Player Injuries'].apply(list)

full2 = full.groupby('Roto Teams')['Player Injuries'].apply(list).reset_index(name='new')

full2['Injury List'] = full2['new']
full2['Injury List'] = full2['new'].map(lambda x: list(set(x)))





grouper2 = join_raptor[['Roto Teams', 'Player Questionable']]

full3 = pd.merge(pregrouped,
                 grouper2,
                 on = 'Roto Teams',
                 how = 'left')

full3.groupby('Roto Teams')['Player Questionable'].apply(list)

full4 = full3.groupby('Roto Teams')['Player Questionable'].apply(list).reset_index(name='new1')
full4['Questionable List'] = full4['new1']
full4['Questionable List'] = full4['new1'].map(lambda x: list(set(x)))



full5 = pd.merge(full2,
                 full4,
                 on = 'Roto Teams',
                 how = 'left')

full5 = full5.drop(full5.columns[[1,3]], axis=1)



df3 = join_raptor.groupby(['Roto Teams']).sum()
df3.merge(join_raptor, on= 'Roto Teams', how = 'left')
df3.reset_index(inplace=True)
df3 = df3.drop(df3.columns[[1,2,3]], axis = 1)
df3 = df3[['Roto Teams', 'Number of Questionable', 'Questionable Raptor', 'Number of Injuries', 'Out Raptor']]




Q_column = full5['Questionable List']
I_column = full5['Injury List']

df3 = pd.concat([df3,Q_column], axis =1)
df3 = pd.concat([df3, I_column], axis =1)

join_games = join_games.set_index('Roto Teams')

full_join = join_games.merge(df3, how = 'left', left_on = 'Roto Teams', right_on = 'Roto Teams')
full_join = full_join.drop(full_join.columns[[0,4]], axis = 1)
full_join['Will This Player Play?'] = np.nan



full_join = full_join[['DK Teams', 'spread', 'ML', 'Questionable List', 'Number of Questionable', 'Questionable Raptor', 'Will This Player Play?', 'Injury List', 'Number of Injuries', 'Out Raptor', '2021 PD', 'Last1 PD', '2021 EFG', 'Last3 REB', '2021 AST', '2021 TO', 'Last1 TO', '2021 FT', '2021 OREB', 'Last1 Points Paint', 'Last3 Fouls', 'Last1 % Points From FT', '2021 Floor', 'Last3 Floor', 'Last1 Floor', 'Last1 REB', '2021 Fastbreak', 'Last3 Fastbreak', '2021 Opponent EFG']]


preseason_target = pd.DataFrame({'DK Teams':['PHO Suns', 'GS Warriors', 'UTA Jazz', 'BOS Celtics', 'MIA Heat', 'MEM Grizzlies', 'MIL Bucks', 'CLE Cavaliers', 'DAL Mavericks', 'DEN Nuggets', 'PHI 76ers', 'MIN Timberwolves', 'CHI Bulls', 'TOR Raptors', 'ATL Hawks', 'SA Spurs', 'CHA Hornets', 'LA Clippers', 'BKN Nets', 'NO Pelicans', 'NY Knicks', 'LA Lakers', 'IND Pacers', 'WAS Wizards', 'SAC Kings', 'POR Trail Blazers', 'OKC Thunder', 'ORL Magic', 'DET Pistons', 'HOU Rockets'],
                               'Preseason Win Totals': ['51.5', '48.5', '52.5', '46.5', '48.5', '42', '54.5', '27', '48.5', '48', '50.5', '35', '43', '36', '47', '29.5', '38.5', '44', '55.5', '38.5', '42', '52.5', '43', '34', '36.5', '44.5', '23.5', '22.5', '25.5', '27']})


join_preseason = pd.merge(full_join,
                      preseason_target,
                      on = 'DK Teams',
                      how = 'left')

game_id = []


team_rows = len(join_preseason['DK Teams'])

count = 0
count1 = 0

while (count1 < team_rows / 2):
    count = count + 1
    game_id.append(count)
    
    count1 = count1 + 1
    game_id.append(count1)
    


join_preseason['Game ID'] = game_id

print(join_preseason)


join_preseason['spread'] = pd.to_numeric(join_preseason['spread'])
join_preseason['ML'] = pd.to_numeric(join_preseason['ML'])
join_preseason['2021 PD'] = pd.to_numeric(join_preseason['2021 PD'])
join_preseason['Last1 PD'] = pd.to_numeric(join_preseason['Last1 PD'])
join_preseason['2021 EFG'] = join_preseason['2021 EFG'].str.rstrip('%').astype('float') / 100.0
join_preseason['Last3 REB'] = join_preseason['Last3 REB'].str.rstrip('%').astype('float') / 100.0
join_preseason['2021 TO'] = join_preseason['2021 TO'].str.rstrip('%').astype('float') / 100.0
join_preseason['Last1 TO'] = join_preseason['Last1 TO'].str.rstrip('%').astype('float') / 100.0
join_preseason['2021 FT'] = join_preseason['2021 FT'].str.rstrip('%').astype('float') / 100.0
join_preseason['2021 AST'] = pd.to_numeric(join_preseason['2021 AST'])
join_preseason['2021 OREB'] = join_preseason['2021 OREB'].str.rstrip('%').astype('float') / 100.0


join_preseason = join_preseason[['Game ID', 'DK Teams', 'spread', 'ML', 'Questionable List', 'Number of Questionable', 'Questionable Raptor', 'Will This Player Play?', 'Injury List', 'Number of Injuries', 'Out Raptor', 'Preseason Win Totals', '2021 PD', 'Last1 PD', '2021 EFG', 'Last3 REB', '2021 AST', '2021 TO', 'Last1 TO', '2021 FT', '2021 OREB', 'Last1 Points Paint', 'Last3 Fouls', 'Last1 % Points From FT', '2021 Floor', 'Last3 Floor', 'Last1 Floor', 'Last1 REB', '2021 Fastbreak', 'Last3 Fastbreak', '2021 Opponent EFG']]


join_preseason['2021 PD Diff.1'] = join_preseason.groupby('Game ID')['2021 PD'].diff(periods=-1)
join_preseason['2021 PD Diff.2'] = join_preseason.groupby('Game ID')['2021 PD'].diff(periods=1)
join_preseason[['2021 PD Diff.1', '2021 PD Diff.2']] = pd.DataFrame(np.sort(join_preseason[['2021 PD Diff.1', '2021 PD Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])


join_preseason['Last1 PD Diff.1'] = join_preseason.groupby('Game ID')['Last1 PD'].diff(periods=-1)
join_preseason['Last1 PD Diff.2'] = join_preseason.groupby('Game ID')['Last1 PD'].diff(periods=1)
join_preseason[['Last1 PD Diff.1', 'Last1 PD Diff.2']] = pd.DataFrame(np.sort(join_preseason[['Last1 PD Diff.1', 'Last1 PD Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])


join_preseason['2021 EFG Diff.1'] = join_preseason.groupby('Game ID')['2021 EFG'].diff(periods=-1)
join_preseason['2021 EFG Diff.2'] = join_preseason.groupby('Game ID')['2021 EFG'].diff(periods=1)
join_preseason[['2021 EFG Diff.1', '2021 EFG Diff.2']] = pd.DataFrame(np.sort(join_preseason[['2021 EFG Diff.1', '2021 EFG Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])

join_preseason['Last3 REB Diff.1'] = join_preseason.groupby('Game ID')['Last3 REB'].diff(periods=-1)
join_preseason['Last3 REB Diff.2'] = join_preseason.groupby('Game ID')['Last3 REB'].diff(periods=1)
join_preseason[['Last3 REB Diff.1', 'Last3 REB Diff.2']] = pd.DataFrame(np.sort(join_preseason[['Last3 REB Diff.1', 'Last3 REB Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])

join_preseason['2021 TO Diff.1'] = join_preseason.groupby('Game ID')['2021 TO'].diff(periods=-1)
join_preseason['2021 TO Diff.2'] = join_preseason.groupby('Game ID')['2021 TO'].diff(periods=1)
join_preseason[['2021 TO Diff.1', '2021 TO Diff.2']] = pd.DataFrame(np.sort(join_preseason[['2021 TO Diff.1', '2021 TO Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])

join_preseason['Last1 TO Diff.1'] = join_preseason.groupby('Game ID')['Last1 TO'].diff(periods=-1)
join_preseason['Last1 TO Diff.2'] = join_preseason.groupby('Game ID')['Last1 TO'].diff(periods=1)
join_preseason[['Last1 TO Diff.1', 'Last1 TO Diff.2']] = pd.DataFrame(np.sort(join_preseason[['Last1 TO Diff.1', 'Last1 TO Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])

join_preseason['2021 FT Diff.1'] = join_preseason.groupby('Game ID')['2021 FT'].diff(periods=-1)
join_preseason['2021 FT Diff.2'] = join_preseason.groupby('Game ID')['2021 FT'].diff(periods=1)
join_preseason[['2021 FT Diff.1', '2021 FT Diff.2']] = pd.DataFrame(np.sort(join_preseason[['2021 FT Diff.1', '2021 FT Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])

join_preseason['2021 OREB Diff.1'] = join_preseason.groupby('Game ID')['2021 OREB'].diff(periods=-1)
join_preseason['2021 OREB Diff.2'] = join_preseason.groupby('Game ID')['2021 OREB'].diff(periods=1)
join_preseason[['2021 OREB Diff.1', '2021 OREB Diff.2']] = pd.DataFrame(np.sort(join_preseason[['2021 OREB Diff.1', '2021 OREB Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])


replacement_player_weight = -0.25

join_preseason['Replacement Player Values'] = join_preseason['Number of Injuries'] * replacement_player_weight

raptor_injury_loss = 0.5
replacement_weight_on_spread = -0.5

join_preseason['Total Injury Values'] = (join_preseason['Out Raptor'] * raptor_injury_loss) - (join_preseason['Replacement Player Values'] * replacement_weight_on_spread)
join_preseason['Total Injury Values'] = join_preseason['Total Injury Values'].fillna(0)


join_preseason['Injury Diff.1'] = join_preseason.groupby('Game ID')['Total Injury Values'].diff(periods=-1)
join_preseason['Injury Diff.2'] = join_preseason.groupby('Game ID')['Total Injury Values'].diff(periods=1)
join_preseason[['Injury Diff.1', 'Injury Diff.2']] = pd.DataFrame(np.sort(join_preseason[['Injury Diff.1', 'Injury Diff.2']].values, axis = 1))
join_preseason.groupby(['Game ID'])


home_away = []
home_away_rows = len(join_preseason['DK Teams'])

away_count = 0
home_count = 0

while (home_count < home_away_rows / 2):
    away_count = away_count + 1
    away_status = 'Away'
    home_away.append(away_status)
    
    home_count = home_count +1
    home_status = 'Home'
    home_away.append(home_status)
    


join_preseason['Home/Away'] = home_away


def LocationValue(row):
    if row['Home/Away'] == 'Away':
        locVal = 1.5
        
    elif row['Home/Away'] == 'Home':
        locVal = -1.5
        
    return locVal


join_preseason['Home/Away Value'] = join_preseason.apply(LocationValue, axis = 1)


print(join_preseason)

join_preseason.to_excel('fulljoin125.xlsx')





