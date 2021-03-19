import datetime
from data.databasemgr import DatabaseMgr
from typing import Dict, List

from data.securities import Securities
from data.codeInfo import CodeInfo
from storemgr.storemgr import SecuritiesMgr

def getInNarrowVibrate():

    result: List[CodeInfo] = []

    securitiesList: List[Securities] = SecuritiesMgr.instance().securitiesList

    for securities in securitiesList:

        if len(securities.klines) < 200:
            continue

        billion = 1000000000

        lastIndex = len(securities.klines) - 1

        if securities.capital * securities.klines[lastIndex].close < 3 * billion or securities.capital * securities.klines[lastIndex].close > 50 * billion:

            continue

        high = -999

        low = 999

        i = 0

        for kLine in reversed(securities.klines):

            high = max(kLine.high, high)

            low = max(kLine.low, low)

            if high < 1.15 * low:

                i += 1

            else:

                break

        if i < 25:

            continue

        result.append(securities.codeInfo)

    return result

def getHotSecurities():

    result: List[CodeInfo] = []

    securitiesList: List[Securities] = SecuritiesMgr.instance().securitiesList

    for securities in securitiesList:

        if len(securities.klines) < 200:

            continue

        billion = 1000000000

        lastIndex = len(securities.klines) - 1

        if securities.capital * securities.klines[lastIndex].close < 3 * billion or securities.capital * securities.klines[lastIndex].close > 50 * billion:

            continue

        if securities.getGreatIncreaseCountOf(20) >= 3:

            result.append(securities.codeInfo)

            continue

        if securities.getGreatIncreaseCountOf(10) == 2:

            result.append(securities.codeInfo)

            continue

        if securities.isGreatIncreaseInPast(day = 12, increase = 0.2):

            result.append(securities.codeInfo)

            continue

    return result

def refreshHotSecurities():

    items = getHotSecurities()

    today = datetime.date.today()

    dateToday = today.strftime('%m-%d')

    DatabaseMgr.instance().hotSecurities.delete_one({'date': dateToday})

    result = []

    for item in items:

        print(item.name)

        result.append(item.toJson())

    data = {'date':dateToday, 'codeInfos':result}

    DatabaseMgr.instance().hotSecurities.insert_one(data)

def refreshInNarrowVibrate():

    items = getInNarrowVibrate()

    today = datetime.date.today()

    dateToday = today.strftime('%m-%d')

    DatabaseMgr.instance().hotSecurities.delete_one({'date': dateToday})

    result = []

    for item in items:

        print(item.name)

        result.append(item.toJson())

    data = {'date':dateToday, 'codeInfos':result}

    DatabaseMgr.instance().hotSecurities.insert_one(data)

lastDate = 20201228

def getInIncreaase():

    result: List[CodeInfo] = []

    securitiesList: List[Securities] = SecuritiesMgr.instance().securitiesList

    for securities in securitiesList:

        if len(securities.klines) < 200:

            continue

        if securities.isSTIB() or securities.isST():

            continue

        billion = 1000000000

        lastIndex = len(securities.klines) - 1

        if securities.capital * securities.klines[lastIndex].close < 2 * billion or securities.capital * securities.klines[lastIndex].close > 20 * billion:

            continue

        if len(securities.crest) > 1 and len(securities.trough) > 0:

            if securities.crest[len(securities.crest) - 1].date > securities.trough[len(securities.trough) - 1].date:

                if securities.crest[len(securities.crest) - 1].high > securities.crest[len(securities.crest) - 2].high:

                    result.append(securities.codeInfo)

    return result

def refreshIncrease():

    items = getInIncreaase()

    today = datetime.date.today()

    dateToday = today.strftime('%m-%d')

    DatabaseMgr.instance().hotSecurities.delete_one({'date': dateToday})

    result = []

    for item in items:

        print(item.name)

        result.append(item.toJson())

    data = {'date':dateToday, 'codeInfos':result}

    DatabaseMgr.instance().hotSecurities.insert_one(data)

print('start load time = ', datetime.datetime.now())

def getReachLimitUp(count:int):

    result: List[Securities] = []

    securitiesList: List[Securities] = SecuritiesMgr.instance().securitiesList

    for securities in securitiesList:

        klineOfDate = None

        if len(securities.klines) < 200:

            continue

        billion = 1000000000

        lastIndex = len(securities.klines) - 1 - count

        # for kLine in reversed(securities.klines):
        #
        #     if kLine.date > lastDate:
        #
        #         lastIndex -= 1

        if securities.capital * securities.klines[lastIndex].close < 2 * billion or securities.capital * securities.klines[lastIndex].close > 50 * billion:

            continue

        if securities.isST() or securities.isSTIB():

            continue

        klineOfDate = securities.klines[lastIndex]

        if klineOfDate is not None:

            if securities.isSecondBoard():

                if (klineOfDate.close - klineOfDate.preClose)/klineOfDate.preClose > 0.19:

                    result.append(securities)

            else:

                if (klineOfDate.close - klineOfDate.preClose)/klineOfDate.preClose > 0.097:

                    result.append(securities)

    return result

def getReachLimitUps(count:int):

    result: List[Securities] = []

    for i in range(0, count):

        temps = getReachLimitUp(i)

        result.extend(temps)

    return result

def refreshReachLimitUp():

    items:List[Securities] = getReachLimitUps(count=5)

    today = datetime.date.today()

    dateToday = today.strftime('%m-%d')

    DatabaseMgr.instance().hotSecurities.delete_one({'type': 'limit'})

    result = []

    for item in items:

        print(item.codeInfo.name)

        result.append({'code':item.codeInfo.code, 'type':item.codeType})

    data = {'type': 'limit', 'codeInfos': result}

    DatabaseMgr.instance().hotSecurities.insert_one(data)

def getWWave():

    result: List[Securities] = []

    securitiesList: List[Securities] = SecuritiesMgr.instance().securitiesList

    for securities in securitiesList:

        klineOfDate = None

        if len(securities.klines) < 200:

            continue

        billion = 1000000000

        lastIndex = len(securities.klines) - 1

        if securities.capital * securities.klines[lastIndex].close < 2 * billion or securities.capital * securities.klines[lastIndex].close > 50 * billion:

            continue

        if securities.isSTIB() or securities.isST() or securities.pe == '--':

            continue

        if securities.isWShape():

            result.append(securities)

    return result

def refreshWWave():

    items:List[Securities] = getWWave()

    print(len(items))

    today = datetime.date.today()

    dateToday = today.strftime('%m-%d')

    DatabaseMgr.instance().hotSecurities.delete_one({'type': 'w'})

    result = []

    for item in items:

        print(item.codeInfo.name)

        result.append({'code':item.codeInfo.code, 'type':item.codeType})

    data = {'type': 'w', 'codeInfos': result}

    DatabaseMgr.instance().hotSecurities.insert_one(data)