from data.databasemgr import DatabaseMgr

items = [1, 2, 3, 4, 5]

import datetime

print(len(items))

for i in range(2, 5):

    print(i)

today = datetime.date.today()

dateToday = today.strftime('%m-%d')

result = DatabaseMgr.instance().hotSecurities.find_one({'date':dateToday})

codeInfos = result['codeInfos']

for item in codeInfos:

    print(item)

print(result)

DatabaseMgr.instance().hotSecurities.delete_one({'date': dateToday})