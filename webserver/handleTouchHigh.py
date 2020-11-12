import json
from webserver.RequestBaseManager import RequestBaseManager
from data.databasemgr import DatabaseMgr
from data.block import CodeInfo, BlockInfo
from data.codeInfo import CodeInfo
from storemgr.storemgr import SecuritiesMgr
from strategy.find_continue_increase import FindContinueIncrease

def findTouchHigh():

    result:list[CodeInfo] = list()

    for securities in SecuritiesMgr.instance().securitiesList:

        lastIndex = len(securities.klines) - 1

        if lastIndex < 0:

            continue

        if securities.isST() or securities.isSTIB():

            continue

        if securities.toatlCapital() > 500 or securities.toatlCapital() < 50:

            continue

        if securities.isIncrease():

            result.append(securities.codeInfo)

    return result

class HandleTouchHigh(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        # data = json.loads(self.request.body.decode('utf-8'))
        
        codeInfos = findTouchHigh()

        result = list()

        for codeInfo in codeInfos:

            result.append(codeInfo.toJson())

        self.write({'success': 1, "data":{"codeInfos":result}})