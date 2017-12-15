import os
import json
import peewee
from urllib.parse import urlparse

result = urlparse(os.environ.get('DATABASE_URL'))
psql_db = peewee.PostgresqlDatabase(database=result.path[1:],
                                    user=result.username,
                                    host=result.hostname,
                                    password=result.password)


class DatabaseMiddleware(object):
    """
    Database Middleware for managing database(db) connections
    """

    def process_resource(self, req, resp, resource, params):
        """
        Open a db connection for each request
        """
        try:
            message_data = req.bounded_stream.read()
            message_data = json.loads(message_data.decode('utf-8'))
            req.context['request'] = message_data
        except BaseException:
            req.context['request'] = {}
        psql_db.connect()

    def process_response(self, req, resp, resource, request_succeded):
        """
        Close the db on each response
        """
        if not psql_db.is_closed():
            psql_db.close()
