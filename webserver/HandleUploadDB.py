import json
from webserver.RequestBaseManager import RequestBaseManager
from data.databasemgr import DatabaseMgr
from data.block import CodeInfo, BlockInfo
from data.codeInfo import CodeInfo
from storemgr.storemgr import SecuritiesMgr
from strategy.find_continue_increase import FindContinueIncrease
import os

class HandleUploadDB(RequestBaseManager):

    def prepare(self):

        self.request.connection.set_max_body_size(512 * 1024 * 1024)

    def post (self, *args, **kwargs):

        data = bytes(self.request.body)

        try:

            os.remove("stockhistory.db")

        except IOError:

            pass

        f = open('stockhistory.db', 'w+b')

        f.write(data)

        f.close()

        self.write({'success': 1})