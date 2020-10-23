import mongoengine
import datetime
from .file_model import FilesModel


class Cache(mongoengine.Document):
    """Main model"""
    file_name = mongoengine.StringField(required=True)
    """Name of the file (blob name)"""
    file = mongoengine.FileField(required=True)
    """Original File"""
    mime_type = mongoengine.StringField(required=True)
    """Mime types can be ["jpeg","jpg", "png", "wav","pdf", "docx", "pptx", "xlsx", "epub"] """
    files = mongoengine.EmbeddedDocumentListField(FilesModel, default=None)
    is_doc_type = mongoengine.BooleanField(required=True)
    date = mongoengine.DateTimeField(default=datetime.datetime.now)
    text = mongoengine.StringField(max_length=None, default=None)
    is_stt = mongoengine.BooleanField(required=False)
    contains_images = mongoengine.BooleanField(default=None)
    image_location = mongoengine.DictField(default=None)
    labels = mongoengine.ListField(default=None)
    scores = mongoengine.ListField(default=None)
    faces = mongoengine.ListField(default=None)
    meta = {
        'db_alias': 'core',
        'collection': 'cache'
    }
