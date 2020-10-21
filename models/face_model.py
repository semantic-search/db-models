import mongoengine
from .cache_model import Cache


class FaceModel(mongoengine.Document):
    document = mongoengine.ReferenceField(Cache, reverse_delete_rule=mongoengine.CASCADE, required=True)
    person = mongoengine.StringField(required=True)
    file = mongoengine.FileField(required=True)
    meta = {
        'db_alias': 'core',
        'collection': 'features'
    }