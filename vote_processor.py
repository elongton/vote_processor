import csv
import datetime as dt

def lookup(dic, key, *keys):
    if keys:
        return lookup(dic.get(key, {}), *keys)
    return dic.get(key)


# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
# datetime_object = dt.datetime.strptime('2018-03-02 01:05:03', '%Y-%m-%d %I:%M:%S')
# datetime_object2 = dt.datetime.strptime('2018-03-02 01:06:03', '%Y-%m-%d %I:%M:%S')


# mytime = datetime.datetime(2018, 3, 2, hour=1, minute=3, second=3, microsecond=0)
# mytime2 = datetime.datetime(2018, 3, 2, hour=1, minute=5, second=3, microsecond=0)
# print((datetime_object2-datetime_object).total_seconds())


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

# print(vote_dict)
######Prints out total votes by different IP addresses#######
# for book,ips in ip_vote_dict.items():
#     ipTotal = 0
#     voteTotal = 0
#     for key,number in ips.items():
#         ipTotal = ipTotal+1
#         voteTotal = voteTotal + number
#     print(str(book))
#     print(str(ipTotal) + ' IPs' + ', ' + str(voteTotal) + ' total votes')
#     print('----------------------------')

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
        if ((abs((timestamp - beforestamp).total_seconds()) < tolerance) and (beforename == potential_title)):
            quick_vote_dict[potential_title] = quick_vote_dict[potential_title] + 1
    beforestamp = timestamp
    beforename = potential_title

print(quick_vote_dict)
