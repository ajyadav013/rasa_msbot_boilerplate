import peewee
from app.middlewares.database import psql_db

class ABS(peewee.Model):
    """
    Absolute Base Class
    """

    class Meta:
        database = psql_db

    
