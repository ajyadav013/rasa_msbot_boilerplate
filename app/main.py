import falcon
import os
import sys
import psycopg2
from urllib.parse import urlparse
import json

CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.append('/'.join(i for i in CWD.split('/')[:-1]))
from app import bot
from app.middlewares.user import (UserMiddleware, )
from app.middlewares.database import (DatabaseMiddleware, )


class App(falcon.API):
    """
    Base App linking WSGI and Falcon Framework
    """

    def __init__(self, bott, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.add_route('/bot', bott)

middleware = [DatabaseMiddleware(), UserMiddleware()]
bott = bot.Bot()
application = App(bott, middleware=middleware)

if __name__ == "__main__":
    from development import check_dm as test
    test.run_application()
