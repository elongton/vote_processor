import csv
import datetime

def lookup(dic, key, *keys):
    if keys:
        return lookup(dic.get(key, {}), *keys)
    return dic.get(key)


csv_file = csv.DictReader(open("votes.csv"))
vote_dict = {}
for row in csv_file:
    potential_key = row['\ufeff"YAVA Nominations"']
    if (vote_dict.get(potential_key) == None):
        new_dict = {}                           #
        new_dict[row['User IP']] = 1            #
        vote_dict[potential_key] = new_dict     #
    else:
        if (lookup(vote_dict[potential_key], row['User IP']) == None):         #
            vote_dict[potential_key][row['User IP']] = 1
        else:
            vote_dict[potential_key][row['User IP']] = vote_dict[potential_key][row['User IP']] + 1

for key,value in vote_dict.items():
    print(str(value) + ' => ' + str(key))
