from datetime import datetime
from .abs import ABS
import peewee

class Logging(ABS):
    """
        Model to store MINIMUM_TRAINING_INTENT_CONFIDENCE
    """

    text = peewee.CharField(max_length=1000)
    intent = peewee.CharField(max_length=100)
    confidence = peewee.FloatField(default=0.0)
    date = peewee.DateTimeField(default=datetime.now)
