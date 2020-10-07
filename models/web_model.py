import mongoengine
import datetime


class Web(mongoengine.Document):
    url = mongoengine.StringField(required=True)
    text = mongoengine.StringField(max_length=None, default=None)
    date = mongoengine.DateTimeField(default=datetime.datetime.now)
    meta = {
        'db_alias': 'core',
        'collection': 'web'
    }
