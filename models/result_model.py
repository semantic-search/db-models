import mongoengine


class ResultModel(mongoengine.EmbeddedDocument):
    model_name = mongoengine.StringField(required=True)
    results = mongoengine.DictField(required=True)
