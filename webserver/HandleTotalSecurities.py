import json
from webserver.RequestBaseManager import RequestBaseManager
from data.databasemgr import DatabaseMgr
from data.block import CodeInfo, BlockInfo
from data.codeInfo import CodeInfo
from storemgr.storemgr import SecuritiesMgr
from strategy.find_continue_increase import FindContinueIncrease


class HandleTotalSecurities(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        f = open('stockhistory.db', 'r+b')

        data = f.read()

        f.close()

        print("传输完成")

        self.write(data)