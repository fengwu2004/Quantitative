from os import walk
from data.codeInfo import CodeInfo
from storemgr.load import getLines, formatData
from data.databasemgr import DatabaseMgr
from storemgr.storemgr import SecuritiesMgr
from strategy import refreshWWave, refreshReachLimitUp
from data.securities import Securities
from typing import Dict, List
import datetime

import json
from collections import defaultdict

def saveToDB():
    
    mypath = 'C:/Users/Administrator/Desktop/tdx-gbk/'
    
    f = []
    
    for (dirpath, dirname, filenames) in walk(mypath):
        
        f.extend(filenames)
    
    print(f)

    stocks = []
    
    securitiesList = []
    
    for file in f:

        filePath = mypath + file
        
        if filePath.find('.txt') == -1:
            
            continue
        
        stock = formatData(getLines(filePath))

        securitiesList.append(stock)
    
        stocks.append(stock.toJson())

    DatabaseMgr.instance().stocks.remove({})

    DatabaseMgr.instance().stocks.insert_many(stocks)

    result = []

    for stock in stocks:

        codeInfo = CodeInfo()

        codeInfo.code = stock['code']

        codeInfo.name = stock['name']

        result.append(codeInfo.toJson())

    DatabaseMgr.instance().stockInfos.remove({})

    DatabaseMgr.instance().stockInfos.insert_many(result)



SecuritiesMgr.instance()

refreshWWave()

refreshReachLimitUp()
