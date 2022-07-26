#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 14:02:02 2022

@author: dylanelder
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}


data = {
        'player_name': [],
        'Roto Teams': [],
        'status': [],
        
        }


full_data = pd.read_csv('fulljoin125.csv')

print(full_data)


def getInjuries():
    url = 'https://www.rotoballer.com/daily-nba-injury-roundup-for-april-10th-2022'
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

df2 = pd.read_csv('raptortest35.csv')
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



join_preseason = join_preseason[['Game ID', 'DK Teams', 'Questionable List_y', 'Number of Questionable_y', 'Questionable Raptor_y', 'Injury List_y', 'Number of Injuries_y', 'Out Raptor_y']]

print(join_preseason)

join_preseason.to_excel('NBA Injuries Yesterday.xlsx')




