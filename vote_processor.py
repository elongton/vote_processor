import csv
import datetime as dt

def lookup(dic, key, *keys):
    if keys:
        return lookup(dic.get(key, {}), *keys)
    return dic.get(key)

tolerance = input("How many seconds between votes is a quickvote?:")
#this script counts votes by IP address
csv_file = csv.DictReader(open("votes.csv"))
ip_vote_dict = {}
for row in csv_file:
    #it's a potential key because this algorithm gathers new titles as it goes along
    potential_title = row['\ufeff"YAVA Nominations"']
    if (ip_vote_dict.get(potential_title) == None):
        new_dict = {}
        new_dict[row['User IP']] = 1
        ip_vote_dict[potential_title] = new_dict
    else:
        if (lookup(ip_vote_dict[potential_title], row['User IP']) == None):
            ip_vote_dict[potential_title][row['User IP']] = 1
        else:
            ip_vote_dict[potential_title][row['User IP']] = ip_vote_dict[potential_title][row['User IP']] + 1

#this script finds fraudulent behavior by comparing timestamps
csv_file = csv.DictReader(open("votes.csv"))
quick_vote_dict = {}
beforestamp = None
beforename = None
for row in csv_file:
    potential_title = row['\ufeff"YAVA Nominations"']
    timestamp = dt.datetime.strptime(row['Entry Date'], '%Y-%m-%d %H:%M:%S')
    if (quick_vote_dict.get(potential_title) == None):
        quick_vote_dict[potential_title] = 0
    if ((beforestamp is not None) and (beforename is not None)):
        if ((abs((timestamp - beforestamp).total_seconds()) < int(tolerance)) and (beforename == potential_title)):
            quick_vote_dict[potential_title] = quick_vote_dict[potential_title] + 1
    beforestamp = timestamp
    beforename = potential_title


final_dictionary = {}
######Finds total votes by different IP addresses#######
for book,ips in ip_vote_dict.items():
    ipTotal = 0
    voteTotal = 0
    for key,number in ips.items():
        ipTotal = ipTotal+1
        voteTotal = voteTotal + number
    final_dictionary[book] = {'ipTotal': ipTotal, 'voteTotal': voteTotal}

for book,quickvotes in quick_vote_dict.items():
    final_dictionary[book]['quickVotes'] = quickvotes
#
# print(final_dictionary)

######Prints the results#########
for book,votevalues in final_dictionary.items():
    print(str(book))
    print(str(votevalues['ipTotal']) + ' IPs, ' + str(votevalues['voteTotal']) + ' total votes, ' + str(votevalues['quickVotes']) + ' quick votes')
    print('----------------------------')
