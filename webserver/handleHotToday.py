from webserver.RequestBaseManager import RequestBaseManager
from data.databasemgr import DatabaseMgr
import datetime

class HandleHotToday(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        today = datetime.date.today()

        dateToday = today.strftime('%m-%d')

        result = DatabaseMgr.instance().hotSecurities.find_one({'date':dateToday})

        codeInfos = result['codeInfos']

        self.write({'success': 1, "data":{"codeInfos":codeInfos}})