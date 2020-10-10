import mongoengine


class Result(mongoengine.EmbeddedDocument):
    model_name = mongoengine.StringField(required=True)
    results = mongoengine.ListField(required=True)
