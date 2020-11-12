import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.httpserver
import datetime

from storemgr.storemgr import SecuritiesMgr
from webserver.handleBlockInfo import HandleBlockInfo
from webserver.handleCapitalInfo import HandleCapitalInfo
from webserver.handleContinueIncrease import HandleContinueIncrease
from webserver.handleTouchHigh import HandleTouchHigh
from webserver.handleGreatIncrease import HandleGreatIncrease
from webserver.handleThreeDayGreatIncreaseEx import HandleThreeDayGreatIncrease
from webserver.handleInIncrease import HandleInIncrease
from webserver.handleInDecrease import HandleInDecrease
from webserver.handleInLow import HandleInLow
from webserver.HandleTotalSecurities import HandleTotalSecurities
from webserver.HandleUploadDB import HandleUploadDB

def make_app():

    app = tornado.web.Application([
        ("/upload/block", HandleBlockInfo),
        ("/upload/capital", HandleCapitalInfo),
        ("/ask/continue", HandleContinueIncrease),
        ("/ask/touchHigh", HandleTouchHigh),
        ("/ask/greatIncrease", HandleGreatIncrease),
        ("/ask/threedaygreateincrease", HandleThreeDayGreatIncrease),
        ("/ask/increase", HandleInIncrease),
        ("/ask/decrease", HandleInDecrease),
        ("/ask/inLow", HandleInLow),
        ("/ask/totalsecurities", HandleTotalSecurities),
        ("/ask/uploadkLineDB", HandleUploadDB),
    ])

    server = tornado.httpserver.HTTPServer(app, max_buffer_size=512 * 1024 * 1024)

    server.listen(8888)

    tornado.ioloop.IOLoop.instance().start()


print('start load time = ', datetime.datetime.now())
SecuritiesMgr.instance()
print('load finish time = ', datetime.datetime.now())

if __name__ == "__main__":
    make_app()