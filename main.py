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
from webserver.handleUploadStocks import HandleUploadStocks


def make_app():

    app = tornado.web.Application([
        ("/upload/capital", HandleCapitalInfo),
        ("/ask/continue", HandleContinueIncrease),
        ("/ask/touchHigh", HandleTouchHigh),
        ("/ask/greatIncrease", HandleGreatIncrease),
        ("/ask/threedaygreateincrease", HandleThreeDayGreatIncrease),
        ("/upload/allstocks", HandleUploadStocks),
        ("/ask/decrease", HandleInDecrease),
        ("/ask/inLow", HandleInLow),
        ("/ask/inLow", HandleInLow),
        ("/ask/hottoday", HandleHotToday)
    ])

    server = tornado.httpserver.HTTPServer(app, max_buffer_size=512 * 1024 * 1024)

    server.listen(8888)

    tornado.ioloop.IOLoop.instance().start()

print('load finish time = ', datetime.datetime.now())

if __name__ == "__main__":

    make_app()