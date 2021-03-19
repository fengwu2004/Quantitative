from webserver.RequestBaseManager import RequestBaseManager
from data.databasemgr import DatabaseMgr
import datetime

class HandleHotToday(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        today = datetime.date.today()

        dateToday = today.strftime('%m-%d')

        datas = DatabaseMgr.instance().hotSecurities.find_one({'type':'w'})

        wWavecodeInfos = datas['codeInfos']

        datas = DatabaseMgr.instance().hotSecurities.find_one({'type':'limit'})

        reachLimits = datas['codeInfos']

        self.write({'success': 1, "data":{"w":wWavecodeInfos, 'limit':reachLimits}})