import json
from re import I

def set_score(dic, key, arg):
    tup = dic.get(key)
    win, nulls, los, total = tup
    if arg == 0:
        los += 1
    if arg == 1:
        nulls += 1
    elif arg == 3:
        win += 1
    total = win*3+nulls
    lst = [win, nulls, los, total]
    tup = tuple(lst)
    dic[key] = tup

def res_match(lst, dic):
    # lst ['Brentford', '1', '0', 'Arsenal']
    # 0-1 2-3
    point_team1 = lst[1]
    point_team2 = lst[2]
    if point_team1 == point_team2:
        set_score(dic, lst[0], 1)
        set_score(dic, lst[3], 1)
    elif point_team1 > point_team2:
        set_score(dic, lst[0], 3)
        set_score(dic, lst[3], 0)
    elif point_team1 < point_team2:
        set_score(dic, lst[0], 0)
        set_score(dic, lst[3], 3)

def init_dic(lst,dic):
    for line in en:
        lst = line.split()
        lst.remove('-')
        for i in lst:
            if i.isdigit != True:
                dic[i] = score
    
dic = {}
win, nulls, los, total = 0, 0, 0, 0
 
table = [win, nulls, los, total]
score = tuple(table)

with open('res.txt', 'r', encoding='utf-8') as en:
    for line in en:
        lst = line.split()
        lst.remove('-')
        for i in lst:
            if i.isdigit() != True:
                if i in dic.keys():
                    continue
                else:
                    dic[i] = score
            else:
                i = int(i)
        res_match(lst,dic)

with open('result.json', 'w', encoding='utf-8') as eng:
    eng.write(json.dumps(dic))
    print('Save complete!')

for i in dic:
    print(f'{i}: {dic.get(i)}')
    