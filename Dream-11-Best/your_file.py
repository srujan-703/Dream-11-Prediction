import builtins
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

file_path = './player_names.txt'
with builtins.open(file_path, 'r') as f:
    player_names = f.read().splitlines()
k=player_names[:]
# for i in k:
#     print(i)
with builtins.open(file_path, 'w') as f:
    f.write('')
    
    # f.write(k)
with builtins.open(file_path, 'a') as f:
    f.write("Presentsdata \n")
    f.write("Hello data got "+str(len(k))+"\n")
print("printting k",len(k))
# f.write("Hello data got "+str(len(k)))
# for i in k:
#     with builtins.open(file_path, 'a') as f:
#         f.write("Hello "+i)
#         f.write("\n")
# team_b_wk = ["AT CAREY"]
# team_a_wk = ["MS DHONI"]
# team_a_bat = ["Virat Kohli", "RG Sharma", "Shikhar Dhawan", "KL Rahul","Rishabh Pant"]
# team_b_bat = ["DA WARNER","UT KHAWAJA","SPD SMITH","M LABUSCHAGNE","TM HEAD"]
# team_b_bowl = ["NM LYON","JR HAZLEWOOD","PJ CUMMINS","MA STARC","MG JOHNSON"]     
# team_a_bowl = ["R ASHWIN","RA JADEJA","JJ BUMRAH","MOHAMMED SHAMI","B KUMAR"]
# Process the player names
# ...
team_b_wk = [k[11]]
team_a_wk = [k[10]]
team_a_bat = k[:5]
team_b_bat = k[12:17]
team_b_bowl = k[17:23]   
team_a_bowl=k[5:10]
print("teams ")
print(team_a_bat)
print(team_a_bowl)
print(team_a_wk)
print(team_b_bat)
print(team_b_bowl)
print(team_b_wk)
# Print the processed player names (for testing purposes)
# print(len(player_names),player_names,len(player_names))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
def batting(name):
    
    format= 1
    format_name = "T20s"
    player = name
    url = "http://search.espncricinfo.com/ci/content/player/search.html?search=" + player.lower().replace(" ","+") + "&x=0&y=0"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # print("IN batting ",player)
    newd={
        "M LABUSCHAGNE":787987,
        "TM HEAD":530011
    }
    if player in newd:
        player_id=newd[player]
    else:
        player_id = str(soup.find_all(class_='ColumnistSmry')[0]).split('.html')[0].split('/')[-1]
    # print(player_id)
    df = pd.read_html(f'https://stats.espncricinfo.com/ci/engine/player/{player_id}.html?class={format};template=results;type=batting;view=innings')[3]
    # print(df.head())
    runs = []
    notout = []
    innings = 0
    batting_avg = []
    hundreds = []
    last_f=0
    for i in df.Runs:
        if i != 'DNB' and i != 'TDNB' and i != 'sub' and i!="absent":
            if '*' not in i:
                innings += 1
                notout.append(False)
            else:
                notout.append(True)
            runs.append(int(i.replace('*','')))
            if innings != 0:
                if innings==5:
                    last_f=sum(runs)/innings
                batting_avg.append(sum(runs)/innings)
            else:
                batting_avg.append(0)
            if len(hundreds) == 0:
                if runs[0] > 100:
                    hundreds.append(1)
                else:
                    hundreds.append(0)

            if runs[len(runs)-1]>=100 and len(hundreds)>0:
                hundreds.append(hundreds[len(hundreds)-1]+1)
            elif len(hundreds)>0:
                hundreds.append(hundreds[len(hundreds)-1])
        else:
            if len(runs) == 0:
                batting_avg.append(0)
                hundreds.append(0)
            else:
                batting_avg.append(batting_avg[len(batting_avg)-1])
                hundreds.append(hundreds[len(hundreds)-1])
    return ([batting_avg[-1],last_f])
def bowling(name):
    
    format=3
    format_name = "T20s"
    player = name
    url = "http://search.espncricinfo.com/ci/content/player/search.html?search=" + player.lower().replace(" ","+") + "&x=0&y=0"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # print("in bowling",player)
    newd={"R ASHWIN":26421,
          "MG JOHNSON":6033,
          "B KUMAR":326016}
    if player in newd:
        player_id=newd[player]
    else:
        player_id = str(soup.find_all(class_='ColumnistSmry')[0]).split('.html')[0].split('/')[-1]
    # player_id = str(soup.find_all(class_='ColumnistSmry')[0]).split('.html')[0].split('/')[-1]
    # print(player_id)
    df = pd.read_html(f'https://stats.espncricinfo.com/ci/engine/player/{player_id}.html?class={format};template=results;type=bowling;view=innings')[3]
    # print(df.head())
    bo=0
    inn=len(df)
    # print(inn)
    runs=0
    c1=0
    lastruns=1
    for i in df.Runs:
        if i!= '-':
            runs+=int(i)
            c1+=1
        if c1==5:
            lastruns=runs
#     print(runs)
    wc=0
    c1=0
    lastwi=1
    for i in df.Wkts:
        if i!= '-':
            wc+=int(i)
            c1+=1
        if c1==5:
            lastwi=wc
#     print(wc)
    bow_avg=(runs/wc)
    return ([bow_avg,(lastruns/lastwi)])
import itertools



# Generate all combinations
all_combinations = []
for i in range(11, 12):
    for combination in itertools.combinations(team_a_wk + team_b_wk + team_a_bat + team_b_bat + team_b_bowl + team_a_bowl, i):
        if "AT CAREY" not in combination and "MS DHONI" not in combination:
            continue
        if not any(player in team_a_bat + team_a_bowl for player in combination) or not any(player in team_b_bat + team_b_bowl for player in combination):
            continue
        all_combinations.append(combination)
        
print("Number of possible combinations:", len(all_combinations))
# print(all_combinations[0])
# all_players=team_a_wk+team_b_wk+team_a_bat+team_b_bat+team_a_bowl+team_b_bowl
# def f(name):
d={}
for i in team_a_wk:
    l=batting(i)
#     print(i,)
    # print(i,l[0],l[1])
    val=(l[0])+(l[1]*(0.5))
    d[i]=val
for i in team_b_wk:
    l=batting(i)
#     print(i,)
    # print(i,l[0],l[1])
    val=(l[0])+(l[1]*(0.5))
    d[i]=val
for i in team_a_bat:
    l=batting(i)
#     print(i,)
    # print(i,l[0],l[1])
    val=(l[0])+(l[1]*(0.5))
    
    d[i]=val
for i in team_b_bat:
    l=batting(i)
#     print(i,)
    # print(i,l[0],l[1])
    val=(l[0])+(l[1]*(0.5))
    
    d[i]=val
for i in team_b_bowl:
    l=bowling(i)
#     print(i,)
    # print(i,l[0],l[1])
    val=(l[0])+(l[1]*1)
    
    d[i]=val
for i in team_a_bowl:
    l=bowling(i)
    # print(l)
    # print(i,l[0],l[1])
    val=(l[0])+(l[1]*1)
    
    d[i]=val


# print(type(all_combinations[0]))
for i in d.items():
    print(i[0],i[1])
print(d)
score_d={}
for i in all_combinations:
    val=0
    for j in i:
        val+=d[j]
    score_d[i]=val

# sortedDict = sorted(score_d)
newl=list(score_d.values())
# sorted(newl,reversed=True)
newl.sort()
newl=newl[::-1]
print(newl[:10])
# print(i,score_d[i])
maxl=list(score_d.items())
# print(maxl)
rl=sorted(score_d.items(),key=lambda x:x[1],reverse=True)
print(rl[0])
with builtins.open(file_path, 'a') as f:
        f.write("DREAM 11 TEAM")
print(type(rl[0]))
nrl=list(rl[0])
nrl.pop()
print(nrl)
for i in nrl:
    for j in i:
        with builtins.open(file_path, 'a') as f:
            f.write(j)
            f.write("\n")
# print("kast",rl[:3])