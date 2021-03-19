import json
from webserver.RequestBaseManager import RequestBaseManager
from data.databasemgr import DatabaseMgr
from data.block import CodeInfo, BlockInfo

class HandleUploadStocks(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        if self.checkToken() is not True:
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))
        
        allInfos = data['codeInfos']

        DatabaseMgr.instance().stockInfos.remove({})

        DatabaseMgr.instance().stockInfos.insert_many(allInfos)

        self.write({'success': 1})