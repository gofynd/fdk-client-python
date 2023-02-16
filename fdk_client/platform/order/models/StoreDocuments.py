"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Document import Document



class StoreDocuments(BaseSchema):
    #  swagger.json

    
    gst = fields.Nested(Document, required=False)
    
