import csv,yaml,os
import pandas as pd
import json
with open('player_map.json','r') as fd:
    player_map = json.load(fd)
yaml_list = os.listdir()
def make_reg(temp):
    if temp[1].islower():
        return temp
    temp=temp.split()
    reg=temp[0][0]+'.*'+temp[-1]
    return reg
def find_player(name,df):
    if name in player_map:
        k = player_map[name]
        player = df.filter(regex=k,axis = 0)
        return player.iloc[0]
    else:
        print(name)
        return -1
bats_cluster = pd.read_csv('batsman_cluster.csv',index_col='player_name')
bowl_cluster = pd.read_csv('bowler_cluster.csv',index_col='player_name')
with open('decisiontree_ballinfo.csv','w') as csvfile:
    fieldnames = ['batsman','nonstrike','bowler','runs','wickets','home','ave_score','sr','bowl_ave','bowl_sr','econ','innings','wickets']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    batsman_info = dict()
    bowler_info = dict()
    for num,yaml_file in enumerate(yaml_list):
        if 'yaml' in yaml_file:
            with open(yaml_file,"r") as stream:
                try:
                    yaml_dict = yaml.load(stream)
                except yaml.YAMLError as err:
                    print(err)
                team1 = yaml_dict['info']['teams'][0]
                for number,innings in enumerate(yaml_dict['innings']):
                    wickets=0
                    total = 0
                    innings_info = list(innings.values())[0]
                    if innings_info['team'] == team1:
                        home = 1
                    else:
                        home = 0
                    cur_over = 0
                    for ball in innings_info['deliveries']:
                        ball_info = list(ball.values())[0]
                        prev_over = cur_over
                        cur_over = int(list(ball.keys())[0])
                        print(cur_over,prev_over)
                        if prev_over!=cur_over:
                        	print(prev_over,{'batsman':batsman_info[batsman]['prediction'],'nonstrike':ball_info['non_striker'],'bowler':bowler_info[bowler]['prediction'],'out':out,'home':home,'ave_score':batsman_info[batsman]['ave_score'],'sr':batsman_info[batsman]['sr'],'bowl_ave':bowler_info[bowler]['bowl_ave'],'bowl_sr':bowler_info[bowler]['bowl_sr'],'econ':bowler_info[bowler]['econ'],'innings':number%2,'wickets':wickets,'runs':total})
                        	writer.writerow({'batsman':batsman_info[batsman]['prediction'],'nonstrike':batsman_info[nonstrike]['prediction'],'bowler':bowler_info[bowler]['prediction'],'runs':total,'wickets':wickets,'home':home,'ave_score':batsman_info[batsman]['ave_score'],'sr':batsman_info[batsman]['sr'],'bowl_ave':bowler_info[bowler]['bowl_ave'],'bowl_sr':bowler_info[bowler]['bowl_sr'],'econ':bowler_info[bowler]['econ'],'innings':number%2})
                        	total = 0
                        	wickets = 0
                        batsman = ball_info['batsman']
                        bowler = ball_info['bowler']
                        nonstrike=ball_info['non_striker']
                        if batsman not in batsman_info:
                            batsman_info[batsman] = find_player(batsman,bats_cluster)
                            if type(batsman_info[batsman]) == int:
                                temp_dict = {'prediction':0,'ave_score':18.161195652173927, 'sr':124.90467391304348, 'balls_faced':512.4130434782609, 'hundreds/innings':0.0003079888613018342, 'fifties/innings':0.03316629905487374, 'fours_rate':0.10561940238357537, 'six_rate':0.045928253202445646, 'vulnerability':0.08160455808205533}
                                batsman_info[batsman] = pd.Series(temp_dict)
                        if nonstrike not in batsman_info:
                            batsman_info[nonstrike] = find_player(nonstrike,bats_cluster)
                            if type(batsman_info[nonstrike]) == int:
                                temp_dict = {'prediction':0,'ave_score':18.161195652173927, 'sr':124.90467391304348, 'balls_faced':512.4130434782609, 'hundreds/innings':0.0003079888613018342, 'fifties/innings':0.03316629905487374, 'fours_rate':0.10561940238357537, 'six_rate':0.045928253202445646, 'vulnerability':0.08160455808205533}
                                batsman_info[nonstrike] = pd.Series(temp_dict)
                        if bowler not in bowler_info:
                            bowler_info[bowler] = find_player(bowler,bowl_cluster)
                            if type(bowler_info[bowler]) == int:
                                temp_dict = {'prediction':3, 'bowl_ave':27.86269230769231, 'econ':7.669653846153847, 'bowl_sr':21.53619230769231, 'balls':430.4730769230769}
                                bowler_info[bowler] = pd.Series(temp_dict)
                        runs = ball_info['runs']['batsman']
                        total+=runs
                        out = 0
                        if 'wicket' in ball_info and ball_info['wicket']['kind']!='run out':
                            out = 1
                            wickets+=1
                        # print(batsman_info[batsman][0])
                    print(batsman,nonstrike)
                    writer.writerow({'batsman':batsman_info[batsman]['prediction'],'nonstrike':batsman_info[nonstrike]['prediction'],'bowler':bowler_info[bowler]['prediction'],'runs':total,'wickets':wickets,'home':home,'ave_score':batsman_info[batsman]['ave_score'],'sr':batsman_info[batsman]['sr'],'bowl_ave':bowler_info[bowler]['bowl_ave'],'bowl_sr':bowler_info[bowler]['bowl_sr'],'econ':bowler_info[bowler]['econ'],'innings':number%2})
        print(num+1,'/',len(yaml_list))
        print()
        print()
