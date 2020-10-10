import mongoengine
import datetime
from .file_model import FilesModel
from .result_model import ResultModel

class Cache(mongoengine.Document):
    """Main model"""
    file_name = mongoengine.StringField(required=True)
    """Name of the file (blob name)"""
    file = mongoengine.FileField(required=True)
    """Original File"""
    mime_type = mongoengine.StringField(required=True)
    """Mime types can be ["jpeg","jpg", "png", "wav","pdf", "docx", "pptx", "xlsx", "epub"] """
    files = mongoengine.EmbeddedDocumentListField(FilesModel)
    is_doc_type = mongoengine.BooleanField(required=True)
    date = mongoengine.DateTimeField(default=datetime.datetime.now)
    results = mongoengine.EmbeddedDocumentListField(ResultModel)
    meta = {
        'db_alias': 'core',
        'collection': 'cache'
    }
