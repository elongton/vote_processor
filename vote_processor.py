# Scenarios to weed out:
#
# 1. Same person sits at one computer and spams the voting system
#     a. Same IP address
#     b. Same book
#     c. time stamp within 2 minutes of the last
# 2. One person goes to multiple computers, or uses IP vanish
#     a. Same book
#     b. votes are sequential and
#
# Strategy:
# 1. Split into votes for each title
#     a. title_dict = {title:{
#                         votes:        [[ip address,timestamp], ...],  <== Use len(title_dic['title']['votes'])
#                         votes_by_ip:
#
#                            },
#                        title:{},...}
# 2. Total votes per title: title_dict[title].count()

import csv
import datetime

def lookup(dic, key, *keys):
    if keys:
        return lookup(dic.get(key, {}), *keys)
    return dic.get(key)


csv_file = csv.DictReader(open("votes.csv"))
vote_dict = {}
for row in csv_file:
    #it's a potential key because this algorithm gathers new titles as it goes along
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




# print(vote_dict)

######Prints out total votes by different IP addresses#######
real_votes = 0
for book,ips in vote_dict.items():
    ipTotal = 0
    voteTotal = 0
    for key,number in ips.items():
        ipTotal = ipTotal+1
        voteTotal = voteTotal + number
    print(str(book))
    print(str(ipTotal) + ' IPs' + ', ' + str(voteTotal) + ' total votes')
    print('----------------------------')



# print(vote_dict['<u>Rest in Peace Rashawn Reloaded</u> by Ronnie Sidney, II'])
# print(vote_dict['<u>The Inheritance</u> by Jennifer Ann Reed'])
