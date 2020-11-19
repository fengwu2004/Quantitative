import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.httpserver
import datetime
from data.databasemgr import DatabaseMgr
from typing import Dict, List

from data.securities import Securities
from data.codeInfo import CodeInfo
from storemgr.storemgr import SecuritiesMgr
from webserver.handleCapitalInfo import HandleCapitalInfo
from webserver.handleContinueIncrease import HandleContinueIncrease
from webserver.handleHotToday import HandleHotToday
from webserver.handleTouchHigh import HandleTouchHigh
from webserver.handleGreatIncrease import HandleGreatIncrease
from webserver.handleThreeDayGreatIncreaseEx import HandleThreeDayGreatIncrease
from webserver.handleInIncrease import HandleInIncrease
from webserver.handleInDecrease import HandleInDecrease
from webserver.handleInLow import HandleInLow


def make_app():

    app = tornado.web.Application([
        ("/upload/capital", HandleCapitalInfo),
        ("/ask/continue", HandleContinueIncrease),
        ("/ask/touchHigh", HandleTouchHigh),
        ("/ask/greatIncrease", HandleGreatIncrease),
        ("/ask/threedaygreateincrease", HandleThreeDayGreatIncrease),
        ("/ask/increase", HandleInIncrease),
        ("/ask/decrease", HandleInDecrease),
        ("/ask/inLow", HandleInLow),
        ("/ask/hottoday", HandleHotToday)
    ])

    server = tornado.httpserver.HTTPServer(app, max_buffer_size=512 * 1024 * 1024)

    server.listen(8888)

    tornado.ioloop.IOLoop.instance().start()

def getHotSecurities():

    result: List[CodeInfo] = []

    securitiesList: List[Securities] = SecuritiesMgr.instance().securitiesList

    for securities in securitiesList:

        if len(securities.klines) < 200:

            continue

        billion = 1000000000

        lastIndex = len(securities.klines) - 1

        if securities.capital * securities.klines[lastIndex].close < 4 * billion or securities.capital * securities.klines[lastIndex].close > 50 * billion:

            continue

        if securities.getGreatIncreaseCountOf(15) >= 3:

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

        result.append(item.toJson())

    data = {'date':dateToday, 'codeInfos':result}

    DatabaseMgr.instance().hotSecurities.insert_one(data)

print('start load time = ', datetime.datetime.now())

SecuritiesMgr.instance()

refreshHotSecurities()

print('load finish time = ', datetime.datetime.now())

if __name__ == "__main__":

    make_app()