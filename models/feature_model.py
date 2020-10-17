import mongoengine
from .cache_model import Cache


class Features(mongoengine.Document):
    document = mongoengine.ReferenceField(Cache, reverse_delete_rule=mongoengine.CASCADE, required=True)
    feature = mongoengine.BinaryField(required=True)
    file = mongoengine.FileField(required=True)
    meta = {
        'db_alias': 'core',
        'collection': 'features'
    }